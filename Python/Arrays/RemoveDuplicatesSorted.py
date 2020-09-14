# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.


array=[1,1,1,2,2,2,3,3,3,3,4,4,4,4]

left=0
currentElement=array[0]
for i in range(1,len(array)):
    if array[i] !=currentElement:
        left+=1
        array[left]=array[i]
        currentElement=array[left]
array=array[0:left+1]
print(array)