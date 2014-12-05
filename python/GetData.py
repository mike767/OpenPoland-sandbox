# -*- coding: utf-8 -*-
'''
Before you run this script export your API TOKEN:
	
	export OP_token = "__YOUR TOKEN___"
	
'''
import requests, json, pprint, os

my_token = os.getenv("OP_token")
headers = {
    'content-type': 'application/json',
    'Authorization': 'Token {}'.format(my_token)
}

url = "https://openpoland.net/api/asset/2688/data_filter/"
payload = json.dumps({
    "query": {
        "time": [2005,2006,2007,2008,2009,2010,2011,2012,2013],
        "nts": [3060000000,3260000000,2000000000,6220000000,6040000000]
    }
})

r = requests.post(url, payload, headers=headers)
json_resp = json.loads(r.text)
#pprint.pprint(json_resp)
print json.dumps(json_resp, indent=4, sort_keys=True, encoding="utf-8")
print json_resp[0][1]