#example one-------------------------------------------
# def binary_search(lst, target):
#     low = 0
#     high = len(lst) - 1
    
#     while low <= high:
#         mid = (low + high) // 2
#         guess = lst[mid]
        
#         if guess == target:
#             return mid  # Target found
#         if guess > target:
#             high = mid - 1  # Search lower half
#         else:
#             low = mid + 1  # Search upper half
            
#     return None  # Target not found

# Test the function
# sorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 5
# index = binary_search(sorted_numbers, target)
# if index is not None:
#     print(f"Target found at index {index}")
# else:
#     print("Target not found")
#example two-------------------------------------------
# def binary_search_recursive(lst, target, low=None, high=None):
#     if low is None:
#         low = 0
#     if high is None:
#         high = len(lst) - 1
        
#     if low > high:
#         return None  
    
#     mid = (low + high) // 2
#     guess = lst[mid]
    
#     if guess == target:
#         return mid  
#     if guess > target:
#         return binary_search_recursive(lst, target, low, mid - 1)  # Search lower half
#     else:
#         return binary_search_recursive(lst, target, mid + 1, high)  # Search upper half

# # Test the function
# sorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 5
# index = binary_search_recursive(sorted_numbers, target)
# if index is not None:
#     print(f"Target found at index {index}")
# else:
#     print("Target not found")
#example three--------------------------------------------------
# def binary_search_error_handling(lst, target):
#     try:
#         low = 0
#         high = len(lst) - 1
        
#         while low <= high:
#             mid = (low + high) // 2
#             guess = lst[mid]
            
#             if guess == target:
#                 return mid  # Target found
#             if guess > target:
#                 high = mid - 1  # Search lower half
#             else:
#                 low = mid + 1  # Search upper half
                
#         return None  # Target not found
#     except TypeError:
#         print("Error: List must contain comparable items.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# # Test the function
# sorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 5
# index = binary_search_error_handling(sorted_numbers, target)
# if index is not None:
#     print(f"Target found at index {index}")
# else:
#     print("Target not found")
