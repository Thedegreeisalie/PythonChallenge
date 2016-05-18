from PIL import Image
import numpy
im = Image.open('0007.png', 'r')
l=[]
for i in range(0,100):
	for j in range(0,94):
		pix = im.getpixel((i,j))
		if pix[0] == pix[1] and pix[0] == pix[2]:
			s = pix[0]
			print s
			if int(s) <= 127 and int(s) > 1:
				l.append(chr(s))
m=[]
k=1
while k < len(l):
	m.append(str(l[k]))
	k+=8

print(m)
