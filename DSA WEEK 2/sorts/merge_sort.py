def merge_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    mid = n // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    # Append remaining elements from both halves
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

lst = [3, 1, 2, 5, 6]
print(merge_sort(lst))
