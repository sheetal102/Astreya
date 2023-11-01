N =int(input("enter the number: "))

for i in range(2*N-1):
    for j in range(2*N-1):
        print(N - min(i, j, 2*N-2-i, 2*N-2-j), end='')
    print()

