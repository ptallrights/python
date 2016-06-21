#!/usr/bin/env python

#def odd():
#	n = 1
#	print "hello yield"
#	while True:
#		#print "before yield"
#		yield n
#		print "after yield"
#		n +=2

#for i in odd():
#	print i
#	if i >= 101:
#		break

#o = odd()
#print "======="
#print o.next()
#print o.next()
#print o.next()
#print o.next()

#for i in odd():
#	print i
#	if i >= 2:
#		break

#def test(arg):
#	print "test One"
#	for i in range(1,len(arg)):
#		yield i
#		#print i*2
#
#t=test('justallright')

#print t.next()
#print t.next()
#print t.next()
#print t.next()
#print t.next()
#
#if t.next() >= 3:
#	print 'ok'
#else:
#	print t.next()


#def gen():
#	value = 0
#	while True:
#		recv = yield value
#		if recv == 'e':
#			break
#		value = "gen:%s" % recv
#
#g = gen()
#
#print g.send(None) #g.next()
#print g.send('aaaa')
#print g.send('bbbb')
#print g.send('e')
#print g.send('cccc')
#print g.send('dddd')

def sgen():
	value = 0
	while True:	
		rec = yield value
		if rec == "quit":	
			value = 'please input "q" to quit'
		elif rec == "hello":
			#print "hello,nihao"
			value = "hello,@you"
		else:
			value = "what are you say?"
			#print "what are you say?"
s = sgen()
s.send(None)
while True:
	TEXT = raw_input("please input:")
	if TEXT == "q":
		break
	print s.send(TEXT)
		
