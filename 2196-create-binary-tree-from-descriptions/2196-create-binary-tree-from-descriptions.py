from typing import List, Optional

class Solution:
    def createBinaryTree(
        self,
        descriptions: List[List[int]]
    ) -> Optional["TreeNode"]:

        nodes = {}
        children = set()

        for parent, child, isLeft in descriptions:

            if parent not in nodes:
                nodes[parent] = TreeNode(parent)

            if child not in nodes:
                nodes[child] = TreeNode(child)

            if isLeft == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

            children.add(child)

        # Root = node that is never a child
        for value in nodes:
            if value not in children:
                return nodes[value]

        return None