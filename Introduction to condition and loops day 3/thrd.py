n=int(input("Enter the number: "))
x=n
num = 0
while n>=1:
    rev=n%10
    num=num*10+rev
    n =n//10

if num==x:
    print("True")
else:
    print("false")