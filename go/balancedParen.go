package program



func BalancedBrackets(s string) bool {
	// Write your code here.
	bracketHash := make(map[rune]rune)
	bracketStack := make([]rune, 0)
	bracketHash['}'] = '{'
	bracketHash[')'] = '('
	bracketHash[']'] = '['
	for _,v := range s { 
		switch v {
			case '}':
			last := bracketStack[len(bracketStack)-1]
			bracketStack = bracketStack[0:len(bracketStack)-1]
			if val, ok := bracketHash[v]; ok {
				if last != val {
					return false
				}
			}
			case ')':
			last := bracketStack[len(bracketStack)-1]
			bracketStack = bracketStack[0:len(bracketStack)-1]
			if val, ok := bracketHash[v]; ok {
				if last != val {
					return false 
				}
			}
			case ']':
			last := bracketStack[len(bracketStack)-1]
			bracketStack = bracketStack[0:len(bracketStack)-1]
			if val, ok := bracketHash[v]; ok {
				if last != val {
					return false 
				}
			}
			default:
			bracketStack = append(bracketStack, v)	
		}
			
	}
	return len(bracketStack) == 0
}
