# Permutations of a given string
# Given a string S. The task is to print all permutations of a given string.
# https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string/0
from itertools import permutations 
string="ABC"

perms=permutations(string)

for word in list(perms):
    print("".join(word))
