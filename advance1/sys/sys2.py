import sys

def main(a):
	print (len(sys.argv))
	print ('Arguments : ' , a)
	print ('Arguments : ' , a[2])

if __name__ == "__main__":
	main(sys.argv)
