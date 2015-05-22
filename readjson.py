import json
from pprint import pprint
json_data=open('jsonFormated')
#json_data=open('jsonFile')

data = json.load(json_data)
pprint(data)
json_data.close()
