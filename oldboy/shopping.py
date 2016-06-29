#!/usr/bin/env python
import sys
salary = int(raw_input('please input your salary:'))

#print '------Shopping Menu------'
products = [
    ['Iphone',':',3000],
    ['MacPro',':',12000],
    ['MX4',':',2200],
    ['Mp3',':',100],
    ['Cigarate',':',32],
    ['Nike shoes',':',500],
    ['Water',':',5]
]

#create a shopping list
shopping_list = []

while True:
    if salary < 5:
        sys.exit("you don't have enough money,Goodbye!")
        
    for p in products:
        print products.index(p),p[0],p[1],p[2]
    choice = raw_input('\033[32;1mPlease choose sth to buy:\033[0m')
    if choice == 'quit':
        print 'You have bought below stuff:'
        for i in shopping_list:
            print '\t',i
        sys.exit('Goodbye!')
    if len(choice) == 0:continue
    if not choice.isdigit():continue

    choice = int(choice)
    if choice >= len(products):
        print '\033[31;1mCould not find this item\0333[0m'
        continue
    
    #print products[choice]
    pro = products[choice]

    if salary >= pro[2]:#means you can afford this
        salary = salary - pro[2]
        shopping_list.append(pro)
        print '\033[34;1mAdding %s to shopping list,you have %s left\033[0m' % (pro[0],salary)
    else:
        print '\033[32;1mThe price of %s is %s,yet your current balance is %s,so try another one!\033[0m' % (pro[0],pro[2],salary)
        
