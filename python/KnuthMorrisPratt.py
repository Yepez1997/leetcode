def knuthMorrisPrattAlgorithm(string, substring):
    # Write your code here.
	pattern = getPattern(substring)
	return knp(string, substring, pattern)


def knp(string, substring, pattern):
	j = 0
	i = 0
	while i + len(substring) - j <= len(string):
		if string[i] == substring[j]:
			if j == len(substring) -1:
				return True
			i += 1
			j += 1
		elif j > 0:
			j = pattern[j-1] + 1
		else:
			i += 1
	return False

def getPattern(substring):
	pattern = [-1 for _ in substring]
	j = 0
	i = 1
	while i < len(substring):
		if substring[i] == substring[j]:
			pattern[i] = j
			i += 1
			j += 1
		elif j > 0:
			j = pattern[j-1] + 1 # the previously indexed item + 1
		else:
			i += 1
	return pattern
