def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]#if we want to print in reverse order use j instead of i
    return arr

arr=[1,3,2,5,4]
res=selection_sort(arr)
print(res)
