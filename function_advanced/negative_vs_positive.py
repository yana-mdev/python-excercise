def sort_numbers(*args):
    negative_sum = 0
    positive_sum = 0
    for num in args:
        if num > 0:
            positive_sum += num
        else:
            negative_sum += num

    return negative_sum, positive_sum


nums = map(int, input().split())
neg_sum, pos_sum = sort_numbers(*nums)

print(neg_sum)
print(pos_sum)
if abs(neg_sum) > pos_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")