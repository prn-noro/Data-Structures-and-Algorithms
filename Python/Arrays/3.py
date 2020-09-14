# Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
# https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0

# from sys import maxint
array=[-2, -3, 4, -1, -2, 1, 5, -3]
# array=[-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
# array=[-1 ,-2 ,-3, -4]

globalMaximum=-100
maxSoFar=0

for i in range(len(array)):
    maxSoFar+=array[i]
    globalMaximum=max(globalMaximum,maxSoFar)
    if maxSoFar<0:
        maxSoFar=0

print(globalMaximum)

