"""
https://leetcode.com/problems/diagonal-traverse/
Given a matrix of M x N elements (M rows, N columns), return all elements of the
matrix in diagonal order as shown in the below image.
"""
from collections import deque

class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        rows, cols = len(matrix[0][:]), len(matrix[:][1])
        visited = set()
        Q = deque([(0, 0), (-1, -1)])
        result, items, level = [], [], 0
        while Q:
            i, j = Q.popleft()
            if  i == j == -1:
                if level & 1:
                    items = items[::-1]
                result.extend(items)
                level += 1
                items = []
                if not Q:
                    break
                Q.append((-1, -1))
            else:
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                items.append(matrix[i][j])
                if 0 <= i + 1 < rows and 0 <= j < cols:
                    Q.append((i+1, j))
                if 0 <= i < rows and 0 <= j + 1 < cols:
                    Q.append((i, j + 1))
        return result


s = Solution()
print(s.findDiagonalOrder([[1, 2], [4, 5], [7, 8]]))
# print(s.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

