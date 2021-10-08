class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self,data):
        if self.key == data:
            print("Node is Found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present")

    def preorder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key ,end=" ")
        if self.rchild:
            self.rchild.preorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key , end=" ")

    def delete(self,data,current):
        if self.key is None:
            print("Tree is Empty!")
            return

        if data < self.key:
            if self.lchild:
                self.lchild=self.lchild.delete(data,current)
            else:
                print("given node is not present")

        elif data > self.key:
            if self.rchild:
                self.rchild=self.rchild.delete(data,current)
            else:
                print("given node is not present")
        else:
            if self.lchild is None:
                temp=self.rchild
                if data == current:
                    self.lchild = temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                temp=self.rchild
                if data == current:
                    self.lchild = temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                self=None
                return temp
            node= self.rchild
            while node.lchild:
                node =node.lchild
            self.key = node.key
            self.rchild =self.rchild.delete(node.key,current)
        return

    def min_node(self):
        pre = self
        while pre.lchild:
            pre = pre.lchild
        print("nOde with smallest key:",pre.key)
    
    def max_node(self):
        pre = self
        while pre.rchild:
            pre = pre.rchild
        print("nOde with largest key:",pre.key)

def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)
            
            


        
        
    


root=BST(10)
list1=[20,60,89,78,70,88,27,199]
for i in list1:
    root.insert(i)

root.search(7)
#root.preorder()
#root.postorder()
print("Inorder")
root.inorder()
print()
# print(count(root))
# if count(root)>1:
#     root.delete(10,90)
# else:
#     print("cant perform")

# print("After deletion")
# root.inorder()
root.min_node()
root.max_node()
