"""
https://leetcode.com/problems/word-search-ii/

Given an m x n board of characters and a list of strings words, return all
words on the board. Each word must be constructed from letters of sequentially
adjacent cells (horizontally or vertically), where the same cell may not be
used more than once per word.

Example:
    board = [["o","a","a","n"],
             ["e","t","a","e"],
             ["i","h","k","r"],
             ["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    Output: ["eat","oath"]
"""


class TrieNode:
    """Trie node for efficient prefix matching."""
    def __init__(self):
        self.children = {}
        self.word = None  # Store the complete word at leaf nodes


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # ------------------------------------------------------------------
        # TRIE + BACKTRACKING INSIGHT:
        # 1. Build a Trie from all target words → efficient prefix checking
        # 2. DFS from every cell on the board
        # 3. At each step, check if the current path is a valid Trie prefix
        #    If not → prune (don't explore further)
        #    If we reach a word end → add to results
        # ------------------------------------------------------------------

        # Step 1: Build the Trie from all target words
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # Mark the end of each word

        rows, cols = len(board), len(board[0])
        result = []

        # Step 2: DFS with backtracking
        def dfs(r: int, c: int, parent: TrieNode) -> None:
            char = board[r][c]

            # Step 3: Check if current char is a valid Trie prefix
            if char not in parent.children:
                return  # Prune — no word starts with this prefix

            node = parent.children[char]

            # Step 4: Check if we've found a complete word
            if node.word is not None:
                result.append(node.word)
                node.word = None  # Avoid duplicates

            # Step 5: Mark the cell as visited (using a sentinel)
            board[r][c] = '#'

            # Step 6: Explore all 4 directions
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, node)

            # Step 7: Backtrack — restore the cell
            board[r][c] = char

            # Step 8: Optimization — prune empty Trie branches
            if not node.children:
                del parent.children[char]

        # Step 9: Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result


# ---- Quick verification ----
s = Solution()
board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"]
]
print(sorted(s.findWords(board, ["oath", "pea", "eat", "rain"])))
# Expected: ['eat', 'oath']

board2 = [["a", "b"], ["c", "d"]]
print(s.findWords(board2, ["abcb"]))
# Expected: []
