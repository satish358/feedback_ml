import requests


def checkUserValidorNot(email,passw):
    URL = "https://lostfound2.000webhostapp.com/api/login.php"
    token = {}
    PARAMS = {'email': email, 'pass': passw}

    r = requests.get(url=URL, params=PARAMS)

    data = r.json()
    token['token'] = data['token']
    token['status_code'] = r.status_code
    return token
