
public class ImplementTree {
	
//	Implement Tree
//	Insert Data
//	Inorder,Preorder,Postorder
//	LevelOrder
//	Count Leaf
//	Print Leaf

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		BinaryTree myTree = new BinaryTree();
		myTree.insertEnd(10);
		myTree.insertEnd(5);
		myTree.insertEnd(15);
		myTree.insertEnd(2);
		myTree.insertEnd(6);
		myTree.insertEnd(12);
		myTree.insertEnd(30);
//		myTree.traversal("inorder");
//		myTree.countLeaf();
//		myTree.printLeafNode(myTree.root);
		myTree.leftView(myTree.root);
	}

}

