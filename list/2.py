def find_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
t = int(input())
for _ in range(t):
    N = int(input())
    arr = list(map(int, input().split()))
    duplicate = find_duplicate(arr)
    print(duplicate)
