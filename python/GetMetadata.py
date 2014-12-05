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

url = "https://openpoland.net/api/asset/2688/meta/"
r = requests.get(url, headers=headers)
js_resp = json.loads(r.text)

def getDimDict(metadata):
	dict = {}
	for dim in metadata["dims"]:
		for dimVal in dim["values"]:
			dimId = dimVal["id"]
			dict[dimId] = dimVal["name"]
		
	return dict
	
dict = getDimDict(js_resp)
print json.dumps(js_resp, indent=4, sort_keys=True, encoding="utf-8")