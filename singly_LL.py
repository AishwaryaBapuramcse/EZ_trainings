'''
class node:
    def __init__(self,data):
        self.value=data
        self.next=None
Head=node(10)
Head.next=node(20)
Head.next.next=node(30)

or
'''

class node:
    def __init__(self,data):
        self.value=data
        self.next=None
Head=tail=node(10)

tail.next=node(20)
tail=tail.next

tail.next=node(30)
tail=tail.next

tail.next=node(40)
tail=tail.next

# print(Head)
# print(tail)
# print(Head.next.next.next)
def print_link_list(Head):
    if Head==None:
        print("list is empty")
        return
    curr=Head
    while curr!=None:
        print(curr.value)
        curr=curr.next
print_link_list(Head)        



