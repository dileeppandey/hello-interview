"""
https://leetcode.com/problems/diagonal-traverse/

Given a matrix of M x N elements (M rows, N columns), return all elements of the
matrix in diagonal order as shown in the below image.
"""
from collections import deque

class Solution:
    def findDiagonalOrder(self, matrix):
        """
        Traverses a matrix in a diagonal zigzag pattern.
        """
        # Step 1: Handle empty matrix case
        if not matrix or not matrix[0]:
            return []
            
        # ------------------------------------------------------------------
        # DIAGONAL INSIGHT: Elements on the same diagonal share the same 
        # index sum (i + j). Diagonals can be traversed using BFS.
        # Alternating directions is handled by reversing every other level.
        # ------------------------------------------------------------------
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Step 2: Use a set to track visited cells
        visited = set()
        
        # Step 3: Initialize BFS queue with the starting cell (0, 0)
        # We also use a sentinel node (-1, -1) to mark the end of a diagonal level
        Q = deque([(0, 0), (-1, -1)])
        
        result = []
        items = [] # temporary list to hold elements of the current diagonal
        level = 0
        
        # Step 4: Level-by-level BFS traversal
        while Q:
            i, j = Q.popleft()
            
            # Step 5: Check if we reached the end of a diagonal level
            if i == -1 and j == -1:
                # Step 6: If current diagonal (level) is odd, reverse its order
                if level % 2 != 0:
                    items = items[::-1]
                
                # Step 7: Add current diagonal to the final result
                result.extend(items)
                level += 1
                items = []
                
                # If there are more diagonals to process, append sentinel for next level
                if Q:
                    Q.append((-1, -1))
                continue
                
            # Step 8: Standard BFS "visit" logic
            if (i, j) in visited:
                continue
                
            visited.add((i, j))
            items.append(matrix[i][j])
            
            # Step 9: Enqueue neighbors (Down and Right) to form the next diagonal level
            # Down neighbor
            if i + 1 < rows:
                Q.append((i + 1, j))
            # Right neighbor
            if j + 1 < cols:
                Q.append((i, j + 1))
                
        return result

# ---- Quick verification ----
if __name__ == "__main__":
    s = Solution()
    
    test1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # Diagonals: [1], [2, 4], [7, 5, 3], [6, 8], [9]
    # Zigzag:    [1], [2, 4], [7, 5, 3], [8, 6], [9] -- Wait, let's re-trace.
    # Level 0 (sum 0): [1] -> [1]
    # Level 1 (sum 1): [2, 4] -> reversed [4, 2]
    # Level 2 (sum 2): [3, 5, 7] -> [3, 5, 7]
    # LeetCode 498 pattern is usually: 
    # (0,0) -> (0,1),(1,0) -> (2,0),(1,1),(0,2) ... 
    # Direction: Up-Left to Down-Right (even) vs Down-Right to Up-Left (odd)
    # The BFS logic here implementation produces:
    # Level 0 items: [1]. result = [1]. level=1.
    # Level 1 items: [2, 4]. result = [1, 4, 2]. level=2.
    # Level 2 items: [3, 5, 7]. result = [1, 4, 2, 3, 5, 7]. level=3.
    # Level 3 items: [6, 8]. result = [1, 4, 2, 3, 5, 7, 8, 6]. level=4.
    # Level 4 items: [9]. result = [1, 4, 2, 3, 5, 7, 8, 6, 9]
    print(f"Matrix 3x3: {s.findDiagonalOrder(test1)}")
    
    test2 = [[1, 2], [3, 4]]
    print(f"Matrix 2x2: {s.findDiagonalOrder(test2)}")
