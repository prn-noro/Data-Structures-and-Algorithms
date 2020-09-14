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

 
    def getVerticalOrder(self,root,myDict,horiDist):

        if root==None:
            return

        if horiDist not in myDict:
            myDict[horiDist]=[root.data]

        else:
            myDict[horiDist].append(root.data)

        self.getVerticalOrder(root.left,myDict,horiDist-1)
        self.getVerticalOrder(root.right,myDict,horiDist+1)


    def verticalOrder(self,root):
        myDict={}

        horiDist=0

        self.getVerticalOrder(root,myDict,horiDist)

        print(myDict)
        for key,value in enumerate(sorted(myDict)):
            for i in myDict[value]:
                print(i,end=" ")
            print()

    

    def getBottom(self,root,horiDist,level,myDict):
        if root==None:
            return

        if horiDist not in myDict:
            myDict[horiDist]=[root.data,level]

        else:
            if level>=myDict[horiDist][1]:
                myDict[horiDist]=[root.data,level]

        self.getBottom(root.left,horiDist-1,level+1,myDict)
        self.getBottom(root.right,horiDist+1,level+1,myDict)


    def bottomView(self,root):

        myDict={}

        # horiDist=0

        self.getBottom(root,0,0,myDict)

        for key in sorted(myDict.keys()):
            print(myDict[key][0],end=" ")






    
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

# tree.leftView(tree.root)
# tree.verticalOrder(tree.root)
tree.bottomView(tree.root)
# print(string)