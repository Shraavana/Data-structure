# def recrusion(n):
#     if n<=1:
#         return n
#     else:
#         return n*recrusion(n-1)
# print(recrusion(5))
# #--------------------------------------------------------------------------
# def fibonnoci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonnoci(n-1)+fibonnoci(n-2)
# print(fibonnoci(10))


# def rec(lis,val):
#     if len(lis)<1:
#         return val
#     val.add(lis[0])
#     return rec(lis[1:],val)
# lis=[1,1,2,3,4,4,3,2,5,65]
# val=set()
# res=rec(lis,val)
# print(res)




# recrusion using binary search

# def recrusion_binary(lis,target,low=None,high=None):
#     if low is None:
#         low=0

#     if high is None:
#         high = len(lis)-1

#     if low  > high:
#         return None
    

#     mid=(low+high)//2
#     guess=lis[mid]


#     if guess == target:
#         return mid
    
#     if guess > target:
#         return recrusion_binary(lis,target,low,mid-1)
    
#     if guess < target:
#         return recrusion_binary(lis,target,mid+1,high)
    


# lis=[1,2,3,4,5]
# target=1
# res=recrusion_binary(lis,target)
# print(res)