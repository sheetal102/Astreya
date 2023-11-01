n=input('Enter the string: ')
i=0
while i<len(n) - 1 :
    count=1
    while n[i] == n[i+1]:
        i+=1
        count+=1
        if i+1 == len(n):
            break
    print(str(n[i]) + str(count),end=" ")
    i+=1

print()