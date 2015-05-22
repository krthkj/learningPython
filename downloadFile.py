import urllib2
url = "http://finance.google.com/finance/info?q=rpower"
response = urllib2.urlopen(url)
output = open('jsonFile','w')
output.write(response.read())
output.close()


