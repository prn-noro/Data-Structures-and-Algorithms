a1=[1,12,15,26,38]
a2=[2,13,17,30,45]

# final=[1,2,12,13,15,17,26,30,38,45]
a1.extend(a2)
a1.sort()
print(a1)

new_array=[0]*(len(a1)+len(a2))



# for i in range(len(a1)):
#     if a1[i]>

if len(final)%2!=0:
    print(final[len(final)//2])
else:
    n=len(final)//2
    m=n-1
    print((final[n]+final[m])/2)

