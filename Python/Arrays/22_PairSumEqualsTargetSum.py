# How do you find all pairs of an integer array whose sum is equal to a given number

array=[-1,1,2,3,4,5,6,7,8,9]
targetSum=8

complementDict={}
finalArray=[]

for i in range(len(array)):
    complementedNum=targetSum-array[i]
    if array[i] in complementDict:
        finalArray.append([array[i],complementedNum])
    else:
        complementDict[complementedNum]=i

print(finalArray)

