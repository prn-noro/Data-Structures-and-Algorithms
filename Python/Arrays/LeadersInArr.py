#code
# https://practice.geeksforgeeks.org/problems/leaders-in-an-array/0

testcases=int(input())

for num in range(testcases):
    numElem=int(input())
    array=list(map(int,input().split()))
    maxNum=array[numElem-1]
    final=[]
    final.append(maxNum)
    for i in range(numElem-2,-1,-1):
        if array[i]>=maxNum:
            maxNum=array[i]
            final.append(array[i])
        
    for i in range(len(final)-1,-1,-1):
        print(final[i],end=" ")
    print('\n')