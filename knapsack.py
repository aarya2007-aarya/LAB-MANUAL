def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    values[i - 1] + dp[i - 1][w - weights[i - 1]]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def knapsack_top_down(weights, values, capacity, n, memo):

    if n == 0 or capacity == 0:
        return 0

    if (n, capacity) in memo:
        return memo[(n, capacity)]

    if weights[n - 1] > capacity:
        memo[(n, capacity)] = knapsack_top_down(
            weights, values, capacity, n - 1, memo
        )
    else:
        take = values[n - 1] + knapsack_top_down(
            weights, values,
            capacity - weights[n - 1],
            n - 1, memo
        )

        dont_take = knapsack_top_down(
            weights, values,
            capacity, n - 1, memo
        )

        memo[(n, capacity)] = max(take, dont_take)

    return memo[(n, capacity)]


# Taking input from the user
n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):
    weight = int(input(f"Enter weight of item {i + 1}: "))
    value = int(input(f"Enter value of item {i + 1}: "))

    weights.append(weight)
    values.append(value)

capacity = int(input("Enter maximum weight capacity: "))


# Bottom-Up
print("\nUsing Bottom-Up:")
print("Maximum value:",
      knapsack_bottom_up(weights, values, capacity))


# Top-Down
print("\nUsing Top-Down:")
memo = {}

print("Maximum value:",
      knapsack_top_down(weights, values, capacity, n, memo))