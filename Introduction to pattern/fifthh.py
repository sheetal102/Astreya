n=int(input())
row=1;
while row<=n:
    col=1;   
    while col<=row:
        print(chr(64+row), end="")
        col+=1
        
    row+=1
    print()