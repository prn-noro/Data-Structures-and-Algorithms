# s='Bawds jog, flick quartz, vex nymph'
s='bab'
status=True
s=s.lower()
char=[0]*26


for i in s:
    if i==" " or i==",":
        continue
    char[ord(i)-ord('a')]+=1
    # print(char)
# print(char)

for i in char:
    if i==0:
        # print(0)
        status=False
    
if status==False:
    print(0)
else:
    print(1)