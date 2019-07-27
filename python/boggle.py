# assuming trie implementation
# trie has add method and also .root and end word
def boggleBoard(board, words):
    # Write your code here.
	trie = Trie()
	finalWords = {}
	for word in words:
		trie.add(word)
	visited = [[False for letter in row] for row in board]
	for x in range(len(words)):
		for y in range(len(words[x]))
			letter = words[x][y]
			explore(x,y, words, trie.root, visited, finalWords)
	return list(finalWords.keys())

# assuming we have get neighbors
def explore(x, y, board, trie, visited, finalWords):
	if visited[x][y]:
		return
	letter = board[x][y]
	if letter not in trie:
		return
	visited[x][y] = True
	trieNode = trie[letter]
	if "*" in trieNode:
		finalWords[trieNode[*]] = True
	neighbors = getNeighbors(x, y, board) # assume implementation to get all valid directional vectors
	for neighbor in neighbors:
		explore(neighbor[0], neighbor[1], board, trieNode, visited, finalWords)
	visited[x][y] = False

