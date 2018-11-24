with_meta = ['write','dk','hello']
without_meta = ['chat']

def func2(args):
	print args
	abc_with = ""
	abc_without = ""
	for ab in list(args):
		if ab in with_meta:
			abc_with += ab+','
		else:
			abc_without += ab+','

	abc_with = abc_with[:-1]
	abc_without = abc_without[:-1]
	print abc_with
	print abc_without

if __name__ == "__main__":
	a = ['chat','write','hello','dk']
	func2(a)


	
