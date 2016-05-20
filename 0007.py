from PIL import Image
import os
l=[]
i=0
l.append(i)
im = Image.open('0007.png')
for y in range(0,95):
	for x in range(0,629):
		pix=im.getpixel((x,y))
		if pix[0] == pix[1] and pix[0] == pix[2] and pix[0] != l[-1] and pix[0] >= 31 and pix[0] <= 127:
			l.append(pix[0])
s=''
s = ''.join(chr(a) for a in l)
print (s)
# should output smartguy,youmadeit.thenextlevelis[105,10,16,101,103,14,105,16,121]
r = []
q = [105,10,16,101,103,14,105,16,121]
for t in q:
	r.append(chr(t))
	print t
print r
#i
#dleegsoidley

