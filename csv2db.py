#!/usr/bin/python
import csv
import sys
import psycopg2

try:
	filename = "data.csv"

	iFile = open (filename, 'rb')
	reader = csv.reader(iFile)

	conn = psycopg2.connect(
		host = '127.0.0.1',
		database = 'finance',
		user = 'userid',
		password = 'Password'
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

