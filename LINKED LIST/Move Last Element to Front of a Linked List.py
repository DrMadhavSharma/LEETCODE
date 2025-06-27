class Solution:
    def moveToFront(self, head : Optional['Node']) -> Optional['Node']:
       prev=None
       curr=head
       while curr and curr.next :
           prev=curr
           curr=curr.next
       curr.next=head
       head=curr
       prev.next=None
       return head
