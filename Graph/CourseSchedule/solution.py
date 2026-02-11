"""
https://leetcode.com/problems/course-schedule/

There are numCourses courses labeled from 0 to numCourses - 1. You are given
an array prerequisites where prerequisites[i] = [ai, bi] indicates that you
must take course bi first before taking course ai.

Return true if you can finish all courses. (i.e., detect if there's a cycle
in the prerequisite graph — if there is, it's impossible.)

Example: numCourses = 2, prerequisites = [[1,0]] → True (take 0, then 1)
Example: numCourses = 2, prerequisites = [[1,0],[0,1]] → False (cycle!)
"""
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # ------------------------------------------------------------------
        # GRAPH INSIGHT: Model courses as nodes, prerequisites as directed
        # edges. If the graph has a cycle, we can't finish all courses.
        # We use DFS with 3-coloring to detect cycles:
        #   WHITE (0) = unvisited
        #   GRAY  (1) = currently being processed (in the current DFS path)
        #   BLACK (2) = fully processed
        # A cycle exists iff we encounter a GRAY node during DFS.
        # ------------------------------------------------------------------

        # Step 1: Build adjacency list
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # Step 2: Track the state of each node (0=white, 1=gray, 2=black)
        color = [0] * numCourses

        def has_cycle(node: int) -> bool:
            """Returns True if a cycle is detected from this node."""
            if color[node] == 1:
                # Step 3a: We've hit a gray node — cycle detected!
                return True
            if color[node] == 2:
                # Step 3b: Already fully processed, no cycle from here
                return False

            # Step 4: Mark as gray (in progress)
            color[node] = 1

            # Step 5: Visit all neighbors
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True

            # Step 6: Mark as black (complete) — no cycle found from this node
            color[node] = 2
            return False

        # Step 7: Check every course (graph may be disconnected)
        for course in range(numCourses):
            if has_cycle(course):
                return False

        return True


# ---- Quick verification ----
s = Solution()
print(s.canFinish(2, [[1, 0]]))              # Expected: True
print(s.canFinish(2, [[1, 0], [0, 1]]))      # Expected: False (cycle)
print(s.canFinish(4, [[1, 0], [2, 1], [3, 2]]))  # Expected: True (chain)
