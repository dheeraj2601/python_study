'''a function receives four arguments. We want to make call to this function and we have a list of size 4 us
that has all arguments . If we simply pass list to the function, the call does not work.
use unpacking. '''

#unpack
def func(a,b,c,d):
	print (a, b, c, d)

#pack
def xyz(*args):
	sum=0
	for i in range(0, len(args)):
		sum+=args[i]
	return sum	

mylist = [2, 3, 4, 5]

if __name__ == "__main__" :
#unpack
	func(*mylist)

#pack
	print(xyz(10,20,30))
	print(xyz(15,12))
