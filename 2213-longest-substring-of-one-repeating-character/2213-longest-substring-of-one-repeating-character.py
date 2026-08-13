from typing import List


class SegmentTree:
    def __init__(self, s: str):
        self.s = list(s)
        self.n = len(s)

        # Each node stores:
        # left  = longest same-character prefix
        # right = longest same-character suffix
        # best  = longest same-character substring
        self.left = [0] * (4 * self.n)
        self.right = [0] * (4 * self.n)
        self.best = [0] * (4 * self.n)

        self.build(1, 0, self.n - 1)

    def build(self, node: int, l: int, r: int):
        if l == r:
            self.left[node] = 1
            self.right[node] = 1
            self.best[node] = 1
            return

        mid = (l + r) // 2

        self.build(node * 2, l, mid)
        self.build(node * 2 + 1, mid + 1, r)

        self.pull(node, l, r)

    def pull(self, node: int, l: int, r: int):
        left_node = node * 2
        right_node = node * 2 + 1
        mid = (l + r) // 2

        self.left[node] = self.left[left_node]
        self.right[node] = self.right[right_node]

        self.best[node] = max(
            self.best[left_node],
            self.best[right_node]
        )

        # If the boundary characters are equal,
        # the suffix of the left part and prefix of
        # the right part can be joined.
        if self.s[mid] == self.s[mid + 1]:

            left_len = mid - l + 1
            right_len = r - mid

            if self.left[left_node] == left_len:
                self.left[node] += self.left[right_node]

            if self.right[right_node] == right_len:
                self.right[node] += self.right[left_node]

            self.best[node] = max(
                self.best[node],
                self.right[left_node] + self.left[right_node]
            )

    def update(self, node: int, l: int, r: int, index: int, char: str):
        if l == r:
            self.s[index] = char
            self.left[node] = 1
            self.right[node] = 1
            self.best[node] = 1
            return

        mid = (l + r) // 2

        if index <= mid:
            self.update(node * 2, l, mid, index, char)
        else:
            self.update(node * 2 + 1, mid + 1, r, index, char)

        self.pull(node, l, r)


class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        tree = SegmentTree(s)
        answer = []

        for i in range(len(queryIndices)):
            index = queryIndices[i]
            char = queryCharacters[i]

            tree.update(
                1,
                0,
                len(s) - 1,
                index,
                char
            )

            answer.append(tree.best[1])

        return answer