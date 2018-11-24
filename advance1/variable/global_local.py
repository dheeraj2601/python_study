a = 5
print ("a1 : ", a)

def fun():
	a = 10;
	print ("a2 : ", a)
# end parameter in print() - not printing in the next line . same line
	print ()
	print ("hello ", end= " ")
	print ("dk")
	print ("yes", "no", sep= ", ")
        

if __name__ == "__main__":
	print ("a4 : ", a)
	fun()
	print ("a3 : ", a)
