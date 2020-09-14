# https://practice.geeksforgeeks.org/problems/nuts-and-bolts-problem/0
order=['!' ,'#' ,'$' ,'%' ,'&', '*' ,'@' ,'^' ,'~']

nuts = ['@', '%', '$', '#', '^']
bolts= ['%', '@', '#', '$', '^']

nuts=['^', '&', '%', '@', '#', '*', '$', '~', '!']
bolts= ['~', '#', '@', '%', '&', '*', '$', '^', '!']

final=[]
for i in order:
    if i in nuts:
        final.append(i)

print(final)
