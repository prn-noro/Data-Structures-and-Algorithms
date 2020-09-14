# https://practice.geeksforgeeks.org/problems/max-sum-in-the-configuration/1


def rotateArray(array):

    temp=array[0]

    for i in range(1,len(array)):
        array[i-1]=array[i]

    array[len(array)-1]=temp

    return array


array=[8,3,1,2]
count=len(array)
maxSum=0
while count!=0:
    tempSum=0
    final=rotateArray(array)
    for i in range(len(final)):
        tempSum+=i*final[i]
    # print(tempSum)
    maxSum=max(maxSum,tempSum)
    count-=1

    print(maxSum)