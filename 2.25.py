
def duplicates(lst):
    return list(set(lst))
n = int(input("Enter the number of elements: "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
print(f"\nList after removing duplicates: {duplicates(numbers)}")