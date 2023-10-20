N = int(input("Enter the number: "))
num = 0
while N>=1:
    rev=N%10
    num=num*10+rev
    N =N/10
    
print(int(num))