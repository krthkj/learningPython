#!/usr/bin/python

import zipfile # read, test zipfile
import os, errno # delete file and handle error
import urllib2 # download file
import datetime # date and time object
import csv
import sys
import mysql.connector


## main
try:

	try:
		conn = mysql.connector.connect(
			user="sql427247",
			passwd="bS7%gL2%",
			host="sql4.freesqldatabase.com",
			database="sql427247"
		)
		cursor = conn.cursor()
		cursor.execute( 'drop table dailybhav')
		cursor.execute( 'drop table scriptable')

		cursor.execute( 'create table scriptable( sc_code bigint primary key, sc_name varchar(32) not null, sc_group varchar(4) not null, sc_type varchar(4) not null)')
		cursor.execute( 'create table dailybhav( bhav_date date not null, sc_code bigint not null, open real not null, high real not null, low real not null, close real not null, last real not null, prevclose real not null, no_trades bigint not null, no_of_shrs bigint not null, net_turnov bigint not null, tdcloindi varchar(8), primary key (sc_code,bhav_date) , FOREIGN KEY (sc_code) references scriptable (sc_code) ON UPDATE CASCADE ON DELETE CASCADE)')
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
		cursor.close()
		conn.close()

except KeyboardInterrupt ,e :
	print e

