class Node:
    def __init__(self,data):
        self.data=data
        self.pref=None
        self.nref=None

class DoublyLinkedlist:
    def __init__(self):
        self.head=None

    #traversing a forward
    def printLL(self):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            n=self.head
            while n is not None:
                print(n.data ,"-->" ,end=" ")
                n=n.nref

    #traversing backward
    def printrev(self):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data ,"-->" ,end=" ")
                n=n.pref

    #insert at empty LL
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("linked list is not empty")

    #insert at begining 
    def add_begin(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node

        else:
            new_node=Node(data)
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
    
    #insert at end
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref

            n.nref=new_node
            new_node.pref=n
    
    #insert after the node
    def add_after_node(self,data,x):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            n=self.head
        while n is not None:
            if n.data == x:
                break
            n=n.nref
        if n is None:
            print("The node is not present")
        else:
            new_node=Node(data)
            new_node.nref=n.nref
            new_node.pref=n
            if n.nref is not None:
                n.nref.pref=new_node
            n.nref=new_node

    #insert at before the node
    def add_before_node(self,data,x):
        if self.head is None:
            print("Linked List is Empty!")
        else:
            n=self.head
        while n is not None:
            if n.data == x:
                break
            n=n.nref
        if n is None:
            print("The node is not present")
        else:
            new_node=Node(data)
            new_node.nref=n
            new_node.pref=n.pref
            if n.pref is not None:
                n.nref.pref=new_node
            else:
                self.head=new_node
            n.pref=new_node
    
    #delete at beginning
    def delete_begin(self):
        if self.head is None:
            print("LL is empty")
            return
        elif self.head.nref is None:
            self.head=None
            
        else:
            self.head=self.head.nref
            self.head.pref=None

    #delete at end
    def delete_end(self):
        if self.head is None:
            print("LL is Empty")

        if self.head.nref is None:
            self.head=None

        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None

    #delete by values
    def delete_value(self,x):
        if self.head is None:
            print("LL is Empty")
            return
        if self.head.nref is None: #delete head values
            if self.head.data==x:
                self.head=None
            else:
                print("the node is not present")
            return
        if self.head.data == x: #if delete 1st value
            self.head=self.head.nref
            self.head.pref=None
            return
        n=self.head
        while n.nref is not None:
            if x==n.data:
                break
            n=n.nref

        if n.nref is not None:
            n.nref.pref=n.pref
            n.pref.nref=n.nref
        else:
            if n.data==x:
                n.pref.nref=None
            else:
                print("x is not present")
    

        


        

    

    



ll1=DoublyLinkedlist()

ll1.insert_empty(10)
ll1.add_begin(110)
ll1.add_end(50)
ll1.add_after_node(51,50)
ll1.add_end(90)
ll1.add_end(88)
ll1.add_before_node(111,110)
ll1.add_end(89)
ll1.delete_begin()
ll1.delete_end()
ll1.printLL()
#ll1.printrev()



            