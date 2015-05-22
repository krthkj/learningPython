#!/usr/bin/python
import csv
import sys

try:
	filename = "data.csv"

	iFile = open (filename, 'rb')
	reader = csv.reader(iFile)

	rownum = 0
	for row in reader:
		if rownum == 0:
			header = row
		else:
			colnum = 0
			for col in row:
				print '%s : %s' % (header[colnum] , col)
				colnum += 1

		rownum += 1

	iFile.close()

except csv.Error as e:
	print e
	
