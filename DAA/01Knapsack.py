def knapSack(W, wt, val, n):
    # Create a 2D array to store the maximum value that can be attained with given weight constraints
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    
    # Fill the array using bottom-up dynamic programming
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:  # Base case: if no items or weight is 0
                K[i][w] = 0
            elif wt[i-1] <= w:  # If item weight is less than or equal to the current weight limit
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:  # If item weight exceeds the current weight limit, skip it
                K[i][w] = K[i-1][w]
    
    # Return the maximum value achievable with the full weight limit and all items considered
    return K[n][W]

# Test values
# val = [1, 4, 5, 7]
# wt = [1, 3, 4, 5]
# W = 7
# val = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50

val = []
wt = []


n = int(input("Number of inputs: "))

for i in range(n):
    val.append(int(input(f"Enter Value of item {i+1}: ")))
    wt.append(int(input(f"Enter Weight of item {i+1}: ")))

W = int(input("Enter Capacity of Knapsack"))

# Print the result
print(knapSack(W, wt, val, n))
