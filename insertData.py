#!/usr/bin/python

import psycopg2

try:
	db = psycopg2.connect(
		host = '127.0.0.1',
		database = 'finance',
		user = 'userid',
		password = 'password'
	)

	cursor = db.cursor()

	cursor.execute( 'INSERT INTO "bse"."ScripTable" (sc_code, sc_name, sc_group, sc_type ) VALUES (%s,%s,%s,%s)',(007, 'consert', 'a', 'av') )

	db.commit()
except (InterfaceError, DatabaseError, DataError,IntegrityError,InternalError, ProgrammingError,NotSupportedError) as e:
	print e
	pass
except ( OperationalError, psycopg2.extensions.QueryCanceledError, psycopg2.extensions.TransactionRollbackError ) as e:
	print e
	pass
except (NotSupportedError) as e:
	print e
	pass
