import requests


def getToken():
    URL = "http://172.16.4.241/feedbacks/api/login.php"

    email = "satishmankar@gmail.com"
    passw = "12345"

    PARAMS = {'email': email, 'pass': passw}

    r = requests.get(url=URL, params=PARAMS)

    data = r.json()
    token = data['token']
    return token
