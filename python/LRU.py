class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
		self.cache = {}
		self.currentSize = 0
		self.listOfMostRecent = DoublyLinkedList() # assume the implementation

	# insert the key value pairs to the linked list
	# 2 cases ->
		# when the key is not there
			# check if the key is full
			# if not just update the current size
		# when the key is there
			# replace the key
    def insertKeyValuePair(self, key, value):
		if key not in self.cache:
			if self.currentSize == self.maxSize:
				# call an evict method
				self.evictLeastRecentlyUsed()
			else:
				self.currentSize += 1
			self.cache[key] = DoublyLinkedListNode(key)
		else:
			# update the value of the node
			self.replaceValue(key, value)
		# update the node to the head of the linked list
		self.updateMostRecent(self.cache[key])


	# get the value from a key then update its value to the head
    def getValueFromKey(self, key):
		if key not in self.cache:
			return None
		self.updateMostRecentKey(key)
		return self.cache[key].value

	# get the most recently used key
    def getMostRecentKey(self):
		# the head should be the first element in the cache ie mru
		return self.listOfMostRecent.head.key

	# evicts the least frequently used element
	def evictLeastRecentlyUsed(self):
		# assume remove tail is implemented
		tailKey = self.listOfMostRecent.tail.key
		# remove the tail from the linked list
		self.listOfMostRecet.removeTail()
		# remove the tail from the cache
		del self.cache[tailKey]

	# should update the pointers -- heas accordingly
	def updateMostRecent(self, node):
		self.listOfMostRecent.setHead(node)

	def replaceValue(self, key, value):
		if key not in self.cache:
			raise Exception("Key provided is not in the cache")
		# recall that a each element in the hash table points to a linked list node
		self.cache[key].value = value












