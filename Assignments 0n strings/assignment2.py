n=input("Enter the string: ")
i=len(n)
x=n.split()
print(x)
answer=''
for word in x:
    y=word[::-1]
    answer+= y
    answer+=' '
print(answer)
# j= i-1


# reversed_string=''
# while j>=0:
#     x=n[j]
#     reversed_string+=x
#     j-=1
# print(reversed_string)