# https://practice.geeksforgeeks.org/problems/recursively-remove-all-adjacent-duplicates/0 (No Recursion)
# Given a string s, remove duplicate characters from the string s. The output string should not have any adjacent duplicates.


# def removeAdj(string,n):



string = "geeks for geeks"
# Output = gks
# removeAdj(string,len(string))

finalStack=''
# finalStack.append(string[0])
for i in range(len(string)):
    if string[i] in finalStack:
        continue
    else:
        finalStack+=string[i]
    
# final="".join(str(x) for x in finalStack)

print(finalStack)