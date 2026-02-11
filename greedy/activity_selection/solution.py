"""
Activity Selection / Interval Scheduling Maximization

Given a list of activities with start and end times, select the maximum number
of non-overlapping activities that can be performed by a single person.

Example:
    activities = [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)]
    Output: 4  →  [(1,4), (5,7), (8,11), (12,16)]
"""


class Solution:
    def maxActivities(self, activities: list[tuple[int, int]]) -> list[tuple[int, int]]:
        # ------------------------------------------------------------------
        # GREEDY INSIGHT: Always pick the activity that finishes earliest.
        # This leaves the most room for subsequent activities.
        # ------------------------------------------------------------------

        # Step 1: Sort activities by their end (finish) time
        #         This is the key greedy choice — earliest finish first
        sorted_activities = sorted(activities, key=lambda x: x[1])

        # Step 2: Always select the first activity (earliest finish)
        selected = [sorted_activities[0]]
        last_end = sorted_activities[0][1]

        # Step 3: Iterate through remaining activities
        for i in range(1, len(sorted_activities)):
            start, end = sorted_activities[i]

            # Step 4: If this activity starts at or after the last selected
            #         activity ends, it's compatible — select it
            if start >= last_end:
                selected.append((start, end))
                last_end = end
                # We greedily commit to this choice and never revisit it

        return selected


# ---- Quick verification ----
s = Solution()
activities = [
    (1, 4), (3, 5), (0, 6), (5, 7), (3, 9),
    (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)
]
result = s.maxActivities(activities)
print(f"Selected {len(result)} activities: {result}")
# Expected: 4 activities, e.g. [(1,4), (5,7), (8,11), (12,16)]

print(s.maxActivities([(1, 2), (3, 4), (5, 6)]))
# Expected: [(1,2), (3,4), (5,6)] — all 3, no overlap

print(s.maxActivities([(1, 10), (2, 3), (4, 5)]))
# Expected: [(2,3), (4,5)] — skip the long one
