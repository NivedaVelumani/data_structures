class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None

    #traversing a linked list
    def printLL(self):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            n=self.head
            while n is not None:
                print(n.data ,"-->" ,end=" ")
                n=n.ref

    #insert at begining
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node

    #insert at end
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref

            n.ref=new_node

    #insert_after_node
    def add_after_node(self,data,x):
       
        n=self.head
        while n is not None:
            if n.data == x:
                break
            n=n.ref
        if n is None:
            print("The node is not present")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
            
    #insert before node
    def add_before_node(self,data,x):
        if self.head is None:
            print("The linked list is empty")
            return
        if self.head.data == x:
             new_node=Node(data)
             new_node.ref=self.head
             self.head=new_node
             return
        n=self.head
        while n.ref is not None:
            if n.ref.data ==x:
                break
            n=n.ref
        if n.ref is None:
            print("Node is not present")
            
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def delete_begin(self):
        if self.head is None:
            print("LL is empty")
            
        else:
            self.head=self.head.ref

    def delete_end(self):
        if self.head is None:
            print("LL is Empty")
        #if only one node is presnet
        elif self.head.ref is None:
            self.head=None

        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref

            n.ref=None

    def delete_by_value(self,x):
        if self.head is None:
            print("LL is empty")
            return
        if x == self.head.data:
            self.head=self.head.ref
            return
        
        n=self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n=n.ref
        if n.ref is None:
            print("node is not present")
        else:
            n.ref=n.ref.ref
            

ll1=LinkedList()
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_begin(30)
ll1.add_end(80)
ll1.add_end(48)
ll1.add_after_node(40,20)
ll1.add_before_node(79,10)
ll1.delete_begin()
ll1.delete_end()
ll1.delete_by_value(80)
ll1.printLL()