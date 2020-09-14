array=[3, 2, 9, 5, 2 ,9 ,4 ,14, 7, 10]
array=[14, 5, 13, 19, 17, 10, 18, 12]

# O(n**2) Solution
# final=[array[0]]

# for i in range(1,len(array)):
#     j=0
#     while j<=len(final):
#         if j==len(final):
#             final.append(array[i])
#             break
#         if array[i]<final[j]:
#             final[j]=array[i]
#             break
#         else:
#             j+=1
#         print(final)

# print(final)

# O(nlogn) Solution

stack=[]

for i in range(len(array)):
    if not stack or stack[-1]<array[i]:
        stack.append(array[i])
    
    elif stack[0]>array[i]:
        stack[0]=array[i]

    else:
        low=0
        high=len(stack)-1

        while high-low>1:
            mid = (low+high)//2

            if array[i]>stack[mid]:
                low=mid
            else:
                high=mid
        
        stack[high]=array[i]
    print(stack)
print(stack)


