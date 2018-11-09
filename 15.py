def list_length(my_list):
	count = 0
	for i in my_list:
		count += 1
	return count

def main():

	my_list =  ['a', 'b', 1, 45 , 'asd', 45.2]
	print(my_list)
	print("\nlist length is :\t",list_length(my_list))


if __name__=="__main__":
main()