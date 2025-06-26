class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Loop detected This works due to the properties of cycle length and distance from head to loop start.
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                # Now, slow (and fast) is at the start of the loop
                ptr = fast
                while ptr.next != slow:
                    ptr = ptr.next
                ptr.next = None  # Break the loop
                break

