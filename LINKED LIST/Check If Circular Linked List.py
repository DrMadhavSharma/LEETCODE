#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


# your task is to complete this function
# function should return true/false or 1/0
class Solution:
    def isCircular(self, head):
        curr=head.next
        while curr:
            if curr.next==None:
                return False
            elif curr.next==head:
                return True
                break
            curr=curr.next
        return False