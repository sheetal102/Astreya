def find_rotation_index(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return i + 1

t = int(input("Enter number of test cases: "))

for _ in range(t):
    N = int(input())
    arr = list(map(int, input().split()))

    rotation_index = find_rotation_index(arr)

    print(rotation_index)
