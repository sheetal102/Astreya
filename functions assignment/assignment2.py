def checkMember(n):
     a = 0
     b = 1
     while a < n:
       c = a + b
       a = b
       b = c
     if a == n:
       print(True)
     else:
       print(False)
n=int(input())
if(checkMember (n)):
    print("true")
else:
    print("false")