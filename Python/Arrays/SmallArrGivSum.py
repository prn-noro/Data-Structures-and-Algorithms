# Given an array of integers and a number x, find the smallest subarray with sum greater than the given value.

a=[4,2,1,1,2,1,0]
target=7
widStart=0
currentSum=0
minSize=float('inf')
windStart=0
for i in range(len(a)):
    currentSum+=a[i]
    while currentSum>target:
        minSize=min(minSize,i-windStart+1)
        currentSum-=a[windStart]
        windStart+=1

print(minSize)