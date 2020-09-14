class Node:

    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:

    def __init__(self):
        self.root=None
    
    def insert(self,data):
        new_node=Node(data)
        if self.root==None:
            self.root=new_node
        else:
            self.insert_(data,self.root,new_node)
    
    def insert_(self,data,curr_node,new_node):
        if data<curr_node.data:
            if curr_node.left==None:
                curr_node.left=new_node
            else:
                self.insert_(data,curr_node.left,new_node)
        elif data>curr_node.data:
             if curr_node.right==None:
                 curr_node.right=new_node
             else:
                self.insert_(data,curr_node.right,new_node)
        else:
            print("Data Already Exists")
            
    def inorderTraversal(self,start,string):
        if start!=None:
            string=self.inorderTraversal(start.left,string)
            string=str(start.data)+"-"
            string=self.inorderTraversal(start.right,string)

        return string

    def levelorder(self,start):
        if start==None:
            return

        myQueue=[]
        myQueue.append(start)

        while len(myQueue)>0:
            print("Data = ",myQueue[0].data)

            node=myQueue.pop(0)

            if node.left:
                myQueue.append(node.left)
            if node.right:
                myQueue.append(node.right)

    def printTree(self,method):
        if method=='inorder':
            self.inorderTraversal(self.root," ")
        elif method=="levelorder":
            self.levelorder(self.root)


    def leftView(self,start):

        if start==None:
            return

        myQueue=[]
        myQueue.append(start)
        myQueue.append(None)

        while len(myQueue)>0:

            temp=myQueue[0]

            if temp:
                print(temp.data)

                while myQueue[0]!=None:

                    myTemp=myQueue[0]

                    if myTemp.left:
                        myQueue.append(myTemp.left)

                    if myTemp.right:
                        myQueue.append(myTemp.right)

                    myQueue.pop(0)

                myQueue.append(None)

            myQueue.pop(0)





    
tree=Tree()
tree.insert(10)
tree.insert(5)
tree.insert(30)
tree.insert(2)
tree.insert(6)
tree.insert(23)
tree.insert(21)
tree.insert(35)

# tree.printTree('levelorder')

tree.leftView(tree.root)

# print(string)