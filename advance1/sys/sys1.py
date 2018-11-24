import sys


print()
sys.stderr.write("hello stderr")
sys.stderr.flush()
print()
sys.stdout.write("hello stdout")
print()

print (sys.argv[1])
print (sys.argv[2])

print (len(sys.argv))

if len(sys.argv) > 1:
	print (sys.argv[2])
	print (sys.argv[1])


def main(arg):
	print (arg)

main(sys.argv[1])
