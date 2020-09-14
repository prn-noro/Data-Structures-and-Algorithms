# Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.
# https://practice.geeksforgeeks.org/problems/count-the-triplets/0

array=[ 1,5,3,2]
countTrip=0
array.sort()
n=len(array)
i=n-1

while i>=0:
    j=0
    k=i-1

    while j<k:
        if array[j]+array[k]==array[i]:
            countTrip+=1
            print(array[i],array[j],array[k])
            j+=1
            k-=1
            # break
        elif array[j]+array[k]<array[i]:
            j+=1
        else:
            k-=1
    i-=1
print(countTrip)