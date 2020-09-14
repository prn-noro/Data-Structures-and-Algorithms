# Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y coordinate of ith point respectively.
# Return an Integer, i.e minimum number of steps.

# https://www.interviewbit.com/problems/min-steps-in-infinite-grid/

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        # Initital Values
        prevX=A[0]
        prevY=B[0]
        totalSteps=0
        for i in range(1,len(A)):
            # Current Coordinates
            currentX=A[i]
            currentY=B[i]
            
            # Calculate Difference (Absolute)
            dx=abs(currentX-prevX)
            dy=abs(currentY-prevY)
            
            # Adding Max of difference to Total
            totalSteps+=max(dx,dy)
            
            # Update initial X 
            prevX=currentX
            prevY=currentY

        return totalSteps            
            
            
            
