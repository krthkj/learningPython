#!/usr/bin/python
import sys

def read_int ():
	try:
		value = int(raw_input())
	except ValueError:
		value = ''
	return value

count = read_int()
for i in range (0 , count):
#	print (i+1)
	line=sys.stdin.readline()
	line=map(int, line.split())
	print (  i+1 ':' + line)
	
