#!/usr/bin/env python
import collections


f= open("0002.txt", 'r').read()
c= collections.Counter(f)	
print (c)
#-<equality>
