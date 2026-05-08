import math

def totient(n):
    count = 0
    for i in range(1, n):
        if math.gcd(n, i) == 1:
            count += 1
    return count

def is_primitive_root(g, n):
    required_set = set()
    phi = totient(n)

    for i in range(1, phi + 1):
        required_set.add(pow(g, i, n))

    return len(required_set) == phi


def primitive_roots(n):
    roots = []
    for g in range(2, n):
        if math.gcd(g, n) == 1 and is_primitive_root(g, n):
            roots.append(g)
    return roots


# Input
num = int(input("Enter a number: "))
roots = primitive_roots(num)

if roots:
    print("Primitive roots:", roots)
else:
    print("No primitive roots found")