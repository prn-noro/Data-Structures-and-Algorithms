# Missing Number

array=[1, 2, 3, 4, 5, 6, 7, 8, 10]

n=len(array)+1

sumTotal=n*(n+1)//2

print(sumTotal-sum(array))