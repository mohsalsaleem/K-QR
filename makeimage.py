import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.new("RGB",(3508,4961),(255,255,255))
print "Enter starting number"
start = input()

k = start

#kid = "KQ16"+str(k).zfill(4)
#foreground = Image.open(kid+".png")
"""
kid = []
for i in range(16):
	kid.append([])
	for j in range(10):
		kid[i].append("KQ16"+str(i*10+j+k).zfill(4)+".png") 
print kid
"""
count = 0
for i in range(10):
	for j in range(16):
		img.paste(Image.open("KQ16"+str(j*10+i+k).zfill(4)+".png"),(i*350,j*302))
		#print "KQ16"+str(i*10+j+k).zfill(4)+".png"
img.save("final.png")
