"""
Given an unsorted array, find the maximum difference between the successive 
elements in its sorted form.
Return 0 if the array contains less than 2 elements.
"""
import unittest as ut


class Solution(object):

    def maximum_gap_using_sorting(self, nums):
        """Return the maximum gap in nums.
        Complexity = O(n * log n)
        """
        if len(nums) < 2:
            return 0

        nums.sort()
        gap = 0
        for i in range(1, len(nums)):
            gap = max(gap, nums[i] - nums[i - 1])
        return gap

    def maximum_using_pigeonhole_principle(self, nums):
        pass


class Tests(ut.TestCase):
    def test_for_invalid_array(self):
        s = Solution()
        self.assertEqual(s.maximum_gap_using_sorting([1]), 0)

    def test_same_elements(self):
        s = Solution()
        self.assertEqual(s.maximum_gap_using_sorting([1, 1, 1, 1]), 0)

    def test_unsorted_array(self):
        s = Solution()
        self.assertEqual(s.maximum_gap_using_sorting([1, 3, 2, 6]), 3)


if __name__ == '__main__':
    ut.main()
