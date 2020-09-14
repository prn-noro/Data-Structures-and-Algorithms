# Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.
# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0
# array=[1, 2, 3, 7, 5]
# array=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
testcases=int(input())
for i in range(testcases):
    n,getSum = map(int,input().split())
    array=list(map(int,input().split()))
    # getSum=15
    left=0
    right=left+1
    sumTillHere=array[0]
    status=False
    while right<=n:
        if getSum==sumTillHere:
            print(left,right-1)
            status=True
            break

        if sumTillHere<getSum:
            sumTillHere+=array[right]
            right+=1

        else:
            sumTillHere-=array[left]
            left+=1

if status==False:
    print(-1)
