def remove_substri(string, substring):
    return string.replace(substring, "")
input_stri = input("Enter a string: ")
substri = input("Enter substring to remove: ")
print("Updated string:", remove_substri(input_stri, substri))
