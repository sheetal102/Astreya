n=input("Enter the string: ")
length=len(n)
dic={}
ans=''
count=0
for i in range(length):
    if n[i] in dic:
        dic[n[i]] += 1
    else:
        dic[n[i]] = 1

    if count<dic[n[i]]:
        ans=n[i]
        count=dic[n[i]]
print("max occuring char is:  ", ans)