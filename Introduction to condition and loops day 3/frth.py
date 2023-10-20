n=int(input("Enter the number: "))
sum_even=0
sum_odd=0
while n>=1:
    num=n%10
    if num%2==0:
        sum_even=sum_even+num
    else:
        sum_odd=sum_odd+num
    n=n//10
     
print(sum_even, sum_odd)
        
