finalArr=[0,0]
artifacts="1B 2C, 2D 4D"
searched="2B 2D 3B 3D 4A"
mySet=set()

myArr=artifacts.split(",")

for i in myArr:
    spot=i.lstrip()
    spotArr=spot.split(" ")
    spotArr.sort()
    index=0
    while(spotArr[0][0]!=spotArr[len(spotArr)-1][0]):
        string=spotArr[0][index]
        mySet.add(string)
        
    print(mySet)