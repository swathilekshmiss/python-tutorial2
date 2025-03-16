import re
def password_validity(password):
    if (len(password) >= 6 and
        re.search("[a-z]", password) and
        re.search("[0-9]", password) and
        re.search("[A-Z]", password) and
        re.search("[$#@]", password)):
        return "Valid Password"
    else:
        return "Invalid Password"
password = input("Enter a password: ")
print(password_validity(password))
