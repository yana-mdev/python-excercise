def sum_of_coins(coins, target):
    coins.sort(reverse=True)
    used_coins = {}

    index = 0
    while target != 0 and index < len(coins):
        coins_count = target // coins[index]
        target %= coins[index]

        if coins_count > 0:
            used_coins[coins[index]] = coins_count
        index += 1

    if target != 0:
        return "Error"

    result = f"Number of coins to take: {sum(used_coins.values())}\n"
    for value, count in used_coins.items():
        result += f"{count} coin(s) with value {value}\n"
    return result.strip()


coins = [int(x) for x in input().split(", ")]
target_sum = int(input())

print(sum_of_coins(coins, target_sum))
