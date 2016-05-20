from PIL import Image
import numpy
im = Image.open('0007.png', 'r')
l=[]

for i in range(0,629):
	for j in range(0,95):
		pix = im.getpixel((i,j))
		if pix[0] == pix[1] and pix[0] == pix[2] and pix[0] >= 31 and pix[0]<=127:
			l.append(pix[0])
p = ''.join(chr(k) for k in l)
#it looks like it changes every 63 bits this splice thing works awesomely
p2 = p[::63]
print p2
m=[105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join(chr(n) for n in m))
#integrity