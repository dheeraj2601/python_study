def func(a,b,c):
	print (a, b, c, sep=" , ")

def func2(*args):
	args = list(args)
	args[0] = "dheeraj"
	args[1] = "kumar"
	func(*args)

if __name__ == "__main__":
	func2("dk1", "dk2", "dk3")


	
