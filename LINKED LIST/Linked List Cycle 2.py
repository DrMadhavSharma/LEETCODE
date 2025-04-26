class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        slow = head
        fast = head

        # Detect cycle and get meeting point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Found cycle, now find entry point
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow  # Entry point of the cycle

        return None  # No cycle
