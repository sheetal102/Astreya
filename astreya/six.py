p=float(input("Enter the principal amount="))
t=float(input("Enter the timespan="))
r=float(input("Enter the rate="))
z=(1+r)/100
a= p*z*t
CI=a-p
print("Compound Interest=",CI)