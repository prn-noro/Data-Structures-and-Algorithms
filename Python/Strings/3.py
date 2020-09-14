# Longest Palindrome in a string
# https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string/0
# Given a string S, find the longest palindromic substring in S

#code

def checkIfPalindrome(string):
    reverseString=string[::-1] #This has time complexity O(n)
    if string==reverseString:
        return True
    return False

# testcases=int(input())
lenPalDict={}
maxLength=0
# for num in range(testcases):
string="rfkqyuqfjkxy"
string="forgeeksskeegfor"
# string="aaaabbaa"
for i in range(len(string)):
    count=0
    for j in range(len(string)):
        testString=string[i:j+1]
        if(checkIfPalindrome(testString)):
            count=(j-i)+1
    lenPalDict[i]=count
    maxLength=max(maxLength,count)
# print(lenPalDict)
# print(maxLength)

for i in lenPalDict:
    if lenPalDict[i]==maxLength:
        print(string[i:i+maxLength])
        break


# Time Complexity O(n3)
# Space Complexity O(n)