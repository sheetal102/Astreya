from sys import stdin

def sort_0_1(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        while arr[left] == 0 and left < right:
            left += 1
        while arr[right] == 1 and left < right:
            right -= 1

        if left < right:
            arr[left] = 0
            arr[right] = 1
            left += 1
            right -= 1

def takeInput():
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

def printList(arr, n):
    for i in range(n):
        print(arr[i], end=' ')
    print()

t = int(stdin.readline().strip())
while t > 0:
    arr, n = takeInput()
    sort_0_1(arr)  
    printList(arr, n)
    print()
    t -= 1