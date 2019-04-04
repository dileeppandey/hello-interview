"""
https://leetcode.com/problems/coin-change/
"""

class Solution:
    def coinChangeMin(self, coins, amount, known):
        minCoins = amount
        if amount in coins:
            known[amount] = 1
            return 1
            
        elif amount in known and known[amount] > 0:
            return known[amount]

        else:
            for i in [c for c in coins if c <= amount]:
                minCoins = min(minCoins, 1 + self.coinChangeMin(coins, amount - i, known))
                known[amount] = minCoins
        return minCoins

    def coinChange(self, coins, amount):
        return self.coinChangeMin(coins, amount, {})