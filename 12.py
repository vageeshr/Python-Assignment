def main():

	#lambda expressions
	circle = lambda radius : (3.141592653589793) * radius * radius
	square = lambda side :  side * side
	triangle = lambda height, base : ((height * base)/2)


	print("\n1 - Area of Circle\n")
	print("2 - Area of Triangle\n")
	print("3 - Area of Square\n")
	print("4 - Quit\n")

	while True:

		try:
			choice = int(input("\nEnter your choice:\t"))
		except Exception as e:
			print("\nPlease enter valid integer\n")
			continue

		if choice == 1:

			try:
				radius = float(input("\nEnter radius of the Circle:\t"))
				print("\nArea is : ", circle(radius))

			except Exception as e:
				print(str(e))
				print("\nPlease enter valid radius value\n")
				continue


		if choice == 2:

			try:
				base = float(input("\nEnter base of the Triangle:\t"))
				height = float(input("\nEnter height of the Triangle:\t"))
				print("\nArea is : ", triangle(height, base))

			except Exception as e:
				print("\nPlease enter valid integers\n")
				continue


		if choice == 3:

			try:
				side = float(input("\nEnter a side of the Square:\t"))
				print("\nArea is : ", square(side))

			except Exception as e:
				print("\nPlease enter valid integer\n")
				continue
			

		if choice == 4:

			print("Bye\n")
			break

		if (choice <1) or (choice > 4):
			print("\n Invalid Choice \n")



if __name__ == "__main__":
	main()