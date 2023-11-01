def print_pattern():
    start_char = ord('A')
    for i in range(5):
        print(' ' * (4-i), end='')
        print(chr(start_char + i), end='')
        if i > 0:
            print(' ' * (2*i-1) + chr(start_char + i + 1), end='')
        print()

    for i in range(7):
        print(chr(start_char + i), end='')

print_pattern()
