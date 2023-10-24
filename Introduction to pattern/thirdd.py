n=int(input())
row=1;
while row<=n:
    col=1;
    while col<=row:
        if col==1 or col==row:
            print('1', end='')
        else:
            print('2', end='')
        col+=1
    print()
    row+=1