def knapsackProblem(items, capacity):
    # Write your code here.
	knapsack = [[0 for j in range(0, capacity+1)] for i in range(0, len(items)+1)]
	# iterate through all
	for i in range(1, len(items) + 1):
		currentValue = items[i-1][0]
		currentWeight = items[i-1][1]
		for c in range(0, capacity+1):
			if currentWeight > c:
				knapsack[i][c] = knapsack[i-1][c]
			else:
				knapsack[i][c] = max(knapsack[i-1][c], knapsack[i-1][c - currentWeight] + currentValue)

	return [knapsack[-1][-1], getKnapSackVals(knapsack, items)]


def getKnapSackVals(knapsack, items):
	sequence = []
	i = len(knapsack)-1
	c = len(knapsack[0])-1
	while i > 0:
		if knapsack[i][c] == knapsack[i-1][c]:
			i -= 1
		else:
			sequence.append(i-1)
			c -= items[i-1][1]
			i -= 1

		if c == 0:
			break

	return list(reversed(sequence))
