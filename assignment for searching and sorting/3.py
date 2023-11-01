def find_second_largest(arr):
    arr.sort(reverse=True)  
    return arr[1] 
N = int(input("Enter: "))
arr = list(map(int, input().split()))

result = find_second_largest(arr)

print(result)