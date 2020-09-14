# https://practice.geeksforgeeks.org/problems/merge-k-sorted-arrays/1

array=[[1, 2, 3], [4, 5, 6],[7, 8, 9]]

# Merge Two sorted arrays
# a1=[1,2,3]
# a2=[2,5,6]

def mergeTwoArray(a1,a2):
    new_final=[0]*(len(a1)+len(a2))

    i=0
    j=0
    k=0

    while i<len(a1) and j<len(a2):

        if a1[i]<a2[j]:
            new_final[k]=a1[i]
            i+=1
            k+=1
        else:
            new_final[k]=a2[j]
            j+=1
            k+=1
        
    if i<len(a1):
        while i<len(a1):
            new_final[k]=a1[i]
            i+=1
            k+=1

    if j<len(a2):
        while j<len(a2):
            new_final[k]=a2[j]
            j+=1
            k+=1
    return new_final


# array=[[1, 2, 3], [4, 5, 6],[7, 8, 9]]
array=[[1, 2, 2, 2],[3, 3, 4, 4],[5, 5, 6, 6],[7, 8, 9, 9 ]]
first=array[0]

for i in range(1,len(array)):
    new_array=array[i]
    first=mergeTwoArray(first,new_array)


print(first)