#1 You are given an string of n characters. you have to remove exactly k characters and make the lexicographically smallest string. Expected time complexity O(n) .

string='abzaxbcfdsxyz'
k=1
final=""
for i in range(len(string)-1):

    if len(string)<k:
        print("")
        break

    if k!=0:
        if string[i]<string[i+1]:
            final+=string[i]
        else:
            k-=1
        
    else:
        if i!=len(string)-1:
            final+=string[i:]
            break

print(final)