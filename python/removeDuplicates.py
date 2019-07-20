class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for letter in S:
          if stack and letter == stack[-1]:
            stack.pop()
          else:
            stack.append(letter)
        return "".join(stack)

