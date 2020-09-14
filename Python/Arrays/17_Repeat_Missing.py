# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# Also, there is a duplicate number, return that.

a=[1,3,5,5,4]

repeatedNum=sum(a)-sum(set(a))

# a.remove(repeatedNum)

N=max(a)

totalSum=(N*(N+1))//2

missingNum=totalSum-(sum(a)-repeatedNum)

print([repeatedNum,missingNum])