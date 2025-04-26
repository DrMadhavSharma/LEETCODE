class Solution:
    def reverseList(self, head):
        # Code here
        curr=head
        forward=None
        prev=None
        while curr:
            forward=curr.next
            curr.next=prev
            prev=curr
            curr=forward
        return prev
