class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=list1
        curr2=list2
        dummy=ListNode(-1)
        tail=dummy
        while curr1 and curr2:
            if curr1.val<=curr2.val:
                tail.next=curr1
                curr1=curr1.next
                tail=tail.next
            else:
                tail.next=curr2
                curr2=curr2.next
                tail=tail.next
        tail.next = curr1 if curr1 else curr2
        return(dummy.next)
                