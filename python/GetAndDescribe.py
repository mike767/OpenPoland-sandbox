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

meta = "https://openpoland.net/api/asset/2688/meta/"
r = requests.get(meta, headers=headers)
metadata = json.loads(r.text)

def getDimDict(metadata):
	dict = {}
	for dim in metadata["dims"]:
		for dimVal in dim["values"]:
			dimId = dimVal["id"]
			dict[dimId] = dimVal["name"]
		
	return dict
	
dict = getDimDict(metadata)

data = "https://openpoland.net/api/asset/2688/data_filter/"
payload = json.dumps({
    "query": {
        "time": [2012],
        "nts": [3000000000]
    }
})
r = requests.post(data, payload, headers=headers)
data_resp = json.loads(r.text)

first_result = data_resp[0] 

print "Raw response : %s \n" % first_result 
print "\tJednostka	: {}".format(first_result[1])

dim_1_id = first_result[2]
print u"\t{} : {}".format(metadata["dims"][0]["name"], dict[first_result[2]])
print u"\t{} : {}".format(metadata["dims"][1]["name"], dict[first_result[3]])
print u'\tWartość 	: {} {}'.format(first_result[6], first_result[5])
print u"\tRok 		: %s" % first_result[4]

#Raw response : [u'3000000000', u'Region wschodni', 8316, 8306, u'2012', u'%', 8.45, u'B'] 
#
#	Jednostka	: Region wschodni
#	Zakres przedmiotowy : przedsiębiorstwa
#	Rodzaje przedsiębiorstw : przedsiębiorstwa z sektora usług
#	Wartość 	: 8.45 %
#	Rok 		: 2012
	

