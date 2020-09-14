string="abababcdefababcdab"
string="geeksforgeeks"
# string="abca"
seenDict={}
maxDistinct=float('-inf')

for i in range(len(string)):
    newSet=set()
    count=1
    newSet.add(string[i])
    for j in range(i+1,len(string)):
        if string[j] not in newSet:
            count+=1
            newSet.add(string[j])
        else:
            seenDict[i]=count
            maxDistinct=max(maxDistinct,count)
            break

print(maxDistinct) 
