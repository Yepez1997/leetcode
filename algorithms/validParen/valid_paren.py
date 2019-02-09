# Valid Parenthesis Problem 

def valid_paren(parens):
    stack = []
    parens = list(parens)
    for i in range(len(parens)):
        current = parens[i]
        if (current == '[' or current == '(' or current == '{'):
            stack.append(current)
        elif (current == "}"):
            if (stack.pop() != '{'):
                return False
        elif (current == ")"):
            if (stack.pop() != '('):
                return False
        elif (current != "["):
            if (stack.pop() != '['):
                return False
    return True   

def tests():
    assert(valid_paren("()") == True)
    print(1)
    assert(valid_paren("()[]{}") == True)
    print(2)
    assert(valid_paren("(]") == False)
    print(3)
    assert(valid_paren("([)]") == False)
    print(4)
    return 0

tests()