#!/usr/bin/python

import zipfile # read, test zipfile
import os, errno # delete file and handle error
import urllib2 # download file
import datetime # date and time object

# deletes the file
def silentRemove(filename):
	try:
		os.remove(filename)
		print filename + " removed"
	except OSError as e:
		if e.errno != errno.ENOENT:
			raise e
	return

# checks the zip file
def extractZip(bhavZipFile):
	if os.path.exists(bhavZipFile):
		try:
			fileHandler = zipfile.ZipFile(bhavZipFile,'r')
			if fileHandler.testzip():
				raise zipfile.BadZipfile
			for files in fileHandler.namelist():
				fileHandler.extract(files)
			fileHandler.close()
		except(zipfile.LargeZipFile, zipfile.BadZipfile) as e: 
			print(e)
		finally:
			silentRemove(bhavZipFile)
	return 

# Download  the zip file
def getBhav(bhavDate):
	downloadUrl = "http://www.bseindia.com/download/BhavCopy/Equity/eq"+bhavDate+"_csv.zip"
	bhavZipFile="eq"+bhavDate+"_csv.zip"
	output = open(bhavZipFile,'wb')
	try:
		output.write(urllib2.urlopen(downloadUrl).read())
		print bhavZipFile+" download success"
	except (urllib2.URLError, urllib2.HTTPError,ValueError) as e:
		print(e)
		print bhavZipFile+" download failed"
	finally:
		output.close()
	return bhavZipFile

# Generate today's date ddmmyy
def bhavDate ():
	return datetime.datetime.today().strftime("%d%m%y")

# Get History till date
# helps in setup of database
def bhavHistory(noOfDays):
	today = datetime.datetime.today()
	itr=1
	while itr != noOfDays:
		val = (today - datetime.timedelta(days=itr)).strftime("%d%m%y")
		extractZip(getBhav (val))
		itr += 1
	return

try:
	bhavHistory(5)
	extractZip(getBhav(bhavDate()))
except KeyboardInterrupt ,e :
	print e


