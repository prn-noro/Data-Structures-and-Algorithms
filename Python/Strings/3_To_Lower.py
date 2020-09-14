# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        stack=[ord(i) for i in str]
        
        for i in range(len(stack)):
            if stack[i]>=65 and stack[i]<=90:
                stack[i]+=32
        final=[chr(i) for i in stack]
        
        string="".join(final)
        
        return string
        