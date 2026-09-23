class Solution:
    def pairSum(self, head):
        # Find start of second half
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None

        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Compare both halves
        ans = 0
        left = head
        right = prev

        while right:
            ans = max(ans, left.val + right.val)
            left = left.next
            right = right.next

        return ans