import requests

URL = 'mention_url_here'

headers = {
	"Postman-Token": "tokenid",
	"Host": "host_name",
	# mention all the rest of the key value pair here
}

# add certificates
crt_path = "file_path_of_pem_file"
key_path = "file_path_of_key_file"

certificate = (crt_path, key_path)

api_req = requests.get(url=URL, headers=headers, cert=certificate, verify=True)

# if error - also try for verify=False

if api_req.status_code == 200:
	output = api_req.json()
	print(output)

else:
	raise Exception("Exception - Status Code %s"%(api_req.status_code))
