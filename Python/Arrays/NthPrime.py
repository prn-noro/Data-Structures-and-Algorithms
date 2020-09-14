# https://practice.geeksforgeeks.org/problems/nth-number-made-of-prime-digits/0


def isPrime(n):

    if n==1 or n==0:
        return False

    for i in range(2,(n//2)+1):
        if n%i==0:
            return False

    return True

n=10
count=0
currentPrime=[]
for i in range(1,500):

    

    number=i
    status=True
    while number!=0:
        singleDigit=number%10
        number=number//10

        if isPrime(singleDigit):
            continue
        else:
            status=False
            break

    if status==True:
        count+=1
        currentPrime.append(i)

print(currentPrime[10])