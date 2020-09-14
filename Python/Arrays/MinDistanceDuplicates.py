
array=[3, 2, 2, 1, 4, 5, 8, 6, 7, 4, 2]
seen={}
minDistance=float('inf')
for i in range(len(array)):
    if array[i] not in seen:
        seen[array[i]]=i
    else:
        minDistance=min(minDistance,i-seen[array[i]])
    
print(minDistance)