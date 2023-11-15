import requests
import json


def send_api(path, method):
	API_HOST = "http://165.246.44.237:11108/"
	url = API_HOST + path
	headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
	body = {
		"latitude": 0,
		"longitude": 0,
		"raspberryPiId": "10",
		"zone": "A"
	}
	
	try:
		if method =='GET':
			response = requests.get(url, headers=headers)
		elif method == 'POST':
			response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent='\t'))
	except Exception as ex:
		print(ex)

send_api('accident/workerFall', 'POST')
