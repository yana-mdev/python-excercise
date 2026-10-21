def recursive_array(numbers, index):
    if index == len(numbers) - 1:
        return numbers[index]

    return numbers[index] + recursive_array(numbers, index + 1)


nums = [int(x) for x in input().split()]
print(recursive_array(nums, 0))