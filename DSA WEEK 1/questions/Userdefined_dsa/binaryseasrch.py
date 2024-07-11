
# def bin(lst,target):
#     low=0
#     high=len(lst)-1
#     lst=sorted(lst)
#     while low <= high :
#         mid=(low+high)//2

#         if lst[mid]==target:
#            return mid
    
#         elif lst[mid] > target:
#             high = mid-1
    
#         else:
#             low = mid+1

# lst = [2,11,4,8,9,7,5,3]   
# target=4
# res=bin(lst,target)
# print(res)


# def factorial(n):
#     if n<=1:
#         return n 
#     else:
#         return n*factorial(n-1)
    
# res=factorial(5)
# print(res)

# def rec(lst,val):
#     if len(lst)<=1:
#         return val
#     val.add(lst[0])
#     return rec(lst[1:],val)
# lst=[1,2,1,3,4,5,5]
# val=set()
# print(rec(lst,val))

# def recrus(lst, lis):
#     if len(lst)<1:
#         return lis
#     val = lst.pop()
#     lis.append(val)
#     return recrus(lst, lis)
    

# lst=[1,2,3,4]
# lis=[]
# print(recrus(lst, lis))
