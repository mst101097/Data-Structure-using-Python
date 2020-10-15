# this function using for selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index]>arr[j]:
                min_index = j

        #swaping arr
        arr[i],arr[min_index] =  arr[min_index],arr[i]

    for i in range(len(arr)):
        print(arr[i],end=",")

A = [5,4,1,8,3]
selection_sort(A)