n=int(input("Enter the number: "))
i=1
for i in range(n + n - 1):
    size=i
    if i >= n:
        size = n + n - i - 2
    
    for j in range(size + size):
        if j < size:
            print(" ",end="")
        else:
            print("*",end="")
    print()