#!/bin/python3
# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    totalSwaps=0
    positionValue={}
    # Creating Dictionary of Values with their Current Positions
    for index,value in enumerate(arr):
        positionValue[value]=index
    
    for i in range(len(arr)):
        # If element not in their current position
        if arr[i]!=i+1:
            # Increment Swaps
            totalSwaps+=1
            # Get the value which is not placed correctly
            temp=arr[i]
            # Store the correct value inside the index
            arr[i]=i+1
            storingIndex=positionValue[i+1]
            # Store the temp value at the place where the value was swapped
            arr[storingIndex]=temp
            # Updating the dictionary
            positionValue[temp]=storingIndex
    return totalSwaps
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
