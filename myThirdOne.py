#!/usr/bin/python

'myFirstOne.py -- create text file'
import os
ls = os.linesep
all = []
fname = raw_input("please input a filename:")
#get filename
#while True:
if os.path.exists(fname):
	print "ERROR: '%s' already exists" % fname
	try:
	    fobj = open(fname,'r')
	except IOError,e:
	    print "*** file open error:",e
	else:
    	#display contents to the screen
		for eachLine in fobj:
			print eachLine,
		fobj.close()
else:
	print "\nEnter lines ('.' by itself to quit).\n"
	while True:	
		entry = raw_input('>')
		if entry == ".":
			break
		else:
			all.append(entry)
	

fobj = open(fname,"w")
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print "DONE!"

#get file content (txt) lines

#all = []
#print "\nEnter lines ('.' by itself to quit).\n"

#loop until user terminates input
#while True:
#	entry = raw_input('>')
#	if entry == ".":
#		break
#	else:
#		all.append(entry)

#wirte lines to file with prper line-ending

#attempt to open file for reading 
#try:
#    fobj = open(fname,'r')
#except IOError,e:
#    print "*** file open error:",e
#else:
#    #display contents to the screen
#    for eachLine in fobj:
#        print eachLine,
#    fobj.close()
#
