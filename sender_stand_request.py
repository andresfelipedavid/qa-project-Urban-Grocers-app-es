import requests
import configuration

# funcion para crear un nuevo usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body)
# funcion para crear un nuevo kit
def post_new_client_kit(body, token):
    headers = {"Authorization": f"Bearer {token}"}
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH, json=body, headers=headers)


