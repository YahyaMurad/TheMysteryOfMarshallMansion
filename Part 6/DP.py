class DP:
    def __init__(self):
        pass

    def knapsack(self, items, max_weight):
        # Initialize the table
        n = len(items)
        table = [[0] * (max_weight + 1) for _ in range(n + 1)]

        # Fill the table
        for i in range(1, n + 1):
            weight_i = items[i - 1]
            for w in range(1, max_weight + 1):
                if weight_i <= w:
                    table[i][w] = max(table[i - 1][w], table[i - 1][w - weight_i] + 1)
                else:
                    table[i][w] = table[i - 1][w]

        # Find the selected items
        selected_items = []
        w = max_weight
        for i in range(n, 0, -1):
            if table[i][w] != table[i - 1][w]:
                selected_items.append(i)
                w -= items[i - 1]

        # Return the selected items
        return selected_items[::-1]