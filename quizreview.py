#target 3

for x in range (7):
    for y in range (14):
        if x==0 or x==6:
            print("*", end="")
        elif y==13 or y==0:
            print("*", end="")
        else:
            print(" ", end="")
    print()