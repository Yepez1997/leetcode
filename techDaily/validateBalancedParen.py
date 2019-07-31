''' Imagine you are building a compiler. Before running any code, the compiler 
must check that the parentheses in the program are balanced. Every opening bracket must have 
a corresponding closing bracket. We can approximate this using strings. 
'''
class Solution:

    brackets = {}
    brackets[")"] = "("
    brackets["}"] = "{"
    brackets["]"] = "["

    def isValid(self, s):
        stack = []
        if len(s) == 0:
            return True
        for char in s:
            if char in self.brackets:
                if len(stack) <= 0:
                    return False 
                top = stack.pop()
                corresponding = self.brackets[char]
                if top != corresponding: return False 
            else:
                # add all opening brackets
                stack.append(char)
        # after iterating thourgh the entire string there is remaining closing 
        # brackets -> still nil 
        if len(stack) > 0:
            return False 
        return True
    
# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s) == False)

s = ""
# should return True
print(Solution().isValid(s) == True)

s = "([{}])()"
# should return True
print(Solution().isValid(s) == True)
