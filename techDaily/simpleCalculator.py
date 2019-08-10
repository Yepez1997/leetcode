'''
Build a simple calculator that supports addition and subtraction 
'''



# Time Complexity -> O(n)
# Space Complexity -> O(n)
class Solution:
    def simpleCalculator(self, expression):
        expression =  [i for i in expression]
        # get the result
        return self.eval(expression)[0]

    def eval(self, expression, index=0):
        result = 0 
        operation = '+'
        index = 0
        while index < len(expression):
            char = expression[index]
            if char.isdigit():
                if operation == '+':
                    result += int(char)
                else:
                    result -= int(char)
            elif char in ('+',"-"):
                operation = char
            elif char == "(":
                n, index = self.eval(expression, index + 1)
                if operation == '+':
                    result += n 
                else:
                    # we have a subtraction
                    result -= n
            elif char == ")":
                # done with the inside of the stack 
                return (result, index)
            index += 1
        # pass the index so the parent knows which function to go off of 
        return (result, index)



def main():
    expression = "-(3+(2-1))"
    solution = Solution().simpleCalculator(expression)
    print(solution == 4)
    return 0

main()

