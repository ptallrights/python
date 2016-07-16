#!/usr/bin/env python
import os
ls = os.linesep

all = []
fname = raw_input('Enter filename:')
if os.path.exists(fname):
	print "%s already exists" % fname
	action = raw_input("Are you modify the file with read(r) or write(w)?")
	if action == 'r':
		try:
			forbi = open(fname,'r')
		except IOError,e:
			print "*** file open error:",e
		else:
			for eachLine in forbi:
				print eachLine,
			forbi.close()
	elif action == 'w':
		handle = raw_input("Would you to append(a) or reset(s)?")
		if handle == 'a':
			forbj = open(fname,'a')
			print "\nEnter lines ('.' by itself to quit).\n"
			while True:
				entry = raw_input('>')
				if entry == '.':
					break
				else:
					forbj.write(entry)
					forbj.write('\n')
			print 'DONE!'
		elif handle == 's':
			print "\nEnter lines ('.' by itself to quit).\n"
			while True:
				entry = raw_input('>')
				if entry == '.':
					break
				else:
					all.append(entry)
			
			fobk = open(fname,"w")
			fobk.writelines(['%s%s' % (x,ls) for x in all])
			fobk.close()
			print 'DONE!'
		else:
			print "Input error."
	else:
		print "No input content."
else:
	while True:
		entry = raw_input('>')
		if entry == ".":
			break
		else:
			all.append(entry)

	fobk = open(fname,"w")
	fobk.writelines(['%s%s' % (x,ls) for x in all])
	fobk.close()
	print 'DONE!'


#fname = raw_input('Enter filename:')
#while True:
#	if os.path.exists(fname):
#		print "Error: %s already exists" % fname
#	else:
#		break
#
#all = []
#print "\nEnter lines ('.' by itself to quit).\n"
#
#while True:
#	entry = raw_input('>')
#	if entry == ".":
#		break
#	else:
#		all.append(entry)
#
#fobi = open(fname,"w")
#fobi.writelines(['%s%s' % (x,ls) for x in all])
#fobi.close()
#print 'DONE!'
#
#fname = raw_input('Enter filename:')
#print
#
#try:
#	forj = open(fname,'r')
#except IOError,e:
#	print "*** file open error:",e
#else:
#	for eachLine in forj:
#		print eachLine,
#	fobj.close()
