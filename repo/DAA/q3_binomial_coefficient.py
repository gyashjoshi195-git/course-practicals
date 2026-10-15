"""Q3: Binomial coefficient C(n, k) using Dynamic Programming.

C(n, k) = C(n-1, k-1) + C(n-1, k),  C(n, 0) = C(n, n) = 1
Time: O(n*k)   Space: O(n*k)
"""


def binomial(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp[n][k], dp


if __name__ == "__main__":
    n = int(input("Enter n: "))
    k = int(input("Enter k: "))
    value, table = binomial(n, k)
    print(f"C({n}, {k}) = {value}")
    print("\nDP table:")
    for row in table:
        print(row)
