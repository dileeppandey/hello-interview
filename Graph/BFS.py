"""
BFS traversal of a graph
"""
from collections import deque


class Solution(object):

    def bfs_traversal(self, root):
        if root is None:
            return []
        Q = deque()
        Q.append(root)
        # while len(Q) != 0:
        #     for i in range(len(Q)):
        pass
