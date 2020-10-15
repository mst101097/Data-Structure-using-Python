def CountSort(arr,high):
    counter = [0]*(high+1)

    for i in arr:
        counter[i] += 1

    startpoint = 0
    for i in range(len(arr)):
        while 0 < counter[i]:
            arr[startpoint] = i
            startpoint += 1
            counter[i] -= 1

arr = [5,3,2,3,6,1]

CountSort(arr,6)

for i in arr:
    print(i,end=" ")
    