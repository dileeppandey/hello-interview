from trees.tree import Tree
from trees.tree_node import TreeNode

class BinaryTree(Tree):

    def __init__(self, root=None):
        super().__init__(root)

    def inorder(self, root, result):
        if root:
            self.inorder(root.left, result)
            result.append('(' + str(root.val) + ')')
            self.inorder(root.right, result)

    def __str__(self):
        result = []
        self.inorder(self.root, result)
        return ''.join(result)

    def creare_bt(self):
        return TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
