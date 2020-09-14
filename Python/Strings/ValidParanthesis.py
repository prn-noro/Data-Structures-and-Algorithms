# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

"""
1.)Initialize Two Arrays, one closed and one open
2.)For character in string S, check if character in Open
3.)If yes, push to array
4.)If no, Check if len of array ! 0 and stack top element in closed at same index as that of open
4.a)If yes, pop that character from array

5.)Finally if length of array=0, return True
"""


        stack=[]
        opened=["(","[","{"]
        closed=[")","]","}"]
        
        for ch in s:
            if ch in opened:
                stack.append(ch)
            else:
                if len(stack)!=0 and stack[-1]==opened[closed.index(ch)]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0