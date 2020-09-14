# How do you find the largest and smallest number in an unsorted integer array?

a=[1,3,5,5,4]
maxNum=a[0]
minNum=a[0]

# Sorting will take O(nlogn) time which is slower then O(n) so we do not use that.

for i in range(len(a)):

    maxNum=max(maxNum,a[i])
    minNum=min(minNum,a[i])

print(maxNum,minNum)