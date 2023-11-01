import random

n=int(input("Enter the number: "))
num= random.randint(1,100)
if n==num:
    print("The guess is correct")
elif n>=num:
    print("The guess is too high")
elif n<=num:
    print("The guess is too low")
