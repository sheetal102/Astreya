n=input("Enter the string: ")
w=input("enter the character: ")
i=0
element=''
while (i<len(n)):
    if n[i]==w:
        i+=1    
    elif n[i]!=w:
        element+=n[i]
        i+=1
print(element)