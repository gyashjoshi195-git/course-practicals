"""Q6: Knapsack using the Greedy approach (Fractional Knapsack).

Greedy choice: pick items in decreasing order of value/weight ratio.
Items may be taken fractionally, which makes greedy optimal.
(For 0/1 knapsack greedy is NOT guaranteed optimal - use DP.)
Time: O(n log n)
"""


def fractional_knapsack(items, capacity):
    # items: list of (name, value, weight)
    items = sorted(items, key=lambda it: it[1] / it[2], reverse=True)
    total_value = 0.0
    print(f"{'Item':<6}{'Value':<8}{'Weight':<8}{'Ratio':<8}Taken")
    for name, value, weight in items:
        if capacity == 0:
            break
        take = min(weight, capacity)
        fraction = take / weight
        total_value += value * fraction
        capacity -= take
        print(f"{name:<6}{value:<8}{weight:<8}{value / weight:<8.2f}{fraction:.2f}")
    return total_value


if __name__ == "__main__":
    items = [("A", 60, 10), ("B", 100, 20), ("C", 120, 30)]
    W = 50
    print("Capacity:", W)
    print("Maximum value:", fractional_knapsack(items, W))  # 240.0
