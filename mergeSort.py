class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        def findmid(head):
            slow=head
            fast=head
            prev=None
            while(fast and fast.next):
                prev=slow
                slow=slow.next
                fast=fast.next.next
            return prev
        def merge(left,right):
            if left==None:
                return right
            if right==None:
                return left
            
            solnnode=Node(-1)
            solntail=solnnode
            
            while (left!=None and right!=None):
                if left.data<=right.data:
                    solntail.next=left
                    solntail=left
                    left=left.next
                else:
                    solntail.next=right
                    solntail=right
                    right=right.next
            
            while (left!=None):
                solntail.next=left
                solntail=left
                left=left.next
            
            while (right!=None):
                solntail.next=right
                solntail=right
                right=right.next
                
            return solnnode.next
        if head==None or head.next==None:
            return head
        mid=findmid(head)
        left=head
        right=mid.next
        mid.next=None
        
        left=self.mergeSort(left)
        right=self.mergeSort(right)
        
        result=merge(left,right)
        
        return result
        
