string1="abcd"
string2="adbc"

s1Count={}
s2Count={}

for i in string1:
    if i not in s1Count:
        s1Count=1
    else:
        s1Count[i]+=1

for i in string2:
    if i in s2Count:
        s2Count[i]+=1
    else:
        s2Count=1

# print(s1Count==s2Count)