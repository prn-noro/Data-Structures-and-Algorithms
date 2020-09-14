#User function Template for python3
# https://practice.geeksforgeeks.org/problems/case-specific-sorting-of-strings4845/1
'''
	Your task is to return the case sorted string
	as described in the problem statement above.
	
	Function Arguments: string s and size n. 
	Return Type: string
'''
def caseSort(s,n):
    #code here
    final=[0]*n
    lower=[]
    upper=[]
    finalString=""
    for i in range(n):
        if s[i].islower():
            final[i]=0
            lower.append(s[i])
        else:
            final[i]=1
            upper.append(s[i])
    lower.sort()
    upper.sort()
    
    for i in final:
        if i==0:
            char=lower.pop(0)
            finalString+=char
        else:
            char=upper.pop(0)
            finalString+=char
    return finalString