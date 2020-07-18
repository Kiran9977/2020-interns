import urllib.request as request
import json

with request.urlopen('https://api.exchangeratesapi.io/history?start_at=1999-01-01&end_at=2020-07-30') as response:
	source = response.read()
	data1 = json.loads(source)

with open("data.json", "w") as f:
	json.dump(data1, f,indent=4)
	