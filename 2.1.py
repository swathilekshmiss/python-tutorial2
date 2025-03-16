def remove_vowels(string):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in string if char not in vowels])
input_string = input("Enter a string: ")
print("String without vowels:", remove_vowels(input_string))
