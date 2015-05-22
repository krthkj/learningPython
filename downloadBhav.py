import urllib2

#download_url = "http://www.bseindia.com/download/BhavCopy/Equity/eq271213_csv.zip"
#download_url = "http://www.bseindia.com/download/BhavCopy/Equity/eq251213_csv.zip"
try:
	download_url = "http://karthikjain.in"
	bhavfile = urllib2.urlopen(download_url)
	output = open('bhav.zip','wb')
	output.write(bhavfile.read())
	output.close()
except urllib2.URLError , e:
	print ("url error")
except urllib2.HTTPError ,e: 
	print ("http err")
except ValueError ,e: 
	print (e)
	
