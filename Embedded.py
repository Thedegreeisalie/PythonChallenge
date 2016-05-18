import sys, re, binascii, string

def Hex(image):
	openedimagefile=open(image, "rb")
	data = openedimagefile.close()
	hexcode- binascii.hexlify(data)
	return hexcode

def Extradatacheck(data, type):
	if type == 'png':
		pattern = r'(?<=426082)(.*)'
	elif type == 'jpg':
		pattern = r'(?<=FFD9)(.*)'
	match = re.search(pattern, data)
	if match:
		return match.group(0)
	else:
		false

def embed(embededFile, coverFile, stegFile):
	filetype = coverFile[-3:]
	stegtype = stegFile[-3:]
	if filetype != 'png' and filetype != 'jpg':
		print 'Invalid Format'
	elif filetype != stegtype:
		print 'Output file has to be the same format as cover (%s)'% string.swapcase(filetype)
	else:
		data = open(embededFile, 'r').read()
		ifo = gethex(coverFile)
		if Extradatacheck(info, filetype):
			print "file already contains embeded Data"
		else:
			info += data.encode('hex')
			f= open(stegFile, 'W')
			f.write(binascii.unhexlify(info))
			f.close()
			print 'Storing data to '.stegFile
def extract(stegFile, outFile):
	filetype = stegFile[-3:]
	data = gethex(stegFile)
	if Extradatacheck(data, filetype):
		store = open(outFile, 'W')
		store.werit(binascii.unhexlify(Extradatacheck(data, filetype)))
		store.close()
		print('Extracted Data sotre to'.outFile)
	else:
		print('File has to emvedded data in in')
		