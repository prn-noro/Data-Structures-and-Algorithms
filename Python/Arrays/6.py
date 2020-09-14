# Given a sorted array of positive integers. Your task is to rearrange  the array elements alternatively i.e first element should be max value, second should be min value, third should be second max, fourth should be second min and so on...
# https://practice.geeksforgeeks.org/problems/-rearrange-array-alternately/0/
# Using Extra Space

array=[10, 20 ,30 ,40, 50, 60, 70 ,80 ,90 ,100, 110]

new_array=[]
left=0
right=len(array)-1

while left<=right:

    if left==right:
        new_array.append(array[left])
        break

    new_array.append(array[right])
    new_array.append(array[left])
    left+=1
    right-=1

print(new_array)