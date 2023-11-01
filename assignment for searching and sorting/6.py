def sumOfTwoArrays(arr1, n, arr2, m, output):
    i = n - 1
    j = m - 1
    carry = 0
    
    k = max(n, m) 
    
    while i >= 0 and j >= 0:
        sum = arr1[i] + arr2[j] + carry
        output[k] = sum % 10
        carry = sum // 10
        i -= 1
        j -= 1
        k -= 1
    
    while i >= 0:
        sum = arr1[i] + carry
        output[k] = sum % 10
        carry = sum // 10
        i -= 1
        k -= 1
    
    while j >= 0:
        sum = arr2[j] + carry
        output[k] = sum % 10
        carry = sum // 10
        j -= 1
        k -= 1
    
    output[0] = carry

t = int(input("Enter number of test cases: "))

for _ in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    m = int(input())
    arr2 = list(map(int, input().split()))

    output = [0] * (max(n, m) + 1)

    sumOfTwoArrays(arr1, n, arr2, m, output)

    print(*output)
