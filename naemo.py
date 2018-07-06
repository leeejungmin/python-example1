import random

cT=[[0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]]

for i in range(5):
    for j in range(5):
        cT[i][j]=random.randint(0,1)


def correct_show():
    print('*', end='  ')
    for i in range(5):
        for j in range(1):
            print(xr[i][j], end='  ')
    print()
    for i in range(5):
        print(xc[i],cT[i])

T=[[0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0],
   [0,0,0,0,0]]

while cT != T:
    print('*', end='  ')
    for i in range(5):
        for j in range(1):
            print(xr[i][j], end='  ')
    print()
    for i in range(5):
        print(xc[i],T[i])

    r=int(input('Take Row'))-1
    c=int(input('Take column'))-1
    a=int(input('which one? 0 or 1'))

    """
        if a != 0 or a != 1
            while a is 0 or 1:
                print('Do it right!!! 0 or 1')
                a=int(input())
    """

    T[r][c] = a
    
    if cT==T:
        print('*', end='  ')
        for i in range(5):
            for j in range(1):
                print(xr[i][j], end='  ')
        print()
        for i in range(5):
            print(xc[i],T[i])
            print('Well Done!!!')
