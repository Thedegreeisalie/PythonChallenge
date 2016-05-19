#!/usr/bin/env python

import re


f = open("0003.txt", 'r').read()
u = re.findall(r"[a-z][A-Z][A-Z][A-Z][a-z][A-Z][A-Z][A-Z][a-z]", f, re.MULTILINE)
print (u)
c = ''.join(u) 
k = re.findall(r"[A-Z][a-z][A-Z]", c, re.MULTILINE)
t = ''.join(k)
print (t)
h = re.findall(r"[a-z]", t, re.MULTILINE)
print (h)
#fpbocihdsxwgqanltzevmjryku

