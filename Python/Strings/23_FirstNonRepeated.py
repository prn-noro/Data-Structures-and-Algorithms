# How do you print the first non-repeated character from a string

string="geeksforgeeks"
freqDict={}

for i in string:
    if i not in freqDict:
        freqDict[i]=1
    else:
        freqDict[i]+=1
    
for i in string:
    if freqDict[i]==1:
        print(i)
        break

