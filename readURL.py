#!/usr/bin/python

import urllib2

# URL variable
url = 'http://finance.google.com/finance/info?client=ig&q=SBIN'

# Preparing a URL request
request = urllib2.Request(url)

# Response caught
response = urllib2.urlopen(request)

# gives the information about the response
# print response.info()

# printing the response to the console
print response.read()

