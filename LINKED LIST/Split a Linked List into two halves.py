class Solution:
    def splitList(self, head):
        # If list is empty or has only one node, nothing to split
        if not head or head.next == head:
            return head, None  

        slow = head
        fast = head

        # Step 1: Use slow and fast pointers to find the middle of the circular list
        # Stop if fast is one step or two steps away from completing the loop
        # This helps identify the midpoint depending on odd/even number of nodes
        while fast.next != head and fast.next.next != head:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Start of the two halves
        head1 = head           # First half starts from original head
        head2 = slow.next      # Second half starts from node after slow

        # Step 3: Make first half circular
        slow.next = head1

        # Step 4: Handle odd-length lists
        # If the loop exited because fast.next.next == head,
        # it means there's an odd number of nodes and fast is not at the last node yet
        # So move fast one more step to reach the actual last node
        if fast.next.next == head:
            fast = fast.next

        # Step 5: Make second half circular
        fast.next = head2

        return head1, head2
