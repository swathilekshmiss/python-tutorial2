string = input("Enter a string: ")
wordremove = input("Enter words to remove, separated by spaces: ").split()
for word in wordremove:
    string = string.replace(word, "")
print("Updated string:", string)
