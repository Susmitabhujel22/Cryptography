import math

def totient(n):
    count = 0
    for i in range(1, n):
        if math.gcd(n, i) == 1:
            count += 1
    return count


# Input
num = int(input("Enter a number: "))
print("Totient value:", totient(num))