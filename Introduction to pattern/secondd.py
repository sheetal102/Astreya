n=int(input())
row=1;
while row<=n:
    col=1;
    while col<=row:
        if col==1 or col==row:
            print(row-1, end='')
        else:
            print('0', end='')
        col+=1 
    print()
    row+=1  

    