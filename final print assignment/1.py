def print_pattern(N):
    for i in range(N):
        spaces = (N - i - 1) * ' '
        if i == 0:
            print(spaces + 'A')
        else:
            print(spaces + 'A' + (2*i - 1) * ' ' + 'B')

    for i in range(N-2, -1, -1):
        spaces = (N - i - 1) * ' '
        if i == 0:
            print(spaces + 'A')
        else:
            print(spaces + 'A' + (2*i - 1) * ' ' + 'B')
print_pattern(5)
