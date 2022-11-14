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


# SECRET_ID, PROJECTID = read_pubsub()

# print(SECRET_ID)
# print(PROJECTID)





# def read_pubsub(event, context):
#     pubsub_message = base64.b64decode(event['data']).decode('utf-8')
#     pub = json.loads(pubsub_message)
#     SECRET_ID = pub["name"].split("/")[3]
#     PROJECT_ID = pub["name"].split("/")[1]
#     print(SECRET_ID)
#     return SECRET_ID, PROJECT_ID


# SECRET_ID, PROJECTID = read_pubsub()

# print(SECRET_ID)
# print(PROJECTID)


# def add_secret_version(secret_id, payload):
#     PROJECT_ID = PROJECTID

#     client = secretmanager.SecretManagerServiceClient()

#     parent = f"projects/{PROJECT_ID}/secrets/{secret_id}"

#     payload = payload.encode('UTF-8')

#     response = client.add_secret_version(parent=parent, payload={'data': payload})

#     print(f'Added secret version: {response.name}')
#     return response


# def senhasegura():
  # tamanho_da_senha = 10
  # caracteres = string.ascii_letters + string.digits
  # # caracteres = string.ascii_letters + string.digits + string.punctuation
  # senha_segura = ''
  # for i in range(tamanho_da_senha):
  #   senha_segura += choice(caracteres)
  # return senha_segura


# pwdnow = senhasegura()


# add_secret_version(SECRET_ID, pwdnow)




