# https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays/0/
# Given two sorted arrays arr1[] and arr2[] in non-decreasing order with size n and m. The task is to merge the two sorted arrays into one sorted array (in non-decreasing order).
# Using Extra Space
arr1=[1, 5, 9, 10, 15, 20]
arr2=[2,3,8,13]

new_arr=[0]*(len(arr1)+len(arr2))

ptr1=0
ptr2=0
i=0
while ptr1<len(arr1) and ptr2<len(arr2):

    if arr1[ptr1]<=arr2[ptr2]:
        new_arr[i]=arr1[ptr1]
        i+=1
        ptr1+=1
    else:
        new_arr[i]=arr2[ptr2]
        i+=1
        ptr2+=1
    print(new_arr)


if ptr1<len(arr1):
    while ptr1<len(arr1):
        new_arr[i]=arr1[ptr1]
        ptr1+=1
        i+=1

if ptr2<len(arr2):
    while ptr2<len(arr2):
        new_arr[i]=arr2[ptr2]
        ptr2+=1
        i+=1

print(new_arr)