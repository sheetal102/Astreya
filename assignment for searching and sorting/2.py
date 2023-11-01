def rotate_array(arr, D):
    n = len(arr)

    arr[:D] = arr[D:]+arr[:D]

t = int(input("Enter number of test cases: "))

for _ in range(t):
    N = int(input())
    arr = list(map(int, input().split()))
    D = int(input())

    rotate_array(arr, D)

    print(*arr)
