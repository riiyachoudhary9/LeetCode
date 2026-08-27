class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove nth node from the end
        slow.next = slow.next.next

        return dummy.next
        