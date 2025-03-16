def d_to_b(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary
deci_num=int(input("Enter a decimal number: "))
print("Binary representation:", d_to_b(deci_num))
