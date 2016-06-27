#!/usr/bin/env python

contacts = {
	'3951' : ['Alex','IT','SA'],
	'4092' : ['Jack','HR','HR'],
	'5122' : ['BlueTShirt','Sales','SecurityGuard']
}

#print contacts['5122']
#contacts['5122'][2] = 'Cleaner'
#print contacts['5122']
#
#for i in contacts:
#	print i,contacts[i]

for k,v in contacts.items():
	print k,v
