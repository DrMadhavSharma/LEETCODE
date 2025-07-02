''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def addTwoLists(self, num1, num2):
        def reverse(head):
            prev=None
            curr=head
            while curr:
                forward=curr.next
                curr.next=prev
                prev=curr
                curr=forward
            return prev
        carry=0
        f=reverse(num1)
        se=reverse(num2)
        dummy=Node(0)
        tail=dummy
        while f and se:
            s=f.data+se.data+carry
            temp=Node(0)
            temp.data=s%10
            carry=s//10
            tail.next=temp
            tail=temp
            f=f.next
            se=se.next
        while f:
            s=f.data+carry
            temp=Node(0)
            temp.data=s%10
            carry=s//10
            tail.next=temp
            tail=temp
            f=f.next
        while se:
            s=se.data+carry
            temp=Node(0)
            temp.data=s%10
            carry=s//10
            tail.next=temp
            tail=temp
            se=se.next
        if carry:
            tail.next=Node(carry)
        
        
        
        result = reverse(dummy.next)

        # Edge case: if the most significant digit is 0 and not the only digit
        if result.data == 0 and result.next:
            result = result.next
        
        return result

        
            
            
            