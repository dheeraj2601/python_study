
#Byte objects are sequence of Bytes, whereas Strings are sequence of characters.
#Byte objects are in machine readable form internally, Strings are only in human readable form.
#    Since Byte objects are machine readable, they can be directly stored on the disk. Whereas, Strings need encoding before which they can be stored on disk.


a = "Dheeraj"
b = b"Dheeraj"

print (b);

#encoding : 
c = a.encode('ASCII')

if (b == c):
	print ("encoding success")
else:
	print ("encoding fail")


d = b.decode('ASCII')
if (d == a):
	print ("decoding success")
else:
	print ("decoding fail")


