"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its
nodes' values (i.e., from left to right, level by level).

Example:
    Tree:   3
           / \
          9  20
            /  \
           15   7
    Output: [[3], [9, 20], [15, 7]]
"""
from collections import deque


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        # ------------------------------------------------------------------
        # BFS INSIGHT: Level order traversal IS BFS on a tree. Use a queue.
        # The trick is to process nodes one level at a time by tracking the
        # queue size at the start of each level.
        # ------------------------------------------------------------------

        if not root:
            return []

        result = []
        queue = deque([root])

        # Step 1: Process the tree level by level
        while queue:
            level_size = len(queue)  # Number of nodes at this level
            level_values = []

            # Step 2: Process all nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)

                # Step 3: Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Step 4: Add this level's values to the result
            result.append(level_values)

        return result


# ---- Quick verification ----
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
s = Solution()
print(s.levelOrder(root))    # Expected: [[3], [9, 20], [15, 7]]
print(s.levelOrder(None))    # Expected: []
print(s.levelOrder(TreeNode(1)))  # Expected: [[1]]
