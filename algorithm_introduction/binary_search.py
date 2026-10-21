def binary_search(arr, targ):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_element = arr[mid]
        if mid_element == targ:
            return mid
        if mid_element < targ:
            left = mid + 1
        else:
            right = mid - 1

    return -1


numbers = [int(x) for x in input().split()]
target = int(input())

print(binary_search(numbers, target))