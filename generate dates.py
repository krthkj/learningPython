#!/usr/bin/python
import datetime
myDay = datetime.datetime.today()
myDay.strftime("%d%m%y")

import datetime
noOfDays=10
today = datetime.datetime.today()
itr=1
while itr != noOfDays:
	val = (today - datetime.timedelta(days=itr)).strftime("%d%m%y")
	print val
	itr += 1


