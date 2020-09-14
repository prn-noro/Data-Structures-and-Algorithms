# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
arr=[1, 3, 5, 2, 4, 6, 7]
swaps=0
valPosition={}

for i in range(len(arr)):
    valPosition[arr[i]]=i

for i in range(len(arr)):
    if arr[i] == i+1:
        continue
    else:
        wrongElem=arr[i]
        swaps+=1
        arr[i]=i+1

        index=valPosition[i+1]

        arr[index]=wrongElem

        valPosition[wrongElem]=index

        print(arr)
        # print(wrongElem)
    
print(swaps)

