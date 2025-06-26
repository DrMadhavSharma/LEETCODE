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
    #second soln
def removeDuplicates(head):
    prev=None
    curr=head
    while curr:
        forward=curr.next
        if prev is None:
            prev=curr
            curr=forward
            continue
        if curr.data==prev.data:# if two nodes are duplicate then remove it 
            prev.next=forward
            curr=forward
        else:          #if two nodes are not duplicate advance forward
            prev=curr
            curr=forward