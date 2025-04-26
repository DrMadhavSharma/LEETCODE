class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next==None:
            return True

        def FindMid(head):
            slow=head
            fast=head
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            return slow
        def reversell(head):
            curr=head
            forward=None
            prev=None
            while curr:
                forward=curr.next
                curr.next=prev
                prev=curr
                curr=forward
            return prev
        mid=FindMid(head)
        temp=reversell(mid)
        head1=head
        head2=temp
        while head2!=None:
            if head1.val!=head2.val:
                return False  
            head1=head1.next
            head2=head2.next
        return True 

