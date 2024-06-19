class node:
    def __init__(self,data):
        self.value=data
        self.next=None
    
class LL:    
    def __init__(self):
        self.Head=None

    def insert_at_front(self,data):
        new_node=node(data)
        new_node.next=self.Head
        self.Head=new_node

    def insert_at_end(self,data):
        new_node=node(data)
        n=self.Head
        while n.next is not None:
            n=n.next
        n.next=new_node 

    def display(self):
        if self.Head==None:
            print("list is empty")
        else:    
            n=self.Head   
            while n is not None:
                print(n.value)
                n=n.next

l=LL()
l.insert_at_front(20)
l.insert_at_end(30)
l.display()

'''class Node:
    def _init_(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def _init_(self):
        self.head=None

    def traverse(self):
        if self.head==None:
            print("Linked List is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,end=" ")
                n=n.ref

    def add_begin(self,data):
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node

    def add_end(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:    
                n=n.ref
            n.ref=new_node

    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if n.data==x:
                break
            else:
                n=n.ref
        if n is None:
            print("Node is not present in LL")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def add_before(self,data,x):
        if self.head is None:
            print("LL is empty")
            return
        if self.head==x:
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            else:
                n=n.ref
        if n is None:
            print("Node is not present in LL")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node

    def del_begin(self):
        if self.head is None:
            print("LL is empty")
        else:
            self.head=self.head.ref

    def del_end(self):
        if self.head is None:
            print("LL is empty")
        elif self.head.ref==None:
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None

    def del_value(self,x):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.data==x:
            self.head=None
            return
        else:
            n=self.head
            while n.ref.ref is not None:
                if n.ref.data==x:
                    break
                n=n.ref
            if n.ref is None:
                print("Node not found")
            else:
                n.ref=n.ref.ref


LL=LinkedList()
LL.add_begin(20)
LL.add_begin(10)
LL.add_end(30)
LL.traverse()'''


