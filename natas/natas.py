import ssl
import sys
import json
import time
import requests
import base64
import os
from bs4 import BeautifulSoup


def encodeCreds(username, password):
    stringToBeEncoded = username + ':' + password
    auth_64 = base64.b64encode(stringToBeEncoded)
    return(auth_64)

def login(username, password, url, headers):
    with requests.Session() as s:
        post = s.get(url, headers=headers)
    return(post.text)

def eraseFile():
    filename = 'flags.txt'
    file = open(filename, 'w')
    file.write('')
    return()

def writeToFlagFile(flagToWrite, level):
    filename = 'flags.txt'
    file = open(filename, "a")
    file.write('Level ' + level + ' - ' + flagToWrite + '\n')
    file.close()
    return()

def natas0():
    url = 'http://natas0.natas.labs.overthewire.org/'
    username = 'natas0'
    password = 'natas0'
    auth_64 = encodeCreds(username, password)
    headers = {
        'Authorization': 'Basic ' + auth_64
    }
    print('[+] Logging into Natas 0 [+]')
    response = login(username, password, url, headers)
    natas1Password = response[857:889]
    print('Password for next level is: ' + natas1Password)
    return(natas1Password)

def natas1(natas1Password):
    url = 'http://natas1.natas.labs.overthewire.org/'
    username = 'natas1'
    auth_64 = encodeCreds(username, natas1Password)
    headers = {
        'Authorization': 'Basic ' + auth_64
    }
    print('[+] Logging into Natas 1 [+]')
    response = login(username, natas1Password, url, headers)
    natas2Password = response[1002:1034]
    print('Password for next level is: ' + natas2Password)
    return(natas2Password)

def main():
    os.system('clear')
    print('[+] Cleaning flags.txt of old passwords [+]')
    eraseFile()
    natas1Password = natas0()
    writeToFlagFile(natas1Password, '1')
    natas2Password = natas1(natas1Password)
    writeToFlagFile(natas2Password, '2')


if __name__ == "__main__":
    main()
