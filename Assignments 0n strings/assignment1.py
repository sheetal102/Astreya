n = input("Enter the string: ")
i = 0
j = 1
element = n[i]

while j < len(n):
    if n[i] != n[j]:
        element += n[j]
    i = j
    j += 1

print(element)

