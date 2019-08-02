'''
You are given a positive integer N which represents the number of steps in a staircase. 
You can either climb 1 or 2 steps at a time. Write a function that returns the number 
of unique ways to climb the stairs
'''
# base case off the first step 
# take the base cases and sum up to achieve optimal 
class Solution:
    def staircase(self, n):
        steps = [0 for i in range(n)]
        steps[0] = 1
        steps[1] = 2
        for i in range(2, n):
            steps[i] = steps[i-2] + steps[i-1]
        return steps[n-1]


print(Solution().staircase(4) == 5)
# 5
print(Solution().staircase(5) == 8)
# 8

