n = 5
for i in range(1, n + 1):
    spaces = " " * (n - i)
    chars = "".join(chr(ord('A') + j) for j in range(2 * i - 1))
    print(spaces + chars)
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    chars = "".join(chr(ord('A') + j) for j in range(2 * i - 1))
    print(spaces + chars)