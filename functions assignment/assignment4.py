def is_armstrong_number(n):
    num_str = str(n)
    
    k = len(num_str)
    
    armstrong_sum = sum(int(digit)**k for digit in num_str)
    
    return armstrong_sum == n

n = int(input("Enter the  number: "))
result = is_armstrong_number(n)
print(result) 
