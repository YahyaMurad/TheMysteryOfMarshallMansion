from DP import DP

def main():
    
    # Intialize the DP object
    dp = DP()

    # Initialize the items
    items = {
        12: "Corn Sack",
        5: "Hoe",
        10: "Oil Tank",
        16: "4 Tires"
    }

    # Initialize the weights
    weights = list(items.keys())

    # Run the function
    print("Dynamic Programming - Knapsack Approach\n")
    selection = dp.knapsack(weights, 30)
    total_weight = 0
    
    # Output the items
    for i in range(len(selection)):
        if i == len(selection) - 1:
            print(items[weights[selection[i] - 1]], end=" ")
        else:
            print(items[weights[selection[i] - 1]], end=", ")

        total_weight += weights[selection[i] - 1]

    print("(" + str(total_weight) + " kg - " + str(len(selection)) + " items)")



if __name__ == "__main__":
    main()