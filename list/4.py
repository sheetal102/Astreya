def count_pairs_with_sum(arr, X):
    num_counts = {}
    count = 0
    
    for num in arr:
        complement = X - num
        if complement in num_counts:
            count += num_counts[complement]
        num_counts[num] = num_counts.get(num, 0) + 1
    
    return count
t = int(input())
for _ in range(t):
    N = int(input())
    arr = list(map(int, input().split()))
    X = int(input())
    
    pairs_count = count_pairs_with_sum(arr, X)
    print(pairs_count)