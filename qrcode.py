import pyqrcode
import qrtools
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
#print("Enter Code")
#kid = raw_input()
#print("Entered Code is: "+kid)

def make_qr(kid):
	kqr = pyqrcode.create(kid)
	kqr.png(kid+".png",scale = 12.5)
	img = Image.open(kid+".png")
	img1 = Image.new("RGB", (295,295),(255,255,255))
	draw = ImageDraw.Draw(img1)
	font = ImageFont.truetype("verdana.ttf",10)
	draw.text((110,275),kid,(0,0,0),font=font)
	img1.save('sample-out.png')
	background = Image.open("sample-out.png")
	foreground = Image.open(kid+".png")
	background.paste(foreground,(0,0))
	background.save(kid+".png")


print "Enter Starting number"
start = input()
end = start+160
i = start
while i < end:
	kid = "KQ16"+str(i).zfill(4)
	make_qr(kid)
	i+=1
print i-1
print "DONE"
"""
img = Image.open(kid+".png")
img1 = Image.new("RGB", (295,295),(255,255,255))
draw = ImageDraw.Draw(img1)
font = ImageFont.truetype("verdana.ttf",10)
draw.text((110,275),kid,(0,0,0),font=font)
img1.save('sample-out.png')
background = Image.open("sample-out.png")
foreground = Image.open(kid+".png")
background.paste(foreground,(0,0))
background.save(kid+".png")
"""
"""
qr = qrtools.QR()
a = qr.decode(kid+".png")
print qr.data
if a == True:
	print "Yes"
else:
	print "No"

"""
