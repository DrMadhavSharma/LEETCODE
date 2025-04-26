class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        anshead=None
        anstail=None
        def insertAtTail(anshead,anstail,digit):
            temp=ListNode(digit)
            if anshead is None:
                anshead=temp
                anstail=temp
            else:
                anstail.next=temp
                anstail=temp
            return anshead,anstail
        def reversell(head):
            if head is None:
                return None
            curr=head
            forward=None
            prev=None
            while(curr):
                forward=curr.next
                curr.next=prev
                prev=curr
                curr=forward
            return prev
        head1 = l1
        head2 = l2

        carry=0
        while(head1 or head2 or carry):
            val1,val2=0,0
            if head1:
                val1=head1.val
            if head2:
                val2=head2.val
            sum_=carry+val1+val2
            digit=sum_%10
            anshead, anstail = insertAtTail(anshead, anstail, digit)
            carry=sum_//10
            if head1:
                head1=head1.next
            if head2:
                head2=head2.next
        return anshead