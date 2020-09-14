
# https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0
# Given an unsorted array arr[] of size N, rotate it by D elements (anticlockwise). (Left Rotate) 
testcases=int(input())

for i in range(testcases):
    noElements,shiftedBy=map(int,input().split())
    array=list(map(int,input().split()))
    currentShift=shiftedBy
    while currentShift!=0:
        temp=array[0]
        for i in range(len(array)-1):
            array[i]=array[i+1]
        array[len(array)-1]=temp
        currentShift-=1
    for i in array:
        print(i,end=" ")