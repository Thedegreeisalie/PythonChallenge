import re, os, zipfile
start= '90052'
dirname = "channel"
#define some list thig
somelistthing = []
nothings = []
nothings.append(start)
#ch
os.chdir(dirname)
#prime the loop
somelistthing.append(open(start + ".txt", 'r').read())
#loopdeloop
for i in range(0,908):
	newnothing = re.findall('\d\d*', somelistthing[-1])[-1]
	nothings.append(newnothing) 
	somelistthing.append(open(nothings[-1] + '.txt', 'r').read())
print (somelistthing)
# it appears that unzipping the dir in the first place was a bad move. now do the same thing while the folder is zippe

#define some list thig
zsomelistthing = []
znothings = []
zcomments = []
znothings.append(start)
#prime the loop
zf = zipfile.ZipFile("channel.zip", 'r')
print (zf.read(start + ".txt", 'r'))

zsomelistthing.append(zf.read(start + ".txt", 'r'))
#loopdeloop
for i in range(0,908):
	znewnothing = re.findall('\d\d*', zsomelistthing[-1])[-1]
	znothings.append(znewnothing) 
	zsomelistthing.append(zf.read(znothings[-1] + '.txt', 'r'))
	info = zf.getinfo(znothings[-1] + '.txt')
	zcomments.append(info.comment)
print (zcomments)
# it appears that unzipping the dir in the first place was a bad move. now do the same thing while the folder is zippe
print (''.join(zcomments))
