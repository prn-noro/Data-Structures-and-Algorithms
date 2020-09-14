# Removing all adjacent characters from string


string ="ggggeeksffforgeekssss"
string="aabccba"
string="abbacacca"
finalStack=[]
finalStack.append(string[0])
checkChar=finalStack[0]
for i in range(1,len(string)):
    if string[i]!=checkChar:
        checkChar=string[i]
        finalStack.append(string[i])
    else:
        if finalStack and finalStack[-1]==string[i]:  
            finalStack.pop()

final="".join(str(x) for x in finalStack)

print(final)


# class Solution(object):
#    def removeDuplicates(self, S):
#       st = []
#       i = 0
#       while i < len(S):
#          if len(st)!=0 and st[-1]==S[i]:
#             i+=1
#             st.pop(-1)
#          else:
#             st.append(S[i])
#             i+=1
#       return "".join(i for i in st)
# ob1 = Solution()
# print(ob1.removeDuplicates("abbacaca"))