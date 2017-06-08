import re, pickle, urllib.request

banner= pickle.load(open("banner.p", "rb"))

listy = []
for line in banner:
	for element in line:
		i = 0
		while i < element[1]:
			listy.append(element[0])
			i += 1
	listy.append('\n')
print (''.join(map(str, listy)))
