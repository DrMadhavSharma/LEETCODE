class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        c=0
        while curr:
            c+=1
            curr=curr.next
        mid=(c//2)
        curr=head
        c=0
        while curr:
            if c==mid:
                return curr
            c+=1
            curr=curr.next