class Solution:
    def reverseDLL(self, head):
        #return head of reverse doubly linked list
        curr=head
        forward=None
        Prev=None
        while curr:
                forward=curr.next
                curr.next=curr.prev
                curr.prev=forward
                Prev=curr
                curr=forward
        return Prev