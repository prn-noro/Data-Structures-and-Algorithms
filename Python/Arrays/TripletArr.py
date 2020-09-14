# You are given an array. You have to find whether there is a triplet of index i, j, k such that i<j<k and a[i]<a[j]<a[k].
# Expected time complexity O(n).
arr = [12, 3, 10, 5, 6, 2, 30] 

n=len(arr)
minIndex=0
maxIndex=n-1

smaller=[0]*n

# There exists no smaller element before 0
smaller[minIndex]=-1

for i in range(1,n):
    if arr[i]<arr[minIndex]:
        minIndex=i
        smaller[i]=-1
    else:
        smaller[i]=minIndex

greater=[0]*n
greater[maxIndex]=-1

for i in range(n-2,-1,-1):
    if arr[i]>arr[maxIndex]:
        maxIndex=i
        greater[i]=-1
    else:
        greater[i]=maxIndex

for i in range(len(arr)):
    if greater[i]!=-1 and smaller[i]!=-1:
        print(arr[smaller[i]],arr[i],arr[greater[i]])
    