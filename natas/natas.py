import ssl
import sys
import json
import time
import requests
import base64


def encodeCreds(username, password):
    stringToBeEncoded = username + ':' + password
    authorizationCookie = base64.b64encode(stringToBeEncoded)
    return(authorizationCookie)

def login(username, password, url, headers):

    with requests.Session() as s:
        post = s.get(url, headers=headers)
        print post.text





def main():
    username = 'natas0'
    password = 'natas0'
    level = 0
    url = 'http://natas{}.natas.labs.overthewire.org/'.format(str(level))
    cookie = encodeCreds(username, password)


    headers = {
        'Authorization': "Basic " + cookie
    }

    login(username, password, url, headers)

    print(cookie)


if __name__ == "__main__":
    main()
