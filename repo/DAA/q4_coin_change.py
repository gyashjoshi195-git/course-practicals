"""Q4: Coin Change using Dynamic Programming.

(a) Minimum number of coins for an amount.
(b) Number of ways to make the amount.
Time: O(amount * number_of_coins)
"""


def min_coins(coins, amount):
    INF = float("inf")
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
    return dp[amount] if dp[amount] != INF else -1


def count_ways(coins, amount):
    dp = [1] + [0] * amount
    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(f"Coins: {coins}, Amount: {amount}")
    print("Minimum coins :", min_coins(coins, amount))   # 3 (5+5+1)
    print("Number of ways:", count_ways(coins, amount))  # 11
