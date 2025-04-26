class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        prev=None
        seen=set()
        while curr:
            if curr.val not in seen:
                seen.add(curr.val)
                prev=curr
            else:
                prev.next=curr.next
            curr=curr.next
        return head