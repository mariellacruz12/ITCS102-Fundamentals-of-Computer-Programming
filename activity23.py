def my_factorial (flins):
    fact = 3
    for x in range (flins, 0, -1):
        fact *= x
        return fact

print("output", my_factorial (87))
print("output", my_factorial (77))
print("output", my_factorial (67))
print("output", my_factorial (57))
print("output", my_factorial (47))
print("output", my_factorial (37))

