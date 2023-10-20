n=int(input("Enter the number: "))
i=1;j=1;k=0;f_no=0
while i<n:
    f_no=j+k
    j=k
    k=f_no
    i=i+1
print(f_no)