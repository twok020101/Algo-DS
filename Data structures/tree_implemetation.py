class Node:
    #Tree intialization
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    #inserting values in the tree(BST)
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right=(Node(data))
                else:
                    self.right.insert(data)
        else:
            self.data=data
    
    #Printing the tree
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    #Inorder Traversal
    #Left->Root->Right
    def inOrderTraversal(self,root):
        res=[]
        if root:
            res=self.inOrderTraversal(root.left)
            res.append(root.data)
            res+=self.inOrderTraversal(root.right)
        return res

    #preOrder Traversal
    #Root->Left->Right
    def preOrderTraversal(self,root):
        res=[]
        if root:
            res.append(root.data)
            res+=self.preOrderTraversal(root.left)
            res+=self.preOrderTraversal(root.right)
        return res
    
    #postOrder Traversal
    #Left->Right->Root
    def postOrderTraversal(self,root):
        res=[]
        if root:
            res=self.postOrderTraversal(root.left)
            res+=self.postOrderTraversal(root.right)
            res.append(root.data)
        return res


#driver code
if __name__=="__main__":
    t=Node(int(input("Enter initial value of Node: ")))
    numberOfValues=int(input("Enter number of inputs: "))
    for i in range(numberOfValues):
        t.insert(int(input()))

    t.printTree()
    print("InOrder Traversal:  \n",t.inOrderTraversal(t))
    print("PreOrder Traversal: \n",t.preOrderTraversal(t))
    print("PostOrder traversal: \n",t.postOrderTraversal(t))
