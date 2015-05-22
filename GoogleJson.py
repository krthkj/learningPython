#!/usr/bin/python

import urllib2
import tempfile
import json

# pprint to print json data on screen
from pprint import pprint

# fetching Google data
url = "http://finance.google.com/finance/info?q=rpower"
response = urllib2.urlopen(url)

#storing google data in temp file
temp_html = tempfile.NamedTemporaryFile(mode='w+')
temp_html.write(response.read())
temp_html.seek(0)

# deleting unnecessary characters and making valid json temp file
temp_json = tempfile.NamedTemporaryFile(mode='w+')
delete_list = ["//" , "\n"]
for line in temp_html:
    for word in delete_list:
        line = line.replace(word, "")
    temp_json.write(line)
temp_html.close()
temp_json.seek(0)

# reading the json data from file
data = json.load(temp_json)

# printing json data stored in variable
# print "pretty print"
# pprint(data)

print "Fetched Data"
print data[0]['c_fix']	# change fix decimal
print data[0]['ccol']	# ??? usuall "chr"
print data[0]['cp_fix']	#  closing percentage fix decimal
print data[0]['e']	# Stock type NSE
print data[0]['id']	# ID
print data[0]['l_fix']	# last value fix decimal
print data[0]['lt']	# last trans           Jul 30, 3:29PM GMT+5:30
print data[0]['lt_dts']	# last trans date  2014-07-30T15:29:59Z
print data[0]['ltt']	# last trans time  3:29PM GMT+5:30
print data[0]['pcls_fix']	# prev day closing with fixed decimal
print data[0]['s']	# ? usually "0"
print data[0]['t']  # stock


# closing files
# temp_html.close()
temp_json.close()

# printing file names
# print temp_html.name
# print temp_json.name
