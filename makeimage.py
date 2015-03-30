import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.new("RGBA",(3508,4961),(0,0,0))
img.save("f.png")

img = Image.open('f.png')
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("img2.png", "PNG")

print "Enter starting number"
start = input()

k = start

background = Image.open("img2.png")
kid = "KQ16"+str(k).zfill(4)
foreground = Image.open(kid+".png")

for i in range(10):
	for j in range(16):
		background.paste(foreground,(i*302,j*302),foreground)


#background.paste(foreground,(0*300,2*300),foreground)
background.save("final.png")
