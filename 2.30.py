numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
unique_numbers = list(dict.fromkeys(numbers))
print("List with unique elements:", unique_numbers)
