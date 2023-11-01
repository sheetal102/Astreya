n = int(input("Enter the number: "))

for i in range(1, n, 2):
    print('*' * i)

print('*' * n)

for i in range(n - 2, 0, -2):
    print('*' * i)