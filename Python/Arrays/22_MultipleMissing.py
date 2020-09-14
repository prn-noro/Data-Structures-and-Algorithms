# You have given an integer array of size N. Array contains numbers from 1 to N-1 but a couple of numbers are missing in an array which also contains duplicates.

# Write a Java program to print the missing number from the sequence.

# For example, if the given array is {1, 1, 2, 3, 5, 5, 7, 9, 9, 9} then it has length 10 and contains a number from 1 to 9. In this case, missing numbers are 4, 6, and 8.


array=[1, 1, 2, 3, 5, 5, 7, 9, 9, 9]

setArray=set(array)
final=[]
for i in range(len(array)):
    if i not in setArray:
        final.append(i)

print(final)