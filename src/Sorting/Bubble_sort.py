def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

A = [40,20,50,60,30,10]

bubble_sort(A)

for i in range(len(A)):
    print(A[i],end=",")
