def push_zeros(arr):
    non_zero_index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
            non_zero_index += 1

t = int(input("Enter number of test cases: "))

for _ in range(t):
    N = int(input())
    arr = list(map(int, input().split()))

    push_zeros(arr)

    print(*arr)
