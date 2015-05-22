#!/usr/bin/python

import urllib2
import os, errno # delete file and handle error
import math

# Download file
def wget(downloadUrl,fileName):
	output = open(fileName,'wb')
	try:
		output.write(urllib2.urlopen(downloadUrl).read())
		print downloadUrl +" download success" + fileName
	except (urllib2.URLError, urllib2.HTTPError,ValueError) as e:
		print(e)
		print fileName+" download failed"
	finally:
		output.close()
	return fileName


#try:
x1 = 49.4366280
y1 = -126.560370
x2 = 19.7768240
y2 =-69.4695810
#zn = 21.430272
zn = 21.95456
#zn=0.669696


xn = math.ceil(abs(x1-x2)/ zn) + 1
#xnr = abs(x1-x2)%zn
#print "xn=",  xn , ", xnr=" , xnr
print "xn=",  xn
#if ( xnr != 0 ):
#	xn += 1

yn = math.ceil(abs(y1-y2)/zn) +1
#ynr = abs(y1-y2)%zn
#print "yn=",yn, ", ynr=",ynr
print "yn=",yn
#if ( ynr != 0 ):
#	yn += 1

i = x1
for countx in range (0, int(xn)):
	j = y1
	for county in range (0, int(yn)):
		URL="https://maps.googleapis.com/maps/api/staticmap?center="+str(i)+","+str(j)+"&zoom=5&size=500x500&sensor=false"
		outFile="x"+str(countx)+"y"+str(county)+".png"
		wget(URL,outFile)
		j += zn
	i -= 10

print "download Done"
#except :
#	print "Something went wrong."

