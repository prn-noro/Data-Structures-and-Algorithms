# Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.
# No Window Size
array=[-2, -3, 4, -1, -2, 1, 5, -3]
array=[-13, -3, -25, -20, -3, -16, 4, -12, -5, -22, -15, -4, -7]

sumTillHere=0
maxSum=-10000000000000000

for i in range(len(array)):
    sumTillHere+=array[i]

    maxSum=max(maxSum,sumTillHere)

    if sumTillHere<0:
        sumTillHere=0
    
print(maxSum)