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

#inputs

row=int(input("Enter number of rows: "))
column=int(input("Enter number of columns: "))  

for x in range (row):
    for y in range (column):
        if x==0 or x==row-1:
            print("*", end="")
        elif y==0 or y==column-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
