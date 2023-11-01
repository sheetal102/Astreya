def find_intersection(arr1, arr2):
    intersection = []
    elements_in_arr1 = {}
    
    for num in arr1:
        elements_in_arr1[num] = elements_in_arr1.get(num, 0) + 1
    
    for num in arr2:
        if num in elements_in_arr1 and elements_in_arr1[num] > 0:
            intersection.append(num)
            elements_in_arr1[num] -= 1
    
    return intersection
t = int(input())
for _ in range(t):
    N = int(input())
    arr1 = list(map(int, input().split()))
    M = int(input())
    arr2 = list(map(int, input().split()))
    
    intersection = find_intersection(arr1, arr2)
    
    if intersection:
        print(" ".join(map(str, intersection)))
    else:
        print("Unset")
