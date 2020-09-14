# https://practice.geeksforgeeks.org/problems/nth-number-made-of-prime-digits/0

n=10

count=2

primeNos={2,3}



for i in range(4,100):
    status=True
    for j in range(2,i//2):

        if i%j==0:
            status=False
            break
        
    if status==True:
        primeNos.add(i)

print(primeNos)