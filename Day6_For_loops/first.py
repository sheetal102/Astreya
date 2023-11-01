n=int(input("Enter the number: "))
for i in range(1,n+1):
    for k in range(1,n-i+2):
        if i %2!=0:
            print(1,end="")
        else:
            print(0,end="")
    print()