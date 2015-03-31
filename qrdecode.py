import pyqrcode
import collections
import qrtools
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

qr = qrtools.QR()

img = Image.open("final.png")

kid = []

for i in range(160):
	kid.append("KQ16"+str(i+1).zfill(4))
#print kid
kidIm = []
count = 0
for i in range(10):
	for j in range(16):
		box = (i*350,j*302,(i+1)*350,(j+1)*302)
		newImg = img.crop(box).save("hello.png")
		qr.decode("hello.png")
		if qr.data in kid:
			count+=1
			kidIm.append(qr.data)
		print qr.data+"\n"

print count

compare = lambda kid,kidIm: collections.Counter(kid) == collections.Counter(kidIm)



if(count == 160 and compare(kid,kidIm) is True):
	print "YES"
else:
	print "NO"


print "DONE"

