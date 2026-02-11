from trees.tree import Tree
from trees.tree_node import TreeNode
from trees.binary_tree import BinaryTree


class BinarySearchTree(Tree):
    def __init__(self, root=None):
        super().__init__(root)

    def create_bst(self):
        return TreeNode(35, TreeNode(20, TreeNode(15, TreeNode(10), TreeNode(18)), TreeNode(30)), TreeNode(55, TreeNode(40), TreeNode(65)))

    def check_bst(self):
        pass

    def delete(self, node):
        pass

    def searchRecur(self, current, val):
        if current:
            if current.val == val:
                return True
            if current.val > val:
                return self.searchRecur(current.left, val)
            if current.val < val:
                return self.searchRecur(current.right, val)
        return False

    def search(self, val):
        return self.searchRecur(self.root, val)

    def insertRecur(self, current, val):
        if current.val >= val:
            if current.left is None:
                current.left = TreeNode(val)
                return
            return self.insertRecur(current.left, val)
        else:
            if current.right is None:
                current.right = TreeNode(val)
                return
            return self.insertRecur(current.right, val)

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        self.insertRecur(self.root, val)

if __name__ == "__main__":
    s = BinarySearchTree()
    s.root = s.create_bst()
    s.insert(9)
    s.insert(17)
    s.insert(50)
    s.insert(60)
    s.insert(70)
    b = BinaryTree()
    b.root = s.root
    print(b)
    print(s.search(60))
    print(s.search(8))
    print(s.search(90))
