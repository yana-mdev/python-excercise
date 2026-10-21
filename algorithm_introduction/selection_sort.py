def selection_sort(arr):
    for index in range(len(arr)):
        min_index = index
        for current_index in range(index + 1, len(arr)):
            if arr[min_index] > arr[current_index]:
                min_index = current_index
        arr[index], arr[min_index] = arr[min_index], arr[index]

    return arr



numbers = [int(i) for i in input().split()]
selection_sort(numbers)
print(*numbers)