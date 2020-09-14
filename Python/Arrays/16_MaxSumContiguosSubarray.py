# Find the contiguous subarray within an array, A of length N which has the largest sum

# https://www.interviewbit.com/problems/max-sum-contiguous-subarray/


from sys import maxint
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        # Initialize Values
        maxSoFar= 0
        finalMax= -maxint-1
        
        # Iterate through the Loop
        for i in range(len(A)):
            
            # Adding values to Maximum So Far
            maxSoFar+=A[i]
            
            # Comparison of two values
            finalMax=max(finalMax,maxSoFar)
            
            # Helps in case of arrays containing on negative values.
            if maxSoFar<0:
                maxSoFar=0
            
        return finalMax