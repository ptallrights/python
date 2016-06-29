#!/usr/bin/env python


staff_dic = {}
f = file('stu_info.txt')
for line in f.xreadlines():
	stu_id,stu_name,mail,company,title,phone = line.split()
	staff_dic[stu_id] = [stu_name,mail,company,title,phone]

while True:
	query = raw_input('\033[32;1mPlease input the query String,use "exit" to quit:\033[0m').strip()
	if len(query) < 3:
		print 'You have to input at lease 3 letters to query!'
		continue
	elif query == 'exit':
		break

	counter = 0
	for k,v in staff_dic.items():
		index = k.find(query)
		str_v = ' '.join(v)
		if index != -1:
			print k[:index] + '\33[31;1m%s\033[0m' % query + k[index + len(query):],str_v
			counter +=1
		else:
			str_v = ' '.join(v)
			index = str_v.find(query)
			if index != -1:
				print k,str_v[:index] + '\033[34;1m%s\033[0m' % query + str_v[index + len(query):]
				counter +=1

			#for i in v:
			#	if i.find(query) != -1:
			#		str_v = ' '.join(v)
			#		print k[:index] + '\033[34;1m%s\033[0m' % query + k[index + len(query):],str_v
			#		counter +=1
			#		break

	print 'Matched \033[31;1m%s\033[0m records!' % counter
