number=int(input("Enter the number: "))
if number==1:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print(a+b)
elif number==2:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print(a-b)
elif number==3:
     a=int(input("Enter first number: "))
     b=int(input("Enter second number: "))
     print(a*b)
elif number==4:
     a=int(input("Enter first number: "))
     b=int(input("Enter second number: "))
     print(a/b)
elif number==5:
      a=int(input("Enter first number: "))
      b=int(input("Enter second number: "))
      print(a%b)
elif number==6:
     exit(1)
elif number>6:
     print("invalid operation")