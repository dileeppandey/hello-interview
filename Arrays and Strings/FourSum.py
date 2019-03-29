"""
https://leetcode.com/problems/4sum/

Given an array nums of n integers and an integer target, are there elements a, 
b, c, and d in nums such that a + b + c + d = target? Find all unique 
quadruplets in the array which gives the sum of target.
"""
from collections import OrderedDict


class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        self.nSum(nums, target, 4, [], results)
        return results

    def nSum(self, nums, target, N, result, results):
        if len(nums) < 2 or N < 2 or target < nums[0] * N or target > nums[-1] * N:
            return
        if N == 2:
            self.twoSum(nums, target, result, results)
        else:
            for i in range(len(nums) - N + 1):
                if target < nums[i]*N or target > nums[-1]*N:
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    self.nSum(nums[i+1:], target-nums[i],
                              N-1, result+[nums[i]], results)

    def twoSum(self, nums, target, result, results):
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l] + nums[r] == target:
                results.append(result + [nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while r > l and nums[r] == nums[r + 1]:
                    r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1

    def four_sum_meet_middle(self, nums, target):
        nums.sort()
        length = len(nums)

        two_sum_dict = OrderedDict()
        for i in range(length):
            for j in range(i+1, length):
                key = nums[i] + nums[j]
                if key in two_sum_dict:
                    two_sum_dict[key].append([i, j, nums[i], nums[j]])
                else:
                    two_sum_dict[key] = [[i, j, nums[i], nums[j]]]
        print(nums)
        result = []
        print(two_sum_dict)
        for i in range(length):
            for j in range(i+1, length):
                key = target - nums[i] - nums[j]
                if key in two_sum_dict:
                    for item in two_sum_dict[key]:
                        if i not in item[:2] and j not in item[:2]:
                            res = item[2:]+[nums[i], nums[j]]
                            res.sort()
                            if res not in result:
                                result.append(res)

        return result


s = Solution()
print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
