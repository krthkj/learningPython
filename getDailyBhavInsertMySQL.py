#!/usr/bin/python

import zipfile # read, test zipfile
import os, errno # delete file and handle error
import urllib2 # download file
import datetime # date and time object
import csv
import sys
import mysql.connector

storeData = datetime.datetime.today().strftime("%Y-%m-%d")

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

# csv2db
def insertFromCsv(filename):
	try:
		iFile = open (filename, 'rb')
		reader = csv.reader(iFile)

		conn = mysql.connector.connect(
			user="sql427247",
			passwd="bS7%gL2%",
			host="sql4.freesqldatabase.com",
			database="sql427247"
		)

		cursor = conn.cursor()

		rownum = 0
		for row in reader:
			if rownum == 10:
				break
			if rownum == 0:
				header = row
			else:
				try:
					cursor.execute( 'INSERT INTO scriptable (sc_code, sc_name, sc_group, sc_type ) VALUES (%s,%s,%s,%s)',(row[0], row[1], row[2], row[3]) )
				except mysql.connector.Error as err:
					print "Something went wrong: {}".format(err)
					pass
				except mysql.connector.Error as err:
					if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
						print("Something is wrong with your user name or password")
					elif err.errno == errorcode.ER_BAD_DB_ERROR:
						print("Database does not exists")
					else:
						print(err)
					pass
				else:
					conn.commit()
					print "scriptable row ", rownum , " success"
			
				try:
					print storeData
					cursor.execute( 'INSERT INTO dailybhav (bhav_date,sc_code,open,high,low,close,last,prevclose,no_trades,no_of_shrs,net_turnov,tdcloindi) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(storeData, row[0], row[4], row[5],row[6], row[7], row[8], row[9],row[10], row[11], row[12], row[13]) )
				except mysql.connector.Error as err:
					print "Something went wrong: {}".format(err)
					pass

				except mysql.connector.Error as err:
					if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
						print("Something is wrong with your user name or password")
					elif err.errno == errorcode.ER_BAD_DB_ERROR:
						print("Database does not exists")
					else:
						print(err)
					pass
				else:
					conn.commit()
					print "dailyBhav row ", rownum , " success"

			rownum += 1
		
		conn.commit()
		cursor.close()
		conn.close()
		iFile.close()

	except csv.Error as e:
		print e
	return


# Get History till date
# helps in setup of database
def bhavHistory(noOfDays):
	today = datetime.datetime.today()
	itr=1
	while itr != noOfDays:
		val = (today - datetime.timedelta(days=itr)).strftime("%d%m%y")
		storeData = (today - datetime.timedelta(days=itr)).strftime("%Y-%m-%d")
		print storeData
		csvFile = extractZip(getBhav (val))
		print csvFile , storeData
		insertFromCsv (csvFile)
		silentRemove(csvFile)
		itr += 1
	return


## main
try:
	bhavHistory(5)
#	csvFile = extractZip(getBhav(bhavDate()))
#	print (csvFile)
#	insertFromCsv (csvFile)
#	silentRemove(csvFile)
except KeyboardInterrupt ,e :
	print e
	

