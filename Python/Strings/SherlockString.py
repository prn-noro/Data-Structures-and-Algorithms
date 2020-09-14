#!/bin/python3
# Sherlock and the Valid String (https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings)
import math
import os
import random
import re
import sys
from collections import Counter
# Complete the isValid function below.
def isValid(s):
    mostFrequent=0
    countFreq={}
    for i in s:
        if i not in countFreq:
            countFreq[i]=1
        else:
            countFreq[i]+=1
    countDict=Counter(countFreq.values())
    count,value = countDict.most_common(1)[0]
    # print(count)
    result=0
    for i in countFreq:
        result+=abs(countFreq[i]-count)
    if result<=1:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
