import sys

def main(argv):

	if(len(argv) >= 3):
		try:
			print("Sum is ", (int(argv[0]) + int(argv[1]) + int(argv [2])))
		except:
			print("Usage: file.py <integer> <integer> <integer>")

	else:
		print("Usage: file.py <integer> <integer> <integer>")

	return

if __name__=="__main__":
	#exclude file name from args
main(sys.argv[1:])