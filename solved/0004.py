#!/usr/bin/env python
#program needs to parse the header and pull a number then parse the header from a website 
import urllib.request
import re
import string
URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
start = "8022"
strhtml = []
strhtml.append(urllib.request.urlopen(URL+start).read())
new = []
new.append(start)
middle = []
i = 1 
middle.append(re.findall(r'(nothing\sis\s\d*)', str(urllib.request.urlopen(URL+start).read()))[-1])
new.append(re.findall(r'(\d\d*)', str((middle[-1])))[-1])
print ("strhtml: " + str(strhtml))
print ("new:" + str(new))
print ("middle:" + str(middle))
while i <= 400:
	print(str(urllib.request.urlopen(URL+str(new[i])).read()))
	strhtml.append(str(urllib.request.urlopen(URL+str(new[i])).read()))
	# print("strhtml: " + str(strhtml[i]))
	middle.append(re.findall(r'(nothing\sis\s\d*)', str(strhtml[i])))
	# print ("middle: " + str(middle[-1]))
	new.append(re.findall(r'(\d\d*)', str(middle[-1]))[-1])
	# print ("new:" + str(new[-1]))
	# print(i)
	i+=1

print (new)
'''
i+=1
while 400 >= i >= 84:
	print(str(urllib.request.urlopen(URL+str(int(new[i-1])/2)).read()))
	strhtml.append(str(urllib.request.urlopen(URL+str(int(new[i-1])/2)).read()))
	print("strhtml: " + str(strhtml[i-1]))
	middle.append(re.findall(r'(nothing\sis\s\d*)', str(strhtml[i-1])))
	print ("middle: " + str(middle[-1]))
	new.append(re.findall(r'(\d\d*)', str(middle[-1]))[-1])
	print ("new:" + str(new[-1]))
	print(i)
	i+=1

'''
	
#start was 1234 but at 16044 it instructs to divide by two and continue.)
