class Node:
    def __init__(self,data):
        self.data = data
        self.ref =None
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def print(self):
       if  self.head is None:
           print("Linked list is empty")

       else:
           n =self.head
           while n is not None:#====To travel the entire linkedlist======
            print(n.data , end =" ")
            n=n.ref
#--------------------------------add data at begin----------------------------------------------
    def add_begin(self,data):    #=======================Adding the element on the begining of the linked list
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
#---------------------------add data at end--------------------------------------
    def add_end(self,data):       #======================Adding the element on the end of the linkedlist
        new_node=Node(data)
        if self.head is None:
            self.head = new_node

        else:
            n=self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
#-----------------------------nth find the data----------------------------------------
    def nth_find(self, n):
        n = self.head
        while n is not None:
            if n.data == n:
                return f"\n{n.data} the values has been found"
            n = n.ref
        print('data is not present')
#----------------------------------------add the node after a "x" value ------------------------
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                n=n.ref
        if n is None:
            print("Node is not present in Linked list")
        else:
            new_node =Node(data)
            new_node.ref = n.ref
            n.ref = new_node
#-------------------------------------------add the node before the "x"---------------------------
    def add_before(self,data,x):
         if self.head is None:
          print("Linked list is empty")
          return
         if self.head.data ==x:
             new_node=Node(data)
             new_node.ref=self.head
             self.head=new_node
             return
         n=self.head
         while n.ref is not None:
            if n.ref.data==x:
                break
            n=n.ref
         if n.ref is None:
            print("Node is not found")

         else:
             new_node=Node(data)
             new_node.ref=n.ref
             n.ref=new_node
#----------------------------------add element in an empty list---------------------------------
    def insert_emp(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node

        else:
            print("linked list is not empty")
#------------------------------------------------------------------------------------------------------------------------
    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            self.head=self.head.ref


    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref =None
    def delete_value(self,x):
        if self.head is None:
            print("Nothing to delete")
            return
        if x ==self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x==n.ref.data:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not present")
        else:
            n.ref=n.ref.ref
    def print_reverse(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            prev = None
            n= self.head
            next_node = None
            
            while n is not None:
                next_node = n.ref
                n.ref = prev
                prev = n
                n = next_node
                
            # Resetting head to original position
            self.head = prev
            
            # Printing reversed list
            while prev is not None:
                print(prev.data,end=" ")
                prev = prev.ref
    def get_middle(self):
        if self.head is None:
            print("Linked list is empty")
            return None
        slow = self.head
        fast = self.head

        while fast is not None and fast.ref is not None:
            slow = slow.ref
            fast = fast.ref.ref

        return print(f"{slow.data}")
LL1 =Linkedlist()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_begin(40)
LL1.add_begin(60)
LL1.add_begin(30)
LL1.get_middle()
LL1.print()


