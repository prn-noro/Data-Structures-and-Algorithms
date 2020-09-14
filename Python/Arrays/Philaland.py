testCases=int(input())
stack=[]
for i in range(testCases):
    sumTwo=1
    maxValue=int(input())
    for i in range(1,maxValue):
        sumTwo+=i
        if sumTwo>=maxValue:
            stack.append(i)
            break

for i in stack:
    print(i)