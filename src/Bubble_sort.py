#Bubble sort
def Bubble(arr):
    n= len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                print("swaping" + str(arr[j]) + "and" + str(arr[j+1]))
                arr[j],arr[j+1] = arr[j+1],arr[j]
                print(arr)

arr= [9,5,2,6]
# to print

Bubble(arr)
print(arr)

