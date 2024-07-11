# def linear_search(arr,target):
    
#     for i in arr:
#         if arr[i] == target:
#             return i
        
#     return -1

# number=[3,2,5,4,6,4]
# target=4
# result=linear_search(number,4)
# print(result)

# Write a Python function linear_search_all(arr, target) that takes a list arr of integers and a target integer target. Implement the linear search algorithm to find all indices
#  where target occurs in the list arr. If target is not present in the list, return an empty list.
#  arr = [3, 5, 2, 7, 5, 9, 1, 5]
# target = 5
# print(linear_search_all(arr, target))  # Output: [1, 4, 7]

# target = 4
# print(linear_search_all(arr, target))

# def linear_Search_all(arr,target):
#     indexes=[]
#     for i in range(len(arr)):
#         if arr[i]==target:
#             indexes.append(i) 
#     return indexes
# numbers=[1,2,3,4,3,5,3]
# target=3
# result=linear_Search_all(numbers,target)
# print(result)

# def search(words,allowed):
#     count=0
#     for i in range(len(words)):
#         if words[i]==allowed:
#             count=count+1
#     return count
# words=["ab","ad","aab","daa"]
# allowed="ab"
# reusult=search(words,allowed)
# print(reusult)

#example one----------------------------
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i  
    return -1  
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
index = linear_search(numbers, target)
if index!= -1:
    print(f"Target found at index {index}")
else:
    print("Target not found")
#example two---------------------------------------------
def linear_search_multiple(targets, lst):
    indices = []
    for t in targets:
        for i in range(len(lst)):
            if lst[i] == t:
                indices.append(i)
                break  
    return indices

# Test the function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
targets = [2, 5, 7]
indices = linear_search_multiple(targets, numbers)
print(f"Indices of targets: {indices}")
#example three---------------------------------------------
def linear_search_with_message(targets, lst):
    found_indices = []
    for t in targets:
        for i in range(len(lst)):
            if lst[i] == t:
                found_indices.append(i)
                break  
    if found_indices:
        print(f"Targets found at indices: {found_indices}")
    else:
        print("None of the targets were found.")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
targets = [2, 5, 7]
linear_search_with_message(targets, numbers)
