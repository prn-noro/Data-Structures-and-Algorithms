# Find Max Sum of Subarray of size K (Sliding Window Protocol) 

a=[4,2,1,7,8,1,2,8,1,0]
k=3
final=[]
sumTillHere=0
maxSum=-1000000
count=0
for i in range(len(a)):
    sumTillHere+=a[i]
    if i>=k-1:
        maxSum=max(maxSum,sumTillHere)
        sumTillHere-=a[i-k+1]

print(maxSum)
