def find_unique(arr):
    unique_element = 0
    for num in arr:
        unique_element ^= num
    return unique_element
t = int(input())
for _ in range(t):
    N = int(input())
    arr = list(map(int, input().split()))
    unique = find_unique(arr)
    print(unique)