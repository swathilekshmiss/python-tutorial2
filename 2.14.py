import math
def nCr(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
n = int(input("Enter n: "))
r = int(input("Enter r: "))
print(f"{n}C{r} is {nCr(n, r)}")
