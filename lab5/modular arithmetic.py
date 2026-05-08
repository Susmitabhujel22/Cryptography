def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0
    
    gcd_value, x1, y1 = extended_euclid(b, a % b)
    
    # Standard Extended Euclidean Algorithm update
    x = y1
    y = x1 - (a // b) * y1
    return gcd_value, x, y

def multipicative_inverse(a, m):
    gcd_val, x, y = extended_euclid(a, m)
    if gcd_val != 1:
        return None  # Inverse only exists if gcd is 1
    else:
        # (x % m) ensures the result is positive
        return x % m

# --- Main Program ---
a = int(input("Enter a number (a): "))
m = int(input("Enter modulo (m): "))

# Additive Inverse
add_inverse = (m - (a % m)) % m
print("\nAdditive Inverse of", a, "under modulo", m, "is:", add_inverse)

# Check Coprimality
if gcd(a, m) == 1:
    print(a, "and", m, "are Relatively Prime.")
else:
    print(a, "and", m, "are NOT Relatively Prime.")

# Multiplicative Inverse
inverse = multipicative_inverse(a, m)

if inverse is None:
    print("Multiplicative Inverse does NOT exist.")
else:
    print("Multiplicative Inverse of", a, "under modulo", m, "is:", inverse)
