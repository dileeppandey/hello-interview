"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest
path from the root node down to the farthest leaf node.

Example:
    Tree:   3
           / \
          9  20
            /  \
           15   7
    Output: 3
"""


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # ------------------------------------------------------------------
        # RECURSIVE INSIGHT: The max depth of a tree is:
        #   1 + max(depth of left subtree, depth of right subtree)
        # This is a natural recursive problem — divide into subproblems
        # (left and right subtrees), combine results.
        # ------------------------------------------------------------------

        # Step 1: Base case — empty tree has depth 0
        if root is None:
            return 0

        # Step 2: Recursively compute depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Step 3: The depth of this tree is 1 (for current node) +
        #         the deeper of the two subtrees
        return 1 + max(left_depth, right_depth)


# ---- Quick verification ----
#     3
#    / \
#   9  20
#     /  \
#    15   7
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
s = Solution()
print(s.maxDepth(root))    # Expected: 3
print(s.maxDepth(None))    # Expected: 0
print(s.maxDepth(TreeNode(1)))  # Expected: 1
