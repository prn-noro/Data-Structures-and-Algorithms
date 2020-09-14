# Given an array of integers and a number x, find the smallest subarray with sum greater than the given value.
# Does not work for negative numbers
a=[5,1, 4, 2]
neededSum=6

windSize=99999
windStart=0
windSum=0

for i in range(len(a)):
    windSum+=a[i]

    while windSum>neededSum:
        windSize=min(windSize,i-windStart+1)
        windSum-=a[windStart]
        windStart+=1

if windSize==99999:
    print('Not Possible')
else:
    print(windSize)