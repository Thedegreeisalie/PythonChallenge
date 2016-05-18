from PIL import Image
import os
l=[]
i=0
im = Image.open('0007.png')
for y in range(0,95):
	for x in range(0,629):
		pix=im.getpixel((x,y))
		if pix[0] == pix[1] and pix[0] == pix[2]:
			l.append(chr(pix[0]))
s=''
j=0
while j < len(l):
	str1 = s.join(str(l[j]))
	j+=1
print str1

str1= ''.join(l)
print str1