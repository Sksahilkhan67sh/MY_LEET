from typing import List


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.index = -1
        self.length = float("inf")


class Solution:
    def stringIndices(
        self,
        wordsContainer: List[str],
        wordsQuery: List[str]
    ) -> List[int]:

        root = TrieNode()

        # Insert container words in reverse
        for i, word in enumerate(wordsContainer):
            node = root

            # Update root for the empty suffix
            if len(word) < root.length:
                root.length = len(word)
                root.index = i

            for ch in reversed(word):
                idx = ord(ch) - ord('a')

                if node.children[idx] is None:
                    node.children[idx] = TrieNode()

                node = node.children[idx]

                # Shortest word wins.
                # If same length, earlier index wins automatically
                # because we process indices from left to right.
                if len(word) < node.length:
                    node.length = len(word)
                    node.index = i

        ans = []

        # Query in reverse
        for word in wordsQuery:
            node = root

            for ch in reversed(word):
                idx = ord(ch) - ord('a')

                if node.children[idx] is None:
                    break

                node = node.children[idx]

            ans.append(node.index)

        return ans