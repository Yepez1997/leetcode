'''
Implement a class for a stack that supports all the regular functions (push, pop)
and an additional function of max() which returns the maximum element in the stack 
(return None if the stack is empty). Each method should run in constant time.
'''

''' Node class for stack ''' 
class Node:
    def __init__(self, val, maxVal):
        self.val = val 
        self.maxVal = maxVal


''' MaxStack API '''
class MaxStack:
    def __init__(self):
        self.stack = []
        self.globalMax = float('inf')
        self.size = 0
    
    ''' push - append value onto the stack '''
    def push(self, val):
        if len(self.stack) == 0:
            self.globalMax = val
            node = Node(val, val)
            self.stack.append(node)
        else:
            if val > self.globalMax:
                self.globalMax = val
            node = Node(val, self.globalMax)
            self.stack.append(node)
        self.size += 1

    ''' pop - pop top value off the stack ''' 
    def pop(self):
        if self.size == 0:
            raise "Stack is Empty"
        else:
            popped = self.stack.pop()
            self.globalMax = popped.maxVal
            return popped.val

    ''' max - get the max value on the stack ''' 
    def max(self):
        if self.globalMax == float('inf'):
            raise "No Value has been set"
        return self.stack[-1].maxVal

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
