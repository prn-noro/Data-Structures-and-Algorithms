#Done Implement LinkedList
#Done Insert Start
#Done Insert End
#Done Find Middle
#Done Has Cycle
#Done Insert At Position 
#Done View List
#Done Delete Node
#Done Nth Node From End
#Done Delete Duplicates
#Done Reverse List
#Done Compare LinkedList
#Done Half Merge Two Sorted Lists



class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.start=None

    def insertEnd(self,data):
        new_node=Node(data)
        if self.start==None:
            self.start=new_node
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=new_node

    def findMiddle(self):
        if self.start==None:
            print("List is empty")
        else:
            tortoise=self.start
            hare=self.start

            while(hare!=None and hare.next!=None):
                hare=hare.next.next
                tortoise=tortoise.next

        print("Middle element is ",tortoise.data)
    
    def insertHead(self,data):
        new_node=Node(data)
        if self.start==None:
            self.start=new_node
        else:
            new_node.next=self.start
            self.start=new_node

    def has_cycle(self):
        slow=self.start
        fast=self.start
        flag=0
        while slow!=None and fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                flag=1
                break
        if flag==1:
            print('Cycle')
        else:
            print('No Cycle')
        
    def insertAtPosition(self,data,position):
        new_node=Node(data)
        count=0
        temp=self.start
        while temp.next!=None:
            if count==position-1:
                temporary=temp.next
                temp.next=new_node
                new_node.next=temporary
                break
            count=count+1
            temp=temp.next

    def deleteAtPosition(self,position):
        count=0
        temp=self.start
        while temp.next!=None:
            if count==position-1:
                temp.next=temp.next.next
            count=count+1
            temp=temp.next

    def viewList(self):
        if self.start==None:
            print("Linked List is Empty")
        else:
            temp=self.start
            while temp.next!=None:
                print(temp.data)
                temp=temp.next
            print(temp.data)
    def reverse(self,linkList):
        current=linkList.start
        following=current.next
        prev=None

        while current!=None:
            current.next=prev
            prev=current
            current=following
            if following!=None:
                following=following.next
        linkList.start=prev

    def compare(self,linkList2):
        start1=self.start
        start2=linkList2.start
        count1=0
        flag=0
        # count2=0
        while start1!=None and start2!=None:
            if start1.data==start2.data:
                count1=count1+1
                start1=start1.next
                start2=start2.next
            else:
                flag=1
                break
        if flag==0:
            print('Same')
        else:
            print('Not same')
    
    def deleteDuplicate(self):
        ptr=self.start
        while ptr.next!=None:
            if ptr.data==ptr.next.data:
                # print(ptr.data)
                while ptr.data==ptr.next.data:
                    if ptr.next.next==None:
                        ptr.next=None
                    else:
                        ptr.next=ptr.next.next

            # if ptr.next

            ptr=ptr.next
    

linkList1=LinkedList()
linkList2=LinkedList()
# linkList1.insertHead(50)
# linkList1.insertHead(20)
# linkList1.insertEnd(10)
# linkList1.insertAtPosition(60,2)
# linkList2.insertHead(50)
# linkList2.insertHead(20)
# linkList2.insertEnd(10)
# linkList2.insertAtPosition(60,2)
# linkList.insertAtPosition(20,1)
# linkList.deleteAtPosition(3)
# linkList.deleteAtPosition(1)
# print('Before Reverse')
# linkList.viewList()
# print('After Reverse')
# linkList.reverse(linkList)
linkList1.insertEnd(10)
linkList1.insertEnd(20)
linkList1.insertEnd(20)
linkList1.insertEnd(30)
linkList1.insertEnd(30)
linkList1.insertEnd(30)
linkList1.insertEnd(30)
linkList1.insertEnd(40)
# linkList1.insertEnd(40)

linkList1.deleteDuplicate()
linkList1.viewList()
# linkList2.viewList()
# linkList1.compare(linkList2)
