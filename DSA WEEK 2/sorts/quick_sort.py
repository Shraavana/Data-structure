def quick_sort(arr):
    n =len(arr)
    if n <=1:
        return arr
    else:
        pivot=arr[n//2]
        left=[x for x in arr if x < pivot]
        middle=[x  for x in arr if x == pivot]
        right=[x for x in arr if x > pivot]

        return quick_sort(left)+middle+quick_sort(right)
    
arr=[1,4,2,3]
print(quick_sort(arr))

