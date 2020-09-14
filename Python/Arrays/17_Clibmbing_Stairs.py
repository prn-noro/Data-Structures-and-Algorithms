# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps={0:1,1:1,2:2}
        
        for i in range(3,n+1):
            steps[i]=steps[i-1]+steps[i-2]
            
        return (steps[n])
        