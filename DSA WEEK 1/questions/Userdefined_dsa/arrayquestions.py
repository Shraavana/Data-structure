#n number of an array display the array after skipping the two values next to the multiple of array---------

# home=[5,1,2,10,2,3,15,1,6]
# homes=[]
# hom=[]
# for i in range(len(home)):
#     if home[i]% 5==0:
#         homes.append(home[i])
#     else:
#         hom.append(home[i])

# print(homes)

#sort an array and print the count of uniques elements----------------------------------------
# from collections import Counter

# sree=[1,1,2,2,3,3,4,5]
# sree.sort()
# count = 0
# uniq = []
# for i in sree:
#     if i not in uniq:
#         uniq.append(i)
#         count += 1
#         print(i)

# print(count)
# print(len(uniq))

#delete the duplicate elements from an array--------------------------------------------
# arr = [1, 2, 3, 2, 4, 1, 5]

# # Use a set to keep track of unique elements
# unique_elements = set()
# result = []

# # Iterate through the array
# for element in arr:
#     # If the element is not in the set, add it to the set and result list
#     if element not in unique_elements:
#         unique_elements.add(element)
#         result.append(element)

# # Replace the original array with the result
# arr[:] = result

# print("Array after removing duplicates:", arr)

#program to remove the prime numbers from the array---------------------------------

        
#write a program to abc in the str------------------------------------
# stro="htghabcejdkabceujabceoijabc"
# sub="abc"
# res =stro.count(sub)
# print(res)

#find the element and return the sum of the indexes if one or two elements not seeing in the element return -1-----------------------------------

# list = [1, 2, 3, 4, 5]
# target1 = 2
# target2 = 5

# indices_sum = 0
# found_targets = []

# for i, num in enumerate(list):
#     if num == target1 or num == target2:
#         indices_sum += i
#         found_targets.append(num)
# if len(found_targets)!= 2:
#     print("-1")
# else:
#     print(indices_sum)


#count of the each letter in the string that given--------------------------------------------
# stri="shraavana"
# count={}
# for char in stri:
#     if char in count:
#         count[char]+=1

#     else:
#         count[char] = 1

# for i ,char_count in count.items():
#     print(f"{i}:{char_count}")



# sum of the prime number----------------------------------------------

# arr = [1, 67, 9, 7, 64, 16, 13]
# prime = []

# for i in range(len(arr)):
#     flag = 0
#     for j in range(2, arr[i]):
#         if arr[i] % j == 0:
#             flag += 1
#             break  # No need to continue checking further once a factor is found
#     if flag == 0:  # Adjusted condition to check for prime numbers
#         prime.append(arr[i])

# print(prime)

# sort an array and print the count of prime numbers in the array------------------------------------------
# arry = [1, 3, 2, 4]
# arry = sorted(arry)
# print("Sorted array:", arry)

# guru = []

# for i in range(len(arry)):
#     flag = 0
#     if arry[i] < 2:
#         continue  # Skip numbers less than 2
#     for j in range(2, arry[i]):
#         if arry[i] % j == 0:
#             flag = 1
#             break
#     if flag == 0:
#         guru.append(arry[i])

# print("List of prime numbers:", guru)
# guru_sum = sum(guru)
# print("Sum of prime numbers:", guru_sum)




#array is sorted or not how to check that------------------------------------------------------------------------
# def is_sorted(arr):
#     sorted = True
#     for i in range(len(arr)-1):
#         if arr[i]>arr[i+1]:
#             sorted = False
        
#     return sorted
    

# arr=[1,2,3,4,5,6]
# res=is_sorted(arr)
# print(res)



#how to print the hello world to world hello---------------------------------------------------------------------

# strg="hello world"
# strg=strg.split(' ')
# print(strg)
# res=strg[::-1]
# print(res)
# result = ' '.join(res)
# print(result)

#count the frequency of element in that array------------------------------------------------------------------------

# arr=[1,1,2,2,3,4,5]
# count={}
# for i in arr:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1

# for i ,char_count in count.items():
#     print(f"{i}:{char_count}")


#find the smallest elemnt in an array--------------------------------------------------------------------------

# arr=[1,2,3]
# arr=min(arr)
# print(arr)



#find the sum of the values ,if sum is greater than 100 delete the even values if sum is odd then delete the even values----------------------------------------------------------
# from collections import Counter
# arr=[1,1,2,3,4,4,3,3,2,2,4,56,7,9990,6]

# counts=Counter(arr)
# print(counts)
# arr=[num for num in arr if counts[num]<2]

# print(arr)

#delete the 2 values next to the odd number

# def delete_next_two_after_odd(arr):
#     i = 0
#     while i < len(arr):
#         if arr[i] % 2 != 0:  
            
#             if i + 1 < len(arr):
#                 del arr[i + 1]
#             if i + 1 < len(arr):
#                 del arr[i + 1]
#         i += 1
#     return arr
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# updated_arr = delete_next_two_after_odd(arr)
# print("Updated array:", updated_arr)
