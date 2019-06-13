package program

type SuffixTrie map[byte]SuffixTrie

func NewSuffixTree() SuffixTrie {
	trie := SuffixTrie{}
	return trie
}


// runtime o(n^2), suffix trie goes through all suffixes of a string 
func (trie SuffixTrie) populateSuffixTrieFrom(str string) {
	for i := range str {
		root := trie 
		for j := i; j < len(str); j++ {
			letter := str[j]
			// if the root is not found, create a new suffix trie node
			if _, found := root[letter]; !found {
				root[letter] = NewSuffixTree()
			}
			// keep pointing to the next letter in the trie
			root = root[letter]
		}
		root['*'] = nil 
	}
}

// runtime o(n), checks if the string is contained in the trie 
func (trie SuffixTrie) contains(str string) bool {
	// want to traverse all over the root 
	root := trie 
	for i := 0; i < len(str); i++ {
		letter := str[i]
		if _, found := root[letter]; !found {
			return false 
		}
		// keep pointing to the next letter in the tree - if found 
		root = root[letter]
	}
	
	// if we found the end 
	_, found := root['*']
	return found
}
