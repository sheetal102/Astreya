N = int(input("enter the value: "))

for i in range(N):
    for j in range(N):
        if i % 2 == 0:
            print(i*N + j + 1, end='  ')
        else:
            print((i+1)*N - j, end='  ')
    print()

