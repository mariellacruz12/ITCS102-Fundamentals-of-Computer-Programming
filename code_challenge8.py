n=4

for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("* ",end="")
    print()

for x in range(n-1,0,-1):
    for y in range(n,x,-1):
        print(end=" ")
    for y in range (0,x):
        print("* ",end="")
    print()