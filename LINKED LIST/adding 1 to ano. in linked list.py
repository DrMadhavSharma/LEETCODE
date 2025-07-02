'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self,head):
        def reverse(head):
            curr=head
            prev=None
            while curr:
                forward=curr.next
                curr.next=prev
                prev=curr
                curr=forward
            return prev
        carry=1
        head=reverse(head)
        temp=head
        while temp:
            if ((temp.data)+carry)%10==0:
                temp.data=0
                carry=1
            else:
                temp.data=(temp.data)+carry
                carry=0
            temp=temp.next
        head=reverse(head)
        if carry==1:
            n_Node=Node(carry)
            n_Node.next=head
            return n_Node
        return head
                