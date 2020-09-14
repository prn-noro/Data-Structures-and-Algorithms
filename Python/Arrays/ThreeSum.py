A = [1, 4, 45, 6, 10, 8] 
k = 22


A.sort() #O(nlogn)
for i in range(len(A)-2): #O(n)

    fixed=A[i]

    left=i+1
    right=len(A)-1

    while left<right:#O(n)

        if fixed+A[left]+A[right]==k:
            print(fixed,A[left],A[right])
            break
        elif (fixed+A[left]+A[right]) < k:
            left+=1
        else:
            right-=1

        print('No Triplet Found')


# Time Complexity : O(n**2) +O(nlogn) ==> O(n**2)
