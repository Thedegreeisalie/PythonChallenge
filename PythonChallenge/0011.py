from PIL import Image
im = Image.open('cave.jpg', 'r')
pixies = list(im.getdata())
dark = []
i=0
for i,j,k in (pixies):
	if k != 0:
		dark.append((i,j,k))