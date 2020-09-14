import java.util.*;
public class MyLinkedList {

	Node head;
	
//	public void mergeList(MyLinkedList l2) {
//		Node ptr1=this.head;
//		Node ptr2=l2.head;
//		MyLinkedList l3=new MyLinkedList();
//		Node ptr3=l3.head;
//		ptr3.data=0;
//		
//		while(ptr1!=null && ptr2!=null) {
//			if(ptr1.data<=ptr2.data) {
//				ptr3.next=ptr1;
//				ptr3=ptr3.next;
//				ptr1=ptr1.next;
//			}
//			else {
//				ptr3.next=ptr2;
//				ptr3=ptr3.next;
//				ptr2=ptr2.next;
//			}
//		}
//		if(ptr1==null && ptr2!=null) {
//			while(ptr2!=null) {
//				ptr3.next=ptr2;
//				ptr3=ptr3.next;
//				ptr2=ptr2.next;
//			}
//		}
////		
//		if(ptr1!=null && ptr2==null) {
//			while(ptr1!=null) {
//				ptr3.next=ptr1;
//				ptr3=ptr3.next;
//				ptr1=ptr1.next;
//			}
//		}
//	}
	
	public void reverseList() {
		Node current=this.head;
		Node following=current.next;
		Node prev=null;
		
		while(current!=null) {
			current.next=prev;
			prev=current;
			current=following;
			if (following!=null) {
				following=following.next;
			}
			else {
				break;
			}
			head=current;
		}
	}
	
	public void compareList(MyLinkedList l2) {
		Node l1Ptr=this.head;
		Node l2Ptr=l2.head;
		while(l1Ptr!=null && l2Ptr!=null) {
			if(l1Ptr.data==l2Ptr.data) {
				l1Ptr=l1Ptr.next;
				l2Ptr=l2Ptr.next;
				continue;
			}
			else {
				System.out.println("Linked Lists Are Different");
				return;
			}
		}
		if (((l1Ptr==null)&&l2Ptr!=null)||(l1Ptr!=null &&l2Ptr==null)){
			System.out.println("Linked Lists Are Different");
			return;
		}
		else {
			System.out.println("Same Linked Lists");
		}
	}
	
	public void removeDuplicates() {
		Node ptr=head;
		Node prevPtr=head;
		HashSet<Integer> mySet = new HashSet<Integer>();
		while(ptr!=null) {
			if(!mySet.contains(ptr.data)) {
				mySet.add(ptr.data);
				prevPtr=ptr;
				ptr=ptr.next;
			}
			else {
				prevPtr.next=ptr.next;
				ptr=ptr.next;
			}
		}
	}
	
	public void insertEnd(int data) {
		Node myNode=new Node();
		myNode.data=data;
		myNode.next=null;
		
		if(head==null) {
			head=myNode;
		}
		else {
			Node ptr=head;
			
			while(ptr.next!=null) {
				ptr=ptr.next;
			}
			ptr.next=myNode;
		}
	}
	
	public void deleteNode(int data) {
		Node ptr=head;
		Node prevptr=head;
		if(ptr==null) {
			System.out.println("No Data In LinkedList");
		}
		else{
			if (head.data==data) {
				head=head.next;
			}
			while(ptr.next!=null) {
				if(ptr.data==data) {
					prevptr.next=ptr.next;
					return;
				}
				prevptr=ptr;
				ptr=ptr.next;
			}
			System.out.println("No Such Data");
			
		}
	}
	
	public void insertPosition(int position,int data) {
		Node myNode=new Node();
		myNode.data=data;
		myNode.next=null;
		int count=0;
		if(head==null) {
			head=myNode;
		}
		else{
			Node ptr=head;
			Node prevptr=head;
			while(count!=position) {
				prevptr=ptr;
				ptr=ptr.next;
				count+=1;
			}
			prevptr.next=myNode;
			myNode.next=ptr;
		}	
	}
	
	public void insertStart(int data) {
		Node myNode=new Node();
		myNode.data=data;
		myNode.next=null;
		
		if(head==null) {
			head=myNode;
		}
		else {
			myNode.next=head;
			head=myNode;
		}
	}
	
	public void detectLoop() 
    { 
        Node slow_p = head, fast_p = head; 
        int flag = 0; 
        while (slow_p != null && fast_p != null && fast_p.next != null) { 
            slow_p = slow_p.next; 
            fast_p = fast_p.next.next; 
            if (slow_p == fast_p) { 
                flag = 1; 
                break; 
            } 
        } 
        if (flag == 1) 
            System.out.println("Loop found"); 
        else
            System.out.println("Loop not found"); 
    } 
	
	public void findFromEnd(int position) {
		if(head==null) {
			return;
		}
		else {
			int count=0;
			Node ptr=head;
			Node myPtr=head;
			
			while(ptr!=null) {
				if (count==position) {
					break;
				}
				ptr=ptr.next;
				count+=1;
			}
			
			while(ptr!=null) {
				ptr=ptr.next;
				myPtr=myPtr.next;
			}
			System.out.println(position+"th data from end is "+myPtr.data);
		}
	}
	
	public void findMiddle() {
		Node slowPtr=head;
		Node fastPtr=head;
		while(fastPtr.next!=null && fastPtr.next.next!=null) {
			slowPtr=slowPtr.next;
			fastPtr=fastPtr.next.next;
		}
		System.out.println("Middle Element is "+slowPtr.data);
	}
	
	public void show() {
		Node ptr=head;
		while(ptr.next!=null) {
			System.out.println(ptr.data);
			ptr=ptr.next;
		}
		System.out.println(ptr.data);
	}
	
	
}
