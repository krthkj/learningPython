import zipfile
import os, errno

my_zip = "bhav.zip"
if os.path.exists(my_zip) :
	try:
		myFile = zipfile.ZipFile(my_zip,'r')
		print ("file read")
		if myFile.testzip():
			raise zipfile.BadZipfile
		for files in myFile.namelist():
			print ("Extracting files",files)
			myFile.extract(files)
		myFile.close()
	except zipfile.LargeZipFile, e: 
		print ( e )
	except zipfile.BadZipfile , e:
		print ( e )

	try:
		os.remove(my_zip)
		print ("file removed")
	except OSError as e:
		if e.errno != errno.ENOENT:
			print ( e )

