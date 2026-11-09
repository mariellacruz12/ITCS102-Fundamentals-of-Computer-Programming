n=7
r=4

for y in range(n):
    for x in range(r):
        if x+y==r-1 or (x==0 and y>=3):
            print('*', end=' ')
        elif (x==r-1 and y<=3) or (x+y==n-1 and y>=4):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
