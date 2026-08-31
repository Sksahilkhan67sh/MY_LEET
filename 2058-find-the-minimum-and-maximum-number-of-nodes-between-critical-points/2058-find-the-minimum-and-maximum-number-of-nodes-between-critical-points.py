from typing import List, Optional

class Solution:
    def nodesBetweenCriticalPoints(
        self,
        head: Optional["ListNode"]
    ) -> List[int]:

        if head is None or head.next is None or head.next.next is None:
            return [-1, -1]

        prev = head
        curr = head.next

        index = 1

        first = -1
        last = -1
        min_dist = float("inf")

        while curr.next is not None:
            # Local maximum OR local minimum
            if (
                (curr.val > prev.val and curr.val > curr.next.val)
                or
                (curr.val < prev.val and curr.val < curr.next.val)
            ):
                if first == -1:
                    first = index
                    last = index
                else:
                    min_dist = min(min_dist, index - last)
                    last = index

            prev = curr
            curr = curr.next
            index += 1

        # Fewer than 2 critical points
        if first == last:
            return [-1, -1]

        max_dist = last - first

        return [min_dist, max_dist]