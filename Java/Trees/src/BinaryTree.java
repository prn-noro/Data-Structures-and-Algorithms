import java.util.LinkedList;
import java.util.Queue;

public class BinaryTree {

	Node root;
	
	public void insertEndHelper(Node currNode, Node newNode) {
		if(newNode.data <currNode.data) {
			if(currNode.left==null) {
				currNode.left=newNode;
			}
			else {
				insertEndHelper(currNode.left,newNode);
			}
		}
		else if(newNode.data >currNode.data) {
			if(currNode.right==null) {
				currNode.right=newNode;
			}
			else {
				insertEndHelper(currNode.right,newNode);
			}
		}
		else {
			System.out.println("Data Already Exists");
		}
	}
	
	public void insertEnd(int data) {
		Node newNode=new Node(data);
		if(root==null) {
			root=newNode;
		}
		else {
			insertEndHelper(root,newNode);
		}
	}
	
	public void inorderTraversal(Node currNode) {
		if(currNode == null) {
			return;
		}
		inorderTraversal(currNode.left);
		System.out.print(currNode.data+" ");
		inorderTraversal(currNode.right);
		
	}
	
	
	public void preorderTraversal(Node currNode) {
		if(currNode == null) {
			return;
		}
		System.out.print(currNode.data+" ");
		preorderTraversal(currNode.left);
		preorderTraversal(currNode.right);
		
	}
	
	
	public void postorderTraversal(Node currNode) {
		if(currNode == null) {
			return;
		}
		postorderTraversal(currNode.left);
		postorderTraversal(currNode.right);
		System.out.print(currNode.data+" ");
		
	}
	
	public void levelorderTraversal(Node currNode) {
		Queue<Node> myQueue = new LinkedList<Node>();
		
		myQueue.add(currNode);
		
		while(myQueue.size()>0) {
			Node temp=myQueue.remove();
			System.out.print(temp.data+" ");
			
			if(temp.left!=null) {
				myQueue.add(temp.left);
			}
			if(temp.right!=null) {
				myQueue.add(temp.right);
			}
			
		}
		
	}
	

	
//	public void verticalorderTraversal(Node currNode){
//		HashMap<Integer,Array> myMap=new HashMap<Integer,Array>();
//	}
	
	public void traversal(String s) {
		if(root == null) {
			System.out.println("Empty Tree");
			return;
		}
		else {
			if(s=="inorder") {
				inorderTraversal(root);
			}
			else if(s=="preorder") {
				preorderTraversal(root);
			}
			else if(s=="postorder") {
				postorderTraversal(root);
			}
			else if(s=="levelorder") {
				levelorderTraversal(root);
			}
//			else if(s=="verticalorder") {
//				verticalorderTraversal(root);
//			}
			else{
				System.out.println("Non Existant");
			}
		}
	}
	
	public void countLeaf() {
		System.out.println(getLeafCount(root)); 
	}
	
	public int getLeafCount(Node currNode) {
		if(currNode==null) {
			return 0;
		}
		else if(currNode.left==null && currNode.right==null) {
			return 1;
		}
		else {
			return getLeafCount(currNode.left)+getLeafCount(currNode.right);
		}
	}
	
//	public void printLeaf() {
//		printLeafNode(root); 
//	}
	
	public void leftView(Node currNode) {
		if(currNode==null) {
			return;
		}
		Queue<Node> myQueue=new LinkedList<Node>();
		
		myQueue.add(currNode);
		myQueue.add(null);
		while(myQueue.size()>0) {
			Node temp=myQueue.peek();
			
			if(temp!=null) {
				System.out.println(temp.data);
				while(myQueue.peek()!=null) {
					
					Node myTemp=myQueue.peek();
					
					if(myTemp.left!=null) {
						myQueue.add(myTemp.left);
					}
					
					if(myTemp.right!=null) {
						myQueue.add(myTemp.right);
					}
					
					myQueue.remove();
					
				}
				myQueue.add(null);
				
			}
			myQueue.remove();
			
		}
		
	}
	
	public void printLeafNode(Node currNode) {
		if(currNode==null){
			return;
		}
		if(currNode.left==null && currNode.right==null) {
			System.out.println(currNode.data); 
		}
		printLeafNode(currNode.left);
		printLeafNode(currNode.right);
	}

}
