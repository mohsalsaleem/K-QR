import pyqrcode
import qrtools

def check(kid):
	qr = qrtools.QR()
	a = qr.decode(kid+".png")
	print qr.data
	if a == True:
        	print "Yes"
	else:
        	print "No"
print "Enter the starting number"

start = input()

end = start+160
i = start
while i < end:
	kid = "KQ16"+str(i).zfill(4)
	check(kid)
	i+=1
print i-1
print "DONE"

