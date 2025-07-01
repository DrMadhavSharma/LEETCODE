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
#Tortoise and hare 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        return slow
        