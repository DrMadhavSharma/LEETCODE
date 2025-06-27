class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        s=set()
        prev=None
        curr=head
        while curr:
            forward=curr.next
            if prev is None:
                prev=curr
                s.add(curr.data)
                curr=forward
                continue
            if (curr.data)  in s:
                prev.next=forward
                curr=forward
            else:
                s.add(curr.data)
                prev=curr
                curr=forward
        return head