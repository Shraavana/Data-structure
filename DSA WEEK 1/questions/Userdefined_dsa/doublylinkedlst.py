class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

        
class doublyLL:
    def __init__(self):
        self.head = None

    def printLL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.nref
#-------------------------------------------reverse the dubly linked list------------------------
    def printLL_reverse(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,"-->",end=" ")
                n = n.pref    

#--------------------------------------------------------------------------------------
    def insert_empty(self,data):
        if self.head is None:
          new_node = Node(data)
          self.head = new_node
        else:
             print("Linked list is not empty")

#--------------------------------------------------------------------
    def add_begin(self,data):
      new_node =Node(data)
      if self.head is None:
        self.head = new_node

      else:
        new_node.nref =self.head
        self.head.pref = new_node
        self.head = new_node

#----------------------------------------------------------------------                
    def add_end(self,data):
       new_node=Node(data)
       if self.head is None:
           self.head = new_node

       else:
        n = self.head
        while n.nref is not None:
            n = n.nref
        n.nref = new_node
        new_node.pref = n
#------------------------------------------------------------------
    def add_after(self,data,x):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n = n.nref
            if n is None:
                print("Given node is  not present in ddbly ")
            else:
                new_node = Node(data) 
                new_node.nref = n.nref
                new_node.pref = n 
                if n.nref  is not None:
                    n.nref.pref = new_node
                n.nref = new_node
#-------------------------------------------j-----------------------------------
    def add_before(self,data,x):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                if x==n.data:
                    break
                n = n.nref
            if n is None:
                print("Given node is  not present in ddbly ")

            else:
               new_node = Node(data)
               new_node.nref = n
               new_node.pref = n.pref
               if n.pref is not None:
                n.pref.nref = new_node 
               else:
                self.head = new_node
               n.pref =new_node
#------------------------------------------------------------------------------------------
    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty ")
            return
        if self.head.nref is None:
            self.head = None
            print("Dbbly is empty after deleting the node")
        else:
            self.head=self.head.nref
            self.head.pref = None
#--------------------------------------------------------------------------------
    def delete_end(self):
        if self.head is None:
            print("Dll is empty")
            return
        if self.head.nref is None:
            self.head = None
            print("Dll is empty after deleting the node")

        else:
            n = self.head 
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None
    def delete_by_value(self,x):
        if self.head is None:
            print("Dll is empty cant delete")
            return
        if self.head.nref is None:
            if x==self.head.data:
                self.head = None

            else:
                print("x is not present in DLL")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref .pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data==x:
                n.pref.nref = None
            else:
                print("x is not present in dll")


LL1=doublyLL()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.delete_by_value(20)
LL1.printLL()

