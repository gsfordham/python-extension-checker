#! /bin/bin/env python

import magic, os, time

def main():
	#List files in current directory
	path = os.getcwd()
	#Set a counter for files and renames
	fcount = 0 #Count of all non-directory files
	rcount = 0 #Count of renamed files
	
	begin = False #Run program -- default: False
	out = "" #Default empty output message
	
	#Get user input
	uin = input("Currently in: '" + str(path) + "'.\nDo you wish to check for bad file extensions? [y/n]")
	
	if uin != "" and (uin.upper()[0]) == "Y":
		begin = True
		
	if begin:
		#Print entry message
		print("Please wait, this could take some time.")
		
		#Walk through files
		for filename in os.listdir(path):
			#Do NOT walk directories
			if os.path.isfile(filename):
				fcount += 1
				#Print regular updates, so the user has feedback
				if fcount % 50 == 0:
					print("Checked " + str(fcount) + " files so far...")
				fn, ext = (os.path.splitext(filename)) 
				'''
					Remove period from file extension, because
					magic does not have periods
				'''
				extf = ext.strip(".")
				
				#Take only the file type (ex: "png" from "image/png")
				ftype = ((magic.from_file(filename, mime=True)).split("/")[1])
				
				#Change file "jpeg" to "jpg"
				if ftype == "jpeg":
					ftype = "jpg"
					
				
				#If the file types do not match
				if extf != ftype:
					#Add back the period for the file type
					final_type = ("." + ftype)
					#Set the new name
					newname = (fn + final_type)
					while True:
						if not os.path.isfile(newname): #There are no file conflicts
							#Rename the file
							os.rename(filename, newname)
							#Increment rename counter
							rcount += 1
							break
						else: #There ARE file conflicts
							#Append datetime to filename prefix
							timestr = (time.strftime("%Y%b%d-%H%M%S", time.gmtime(time.time())))
							newname = (fn + timestr + final_type)
	
	#Make output message grammatically correct
	if rcount == 1:
		out = " file was renamed"
	else:
		out = " files were renamed"
		
	#Return count of renamed files
	return (str(rcount) + out + " out of " + str(fcount) + " total files.")

print(main())