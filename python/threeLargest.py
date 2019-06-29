def findThreeLargestNumbers(array):
    # Write your code here.
	threeLargest = [None, None, None]
	for num in array:
		updateThreeLargest(num, threeLargest)
	return threeLargest


def updateThreeLargest(num, three):
	if three[2] is None or num > three[2]:
		moveAndShift(num, 2, three)
	elif three[1] is None or num > three[1]:
		moveAndShift(num, 1, three)
	elif three[0] is None or num > three[0]:
		moveAndShift(num, 0, three)


def moveAndShift(num, index, array):
	for i in range(index + 1):
		if i == index:
			array[i] = num
		else:
			array[i] = array[i+1]
