"""
https://leetcode.com/problems/moving-average-from-data-stream/

Given a stream of integers and a window size, calculate the moving average of 
all integers in the sliding window.
"""

from collections import deque

class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.items = deque()
        self.current_sum = 0

    def next(self, val):
        if len(self.items) < self.size:
            self.items.append(val)
            self.current_sum += val
        else:
            popped = self.items.popleft()
            self.items.append(val)
            self.current_sum += (val-popped)
        return self.current_sum / len(self.items)
