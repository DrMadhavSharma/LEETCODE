class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return head
        count = 0
        temp = head
        while temp and count < k:
            temp = temp.next
            count += 1
        
        if count < k:
            return head
        curr=head
        forward=None
        prev=None
        c=0
        

        while curr and c < k:
            forward=curr.next
            curr.next=prev
            prev=curr
            curr=forward
            c+=1
            
        if(forward!=None):
            head.next=self.reverseKGroup(forward,k)
        
        return prev
            