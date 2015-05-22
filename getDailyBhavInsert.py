#!/usr/bin/python

import zipfile # read, test zipfile
import os, errno # delete file and handle error
import urllib2 # download file
import datetime # date and time object
import csv
import sys
import psycopg2
import MySQLdb

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
	csvFile=bhavZipFile
	if os.path.exists(bhavZipFile):
		try:
			fileHandler = zipfile.ZipFile(bhavZipFile,'r')
			if fileHandler.testzip():
				raise zipfile.BadZipfile
			for files in fileHandler.namelist():
				csvFile=files
				fileHandler.extract(files)
			fileHandler.close()
		except(zipfile.LargeZipFile, zipfile.BadZipfile) as e: 
			print(e)
		finally:
			silentRemove(bhavZipFile)
	return csvFile

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


# csv2db
def insertFromCsv(filename):
	try:
		iFile = open (filename, 'rb')
		reader = csv.reader(iFile)

		conn = psycopg2.connect(
			host = '127.0.0.1',
			database = 'finance',
			user = 'userid',
			password = 'password'
		)
	
		cursor = conn.cursor()

		rownum = 0
		for row in reader:
			if rownum == 0:
				header = row
			else:
				try:
					cursor.execute( 'INSERT INTO "bse"."ScripTable" (sc_code, sc_name, sc_group, sc_type ) VALUES (%s,%s,%s,%s)',(row[0], row[1], row[2], row[3]) )
				except (InterfaceError, DatabaseError, DataError,IntegrityError,InternalError, ProgrammingError,NotSupportedError) as e:
					print e
					pass
				except ( OperationalError, psycopg2.extensions.QueryCanceledError, psycopg2.extensions.TransactionRollbackError ) as e:
					print e
					pass
				except (NotSupportedError) as e:
					print e
					pass
				
			rownum += 1

		conn.commit()
		cursor.close()
		conn.close()
		iFile.close()

	except csv.Error as e:
		print e
	return

## main
try:
	bhavHistory(5)
	csvFile = extractZip(getBhav(bhavDate()))
	insertFromCsv (csvFile)
	silentRemove(csvFile)
except KeyboardInterrupt ,e :
	print e

