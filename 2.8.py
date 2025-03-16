def replace_substr(string, old_substr, new_substr):
    return string.replace(old_substr, new_substr)
input_str=input("Enter a string: ")
old_substr=input("Enter the substring to replace: ")
new_substr = input("Enter the new substring: ")
print("Updated string:", replace_substr(input_str, old_substr, new_substr))
