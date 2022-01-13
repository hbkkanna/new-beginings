import config
import requests
import json

PATH = "http://localhost:8080/api/v1"

user = {
    "username": "Kannan Muthu",
    "dob": "March 15 1982",
    "address": "28 Roberts Road Exeter Ex2 4HD",
    "phone": "+44 7404384179"
}

update_user = {
    "username": "Kannan Muthu",
    "dob": "March 15 1982",
    "address": "28 Roberts Road Exeter Ex2 4HD",
    "phone": "+44 1111111"
}

invalid_input = {
    "dob": "March 15 1982",
    "address": "28 Roberts Road Exeter Ex2 4HD",
    "phone": "+44 1111111"
}


def delete_user(user_id):
    resp = requests.delete(url=PATH + "/users/" + user_id)
    if resp.status_code == 200:
        print("Delete user : {}".format(user_id))


def test_post():
    print("-----Start Create User test----")

    resp = requests.post(url=PATH + "/users", json=user)

    if resp.status_code != 201:
        raise AssertionError("Create user failed")

    resp_obj = json.loads(resp.content)
    print(resp_obj)

    resp = requests.post(url=PATH + "/users", json=user)
    if resp.status_code != 409:
        raise AssertionError("Duplicate user test failed")

    #delete_user(resp_obj.get("user_id", ""))

    resp = requests.post(url=PATH + "/users", json=invalid_input)
    if resp.status_code != 403:
        raise AssertionError("Invalid input user test failed")

    print("----Done Create User test-----")


def test_update():
    print("-----Start Update User test ------")
    resp = requests.post(url=PATH + "/users", json=user)
    resp_obj = json.loads(resp.content)

    resp = requests.put(url=PATH + "/users/" + resp_obj.get("user_id", ""), json=update_user)

    resp = requests.get(url=PATH + "/users/" + resp_obj.get("user_id", ""))

    resp_obj = json.loads(resp.content)
    if resp_obj.get("phone", None) != "+44 1111111":
        raise AssertionError("Update user test failed")

    resp = requests.put(url=PATH + "/users/" + resp_obj.get("user_id", ""), json=invalid_input)
    if resp.status_code != 403:
        raise AssertionError("Invalid input user test failed")

    resp = requests.put(url=PATH + "/users/" + "TT-099T", json=update_user)
    if resp.status_code != 404:
        raise AssertionError("Update user test NOT FOUND case failed")

    delete_user(resp_obj.get("user_id", ""))

    print("-----Done Update User test------")


def test_get():
    print("-----Start Get User test------")

    resp = requests.post(url=PATH + "/users", json=user)
    resp_obj = json.loads(resp.content)
    resp = requests.get(url=PATH + "/users/" + resp_obj.get("user_id", ""))

    delete_user(resp_obj.get("user_id", ""))

    resp = requests.get(url=PATH + "/users/" + "TT-099T")
    if resp.status_code != 404:
        raise AssertionError("get user test NOT FOUND case failed")
    print("-----Done Get User test------")


def test_delete():
    print("-----Start Delete User test------")

    resp = requests.post(url=PATH + "/users", json=user)
    resp_obj = json.loads(resp.content)

    resp = requests.delete(url=PATH + "/users/" + resp_obj.get("user_id", ""))
    if resp.status_code != 200:
        raise AssertionError("delete user case failed")

    resp = requests.delete(url=PATH + "/users/" + "TT-099T")
    if resp.status_code != 404:
        raise AssertionError("delete user test NOT FOUND case failed")
    print("-----Done Delete User test------")


def test_capacity():
    for i in range(100000):
        username = "Username" + str(i)
        user.update({"username": username})
        resp = requests.post(url=PATH + "/users", json=user)
        if resp.status_code != 201:
            print("Failed to create user")
            break;

if __name__ == "__main__":
    test_post()
    #test_get()
    #test_delete()
    #test_update()
    # test_capacity()
