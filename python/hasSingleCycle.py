''' check if there is a single cycle  ''' 

def hasSingleCycle(array):
	numElementsSeen = 0
	currentIndex = 0
	while numElementsSeen < len(array):
		# we have a cycle
		if currentIndex == 0 and numElementsSeen > 0:
			return False
		numElementsSeen += 1
		currentIndex = getNextIndex(currentIndex, array)
	return currentIndex == 0

def getNextIndex(i, array):
	jump = array[i]
	nextIdx = (i + jump) % len(array)
	return nextIdx if nextIdx >= 0 else nextIdx + len(array)

