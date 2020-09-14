num=-134

reverseNum=0


if num>0:
    sign=1
else:
    sign=-1
    num=-num

while num>0:
    reverseNum=reverseNum*10
    reverseNum+=num%10
    num=num//10

print(reverseNum*sign)