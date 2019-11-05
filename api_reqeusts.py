import requests

URL = 'mention_your_here'

headers = {
	"Postman-Token": "tokenid",
	"Host": "host_name",
	# mention all the rest of the key value pair here
}


api_req = requests.get(url=URL, headers=headers)

print(api_req.json())

if api_req.status_code == 200:
	output = api_req.json()
	print(output)

else:
	raise Exception("Exception - Status Code %s"%(api_req.status_code))
