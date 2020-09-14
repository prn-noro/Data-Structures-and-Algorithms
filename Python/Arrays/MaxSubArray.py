# Find Max Sum of Subarray of size K (Sliding Window Protocol) 

a=[4,2,1,7,8,1,2,8,1,0]
currentSum=0
maxSum=0
k=3
count=0
left=0
for i in range(len(a)):
    currentSum+=a[i]
    count+=1
    if count>=k:
        maxSum=max(maxSum,currentSum)
        currentSum-=a[left]
        left+=1

print(maxSum)