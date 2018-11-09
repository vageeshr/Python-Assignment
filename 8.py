
def main():
	fruit_veggies_list = list()

	fruits = tuple(("apple", "banana", "cherry"))
	veggies = tuple(("chilly", "capcium", "carrot"))

	fruit_veggies_list.append(fruits)
	fruit_veggies_list.append(veggies)

	print(fruit_veggies_list)

	print("\n-----Veggies-----\n")
	for veggie in fruit_veggies_list[1]:
		print(veggie)

	print("\n-----Fruits-----\n")
	for fruit in fruit_veggies_list[0]:
		print(fruit)


if __name__=="__main__":
	main()