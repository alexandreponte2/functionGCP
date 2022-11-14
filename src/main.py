import base64
import json
import re
from sre_parse import ESCAPES
from google.cloud import secretmanager
from random import choice
import string


def secret_hello(event, context):
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    pub = json.loads(pubsub_message)
    print(pub)
    if "rotation" in pub:
        SECRET_ID = pub["name"].split("/")[3]
        PROJECT_ID = pub["name"].split("/")[1]
        tamanho_da_senha = 10
        caracteres = string.ascii_letters + string.digits
        SENHA_SEGURA = ''
        for i in range(tamanho_da_senha):
         SENHA_SEGURA += choice(caracteres)
        payload = SENHA_SEGURA
        print(SECRET_ID,PROJECT_ID)
        client = secretmanager.SecretManagerServiceClient()
        parent = f"projects/{PROJECT_ID}/secrets/{SECRET_ID}"
        payload = payload.encode('UTF-8')

        response = client.add_secret_version(
            request={
            "parent": parent,
            "payload": {"data": payload,}
            }
          )

        print(f'Added secret version: {response.name}')
        print(SECRET_ID, PROJECT_ID)
        print("SEGREDO ATUALIZADO!!!")
    else:
      print("Sem Segredos para Atualizar aqui...")
    return SECRET_ID, PROJECT_ID