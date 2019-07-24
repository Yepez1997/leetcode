def minNumberOfJumps(array):
    # Write your code here.
	jumps = [float("inf") for _ in range(len(array))]
	jumps[0] = 0
	for i in range(1, len(array)):
		for j in range(0,i):
			if array[j] + j >= i:
				jumps[i] = min(jumps[i], jumps[j] + 1)
	return jumps[-1]

