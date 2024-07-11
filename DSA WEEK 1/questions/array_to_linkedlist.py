class Node:
    def __init__(self, data=None):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            n= self.head
            while n.ref:
                n=n.ref
            n.ref = Node(data)

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node:
            elems.append(cur_node.data)
            cur_node = cur_node.ref
        print(elems)

    def list_to_linked_list(self, input_list):  # Corrected here
        for item in input_list:
            self.append(item)

# Example usage
my_list = [1, 2, 3, 4, 5]
linked_list = LinkedList()
linked_list.list_to_linked_list(my_list)  # Corrected here
linked_list.display()


# def linear_search(arr,target):
    
#     for i in arr:
#         # if arr[i] == target:
#         #     return i
#         print(i)
#     for i in range(len(arr)):
#         # if arr[i] == target:
#         #     return i
#         print(i)
        
#     # return -1

# home=[1,20,13,-2,30,"sree"]
# target=30
# result=linear_search(home,4)
# print(result)

sree=[1,2,3]
ind=1
for i in range(len(sree)):
    if i == ind:
        break    


      
      
      