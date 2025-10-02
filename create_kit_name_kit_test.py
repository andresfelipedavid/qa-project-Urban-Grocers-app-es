from sender_stand_request import post_new_user, post_new_client_kit
from data import user_body

# funcion para tomar el token del usuario
def get_new_user_token():
    response = post_new_user(user_body)
    return response.json()["authToken"]

# Plantilla para possitive assert
def positive_assert(name_value):
    token = get_new_user_token()
    response = post_new_client_kit({"name": name_value}, token)
    assert response.status_code == 201
    assert response.json()["name"] == name_value

# Plantilla para negative assert
def negative_assert(name_value):
    token = get_new_user_token()
    response = post_new_client_kit({"name": name_value}, token)
    assert response.status_code == 400

# Plantilla para negative assert sin nombre
def negative_assert_missing_name():
    token = get_new_user_token()
    response = post_new_client_kit({}, token)
    assert response.status_code == 400

# tests - lista de comprobacion
def test_name_length_1():
    positive_assert("a")

def test_name_length_511():
    positive_assert("a" * 511)

def test_name_length_0():
    negative_assert("")

def test_name_length_512():
    negative_assert("a" * 512)

def test_special_characters():
    positive_assert("№%@,")

def test_spaces_allowed():
    positive_assert(" A Aaa ")

def test_numbers_allowed():
    positive_assert("123")

def test_missing_name():
    negative_assert_missing_name()

def test_name_as_number():
    token = get_new_user_token()
    response = post_new_client_kit({"name": 123}, token)
    assert response.status_code == 400

