#!/usr/bin/env python
#coding=utf-8

#import module
#module.test()

#import heat.docker			#目录下__init__.py里面没有__all__
#print heat.docker.docker()

#from heat import *			#heat目录下__init__里面内容是:__all__ = ['docker','nova']
#print docker.docker()
#print nova.nova()
#n = nova.Nova()
#print n.test()

#from heat.common import mod
#
#print mod.hello()
#h = mod.Hello()
#print h.test()

from heat.common import *

print mod.hello()
h = mod.Hello()
print h.test()

print nova.nova()
n = nova.Nova()
print n.test()
