# Given an integer n, return any array containing n unique integers such that they add up to 0.

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        final=[]
        if n%2==0:
            left=n//2
            for i in range(1,left+1):
                x=i
                y=-x
                final.append(x)
                final.append(y)
        else:
            left=n//2
            for i in range(1,left+1):
                x=i
                y=-x
                final.append(x)
                final.append(y)
            final.append(0)
        return final
        