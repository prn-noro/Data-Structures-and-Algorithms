
# https://practice.geeksforgeeks.org/problems/play-with-an-array/1
# Num at odd greater than previous even
# array=[5,3,4,]
array=[5, 4, 3, 2, 1]
for i in range(len(array)):

    if i%2!=0:
        if array[i]>array[i-1]:
            continue
        else:
            array[i],array[i-1]=array[i-1],array[i]

    
print(array)