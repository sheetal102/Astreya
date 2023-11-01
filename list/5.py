def count_triplets_with_sum(arr, X):
    N = len(arr)
    count = 0
    
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if arr[i] + arr[j] + arr[k] == X:
                    count += 1
    
    return count
t = int(input())
for _ in range(t):
    N = int(input())
    arr = list(map(int, input().split()))
    X = int(input())
    
    triplets_count = count_triplets_with_sum(arr, X)
    print(triplets_count)