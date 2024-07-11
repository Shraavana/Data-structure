#insert a node at the begin of a linked list

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.ref=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
#     def print(self):
#         if self.head is None:
#             print("linked list is empty")
#         else:
#             n=self.head
#             while n is not None:
#                 print(n.data,end=" ")
#                 n=n.ref
#     def add(self,data):
#         new_node=Node(data)
#         new_node.ref= self.head
#         self.head = new_node

#     def end(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             n=self.head
#             while n.ref is not None:
#                 n=n.ref
#             n.ref =new_node

#     def add_after(self,data,x):
#         n=self.head
#         while n is not None:
#             if n.data ==x:
#                 n=n.ref
#                 if n is None:
#                     print("lnked list is empty")
#                 else:
#                     new_node=Node(data)
#                     new_node.ref = n.ref
#                     n.ref = new_node

#     def  delete(self):
#         if self.head is None:
#             print("ntg to delete")
#         else:
#             self.head =self.head.ref

#     def delete_end(self):
#         if self.head is None:
#             print("linked list is wmpty ")
#         elif self.head.ref is not None:
#             self.head = None
#         else:
#             n=self.head
#             while n.ref.ref is not None:
#                 n=n.ref
#             n.ref = None

#     def dele_value(self,x):
#         if self.head is None:
#             print("ntg to delete")
#             return
#         if self.head.data==x:
#             self.head = self.head.ref
#             return 
#         n=self.head
#         while n.ref is not None:
#             if x==n.ref.data:
#                 break
#             n=n.ref
#         if n.ref is None:
#             print("Node is node present")

# l=Linkedlist()
# l.add(10)
# l.add(20)
# l.add(50)
# l.delete()
# l.print()
    
#-------------------------------------------------------------------------------------------------------------
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.ref=None

# class linkedlist:
#     def __init__(self):
#         self.head=None

#     def append(self,data):
#         if self.head is None:
#             self.head=Node(data)
#         else:
#             n=self.head
#             while n.ref:
#                 n=n.ref
#             n.ref=Node(data)
#     def display(self):
#         elems=[]
#         cur=self.head
#         while cur:
#             elems.append(cur.data)
#             cur=cur.ref
#         print(elems)

#     def lli(self,list):
#         for i in list:
#             self.append(i)
# list=[1,2,3]
# lli=linkedlist()
# lli.lli(list)
# lli.display()

# def fibonnacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonnacci(n-1)+fibonnacci(n-2)
    
# print(fibonnacci(10))

# def recrusion(n):
#     if n<=1:
#         return n
#     else:
#         return n*recrusion(n-1)
# print(recrusion(4))

# str="htgabcwrufjowjfabcjofjabc"
# substring="abc"
# sree=str.count(substring)
# print(sree)

# str="unni"
# count={}
# for i in str:
#     if i in count:
#         count[i]+=1
#     else:
#         count=1

# for char,char_count in count.items():
#     print(f"{char}:{char_count}")
# def binary(lst,target,low=None,high=None):
#     if low is None:
#         low=0

#     if high is None:
#         high=len(lst)-1

#     if low > high:
#         return None
    
#     mid=(low+high)//2
#     guess=lst[mid]


#     if guess == target:
#         return mid
    
#     if guess>target:
#         return binary(lst,target,low,mid-1)
#     else:
#         return binary(lst,target,mid+1,high)
    

# lst=[12,34,56]
# target=34
# index=binary(lst,target)
# if index is not None:
#     print(f"target is found at index:{index}")

# else:
#     print("target is not found")

# def binary_recrusive(lst,target,low=None,high=None):
#     if low is None:
#         low=0

    
#     if high is None:

#         high=len(lst)-1


#     if low > high:
#         return None
    

#     mid=(low+high)//2
#     guess=lst[mid]

#     if guess==target:
#         return mid
    
#     if guess > target:
#         return binary_recrusive(lst,target,low,mid-1)
    
#     if guess < target:
#         return binary_recrusive(lst,target,mid+1,high)
    



# lst=[1,2,3,45,6,7,8,9]
# target=45
# index=binary_recrusive(lst,target)


# if index is not None:
#     print(f"{index}")

# else:
#     print("hiiiii")

# def binary_search(lst,target):
#     low=0
#     high=len(lst)-1

#     while low<=high:
#         mid=(low+high)//2
#         guess=lst[mid]

#         if guess==target:
#             return mid
#         if guess > target:
#             return mid-1
#         if guess < target:
#             return mid +1
        

# lst=[1,2,3,4,5,6]
# target=4
# index=binary_search(lst,target)
# if index is not None:
#     print(f"{index}")




# def recrusion(n):
#     if n<=1  :
#         return n 
#     else:
#         return n*recrusion(n-1)
    

# print(recrusion(5))


# def recrusion(n):
#     if n<=1:
#         return n 
#     else:
#         return recrusion(n-1)-recrusion(n-2)
    

# print(recrusion(10))

# class MinHeap:
#     def __init__(self):
#         self.heap=[]


#     def get_parent_child_index(self,index):
#         return index + 1 // 2
#     def get_left_child_index(self,index):
#         return 2*index+1
#     def get_right_child_index(self,index):
#         return 2*index+2
#     def swap(self,index1,index2):
#         self.heap[index1],self.heap[index2]=self.heap[index2],self.heap[index1]

#     def insert(self,value):
#         self.heap.append(value)
#         self.heapify_up
        
#     def heapify_up(self):
#         current_index =  len(self.heap)-1
#         while current_index>0:
#             parent_index = self.get_parent_child_index(current_index)
#             if self.heap[parent_index] > self.heap[current_index]:
#                 self.swap(parent_index,current_index)
#                 current_index = parent_index
#             else:
#                 break
    
#     def remove_value(self):
#        if len(self.heap) == 0:
#            return None
#        if len(self.heap) == 1:
#            return self.heap.pop()
#        else:
#            min_value = self.heap[0]
#            self.heap[0]=self.heap.pop()
#            self.heapify_down()
#            return min_value
       
#     def heapify_down(self):
#         current_index = 0
#         while self.get_left_child_index(current_index) <len(self.heap):
#             left_child_index= self.get_left_child_index(current_index)
#             rigth_child_index= self.get_right_child_index(current_index)
#             min_value= left_child_index

#             if rigth_child_index < len(self.heap)and self.heap[rigth_child_index]:
#                 min_value=rigth_child_index

#             if self.heap[min_value] <self.heap[current_index]:
#                 self.swap(min_value,current_index)
#                 current_index=min_value
#             else:
#                 break

#     def display(self):
#         print(self.heap)

#     def sort(self):
#         s_arry=[]
#         while self.heap:
#             s_arry.append(self.remove())
#         self.heap = s_arry
#         return s_arry


# class CycleGraph:
#     def __init__(self):
#         self.cycle_vertex = {}

#     def add_vertex(self,vertex):
#         if vertex not in self.cycle_vertex:
#             self.cycle_vertex[vertex]=set()

#     def add_edge(self,vertex1,vertex2):
#         if vertex1 not in self.cycle_vertex:
#             self.add_vertex(vertex1)
#         if vertex2 not in self.cycle_vertex:
#             self.add_vertex(vertex2)
        
#         self.cycle_vertex[vertex1].add(vertex2)
#         self.cycle_vertex[vertex2].add(vertex1)

#     def display(self):
#         for vertex in self.cycle_vertex:
#             print(f"{vertex}=>{list(self.cycle_vertex[vertex])}")
         

# cyclic=CycleGraph()
# cyclic.add_vertex("A")
# cyclic.add_vertex("B")
# cyclic.add_vertex("C")
# cyclic.add_edge("A","B")
# cyclic.add_edge("B","C")
# cyclic.add_edge("C","A")
# cyclic.display()
                  





class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    
    def is_empty(self):
        return self.root is None
    

    def insert(self,value):
        node=Node(value)
        if self.is_empty():
            self.root=node

        else:
           current=self.root
           while True:
               if value<current.value:
                   if current.left is None:
                       current.left=node
                       break
                   current=current.left

               else:
                   if current.right is None:
                       current.right=node
                       break
    

    def preorder(self,root):
        if root :
            
        
          print(root.value)
          self.preorder(root.left)
          self.preorder(root.right)


bst=BST()
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.preorder(bst.root)

