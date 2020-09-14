'''
Algorithm :
1)Sort the array 
2)Initialize Left=0, Right=1
3)While Right is less than len(array)
4)If right less than len(array)-1 and array[right]==array[right+1], right+=1
5)elif difference equals k, count, left,right +=1
6)elif difference less than k, right+=1
7)elif difference greater than k, left+=1

'''

array=[1,3,5,7,1,2,4,7]
k=2

array.sort()

count=0
left=0
right=1

while right<len(array):

    if right<len(array)-1 and array[right]==array[right+1]:
        right+=1

    elif array[right]-array[left]==k:
        count+=1
        left+=1
        right+=1
    elif array[right]-array[left]>k:
        left+=1
    else:
        right+=1

    right=max(right,left+1)

print(count)

