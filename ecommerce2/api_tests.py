import requests
import json


def test_api():
    base_url = 'http://127.0.0.1:8000/api/'
    login_url = base_url + "auth/token/"
    products_url = base_url + 'products/'
    data = {
        'username': 'cfusiello',
        'password': 'password',
    }
    login_request = requests.post(login_url, data=data)

    """ options reference """
    # login_request.text
    # login_request.json()

    json_data = login_request.json()
    print("JSON Data = " + json.dumps(json_data, indent=4))

    token = json_data['token']
    print("Token = " + token)
    headers = {
        'Authorization': "JWT {0}".format(token)
    }
    products_request = requests.get(products_url, headers=headers)
    print("Products Request as text = " + products_request.text)
    print("Products Request as json = " + json.dumps(products_request.json(), indent=4))


if __name__ == "__main__":

    test_api()
