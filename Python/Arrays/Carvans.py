# codechef.com/problems/CARVANS

array=[10]
count=1
currSpeed=array[0]

for i in range(1,len(array)):
    if array[i]<=currSpeed:
        count+=1 
        currSpeed=array[i]
    
print(count)