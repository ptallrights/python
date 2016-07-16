#!/usr/bin/python
#if
x = int(raw_input("please input x:"))
if x > 0:
	print '"x" must be atleaast 0!'
else:
	print '"x" is fushu'

print "I like to use the Internet for:"
for item in ['e-mail','net-surfing','homework','chat']:
	print item
who = 'knights'
what = 'Ni!'

print 'We are the',who,'who say',what,what,what
print 'We are the %s who say %s' % (who,((what + ' ')*4))
for NUM in [1,2,3,4,5,6]:
	print NUM
