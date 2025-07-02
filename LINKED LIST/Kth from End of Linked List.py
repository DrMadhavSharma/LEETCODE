'''
	A linked list node has the following structure
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
#Function to find the data of kth node from the end of a linked list
class Solution:
    def getKthFromLast(self, head, k):
        def reverse(head):
            prev=None
            curr=head
            while curr:
                forward=curr.next
                curr.next=prev
                prev=curr
                curr=forward
            return prev
        n_head=reverse(head)
        curr=n_head
        c=0
        while curr:
            c+=1
            curr=curr.next
        curr=n_head
        if k<=c:
            for _  in range(k-1):
                curr=curr.next
            return curr.data
        else:
            return -1
            