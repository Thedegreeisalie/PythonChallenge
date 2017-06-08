#pythonchallenge.com/pc/return/good asks for a password it is related to the following two strings pw and un

un= 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw= 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

#BZh91AY&SY is somehow related to the bz2 package but it can't handle the excaped characters.
import bz2

print( bz2.decompress(un.encode('latin1')))
print( bz2.decompress(pw.encode('latin1')))

#huge

#file