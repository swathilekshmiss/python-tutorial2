def replace(string):
    if ' ' in string:
        return string.replace(' ', '*')
    else:
        return f"${string}$"
input_stri = input("Enter a string: ")
print("Updated string:", replace(input_stri))
