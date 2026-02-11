"""
https://leetcode.com/problems/coin-change/
"""
from sys import maxsize


class Solution:
    def coinChangeMin(self, coins, amount, tbl):
        if amount == 0:
            return 0
        
        if amount in tbl:
            return tbl[amount]

        minCount = maxsize

        for i in range(len(coins)):
            if coins[i] > amount:
                continue
            minCount = min(minCount, self.coinChangeMin(coins, amount - coins[i], tbl))

        minCount = (minCount if minCount == maxsize else minCount + 1)
        tbl[amount] = minCount
        return minCount

    def coinChange(self, coins, amount):
        minCount = self.coinChangeMin(coins, amount, {})
        return -1 if minCount == maxsize else minCount

s = Solution()
print(s.coinChange([1,2,5], 11))        