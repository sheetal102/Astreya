n = 5
for i in range(1, n + 1):
    spaces = " " * (n - i)
    numbers = "".join(str(j) for j in range(1, 2 * i))
    print(spaces + numbers)

for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    numbers = "".join(str(j) for j in range(1, 2 * i))
    print(spaces + numbers)