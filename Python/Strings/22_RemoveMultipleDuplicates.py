# How do you find duplicate numbers in an array if it contains multiple duplicates

array=[1,2,3,3,5,6,5,1,5,1,2]
freqDict={}
duplicateArray=[]

for i in range(len(array)):
    if array[i] in freqDict:
        freqDict[array[i]]+=1
    else:
        freqDict[array[i]]=1

for number,count in freqDict.items():
    if count!=1:
        duplicateArray.append(number)

print(duplicateArray)
