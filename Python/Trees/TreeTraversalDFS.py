class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)

    def inorder(self,start,traversal_string):
        if start!=None:
            traversal_string=self.inorder(start.left,traversal_string)
            traversal_string=str(start.data)+'-'
            traversal_string=self.inorder(start.right,traversal_string)
        
        return traversal_string

    def preorder(self,start,traversal_string):
        if start!=None:
            traversal_string+=str(start.data)+'-'
            traversal_string=self.preorder(start.left,traversal_string)
            traversal_string=self.preorder(start.right,traversal_string)
        
        return traversal_string

    def postorder(self,start,traversal_string):
        if start!=None:
            traversal_string=self.postorder(start.left,traversal_string)
            traversal_string=self.postorder(start.right,traversal_string)
            traversal_string+=str(start.data)+'-'
        
        return traversal_string

    def countLeaf(self,curr_node):
        if (curr_node == None):
            return 0
        if curr_node.left == None and curr_node.right == None:
            return 1
        else:
            return self.countLeaf(curr_node.left)+self.countLeaf(curr_node.right)

    def print_tree(self,method):
        print(method)
        if method=='inorder':
            return self.inorder(self.root,'')
        elif method=='preorder':
            return self.preorder(self.root,'')
        elif method=='postorder':
            return self.postorder(self.root,'')
        else:
            print('No method')

tree=BinaryTree(1)

tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)
print(tree.print_tree('inorder'))
print(tree.print_tree('preorder'))
print(tree.print_tree('postorder'))
