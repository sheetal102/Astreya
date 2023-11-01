n=int(input("Enter the number: "))
sum=0
z=str(n)
x=len(z)
for char in z:
      y=int(char)
      sum+=y**x
      
if sum==n:
      print("Armstrong number")
else: 
      print("Not an Armstrong number")