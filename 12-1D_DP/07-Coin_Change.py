"""
Coin Change

https://neetcode.io/problems/coin-change?list=neetcode150

You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.

You may assume that you have an unlimited number of each coin.

Example 1:

Input: coins = [1,5,10], amount = 12

Output: 3
Explanation: 12 = 10 + 1 + 1. Note that we do not have to use every kind coin available.

Example 2:

Input: coins = [2], amount = 3

Output: -1
Explanation: The amount of 3 cannot be made up with coins of 2.

Example 3:

Input: coins = [1], amount = 0

Output: 0
Explanation: Choosing 0 coins is a valid way to make up 0.

Constraints:

1 <= coins.length <= 10
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10000
"""
from typing import List

class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:

		memo = {}

		def dp(amount):
			if amount == 0:
				return 0
			if amount in memo:
				return memo[amount]
			
			result = float("inf")
			
			for coin in coins:
				if amount - coin >= 0:
					result = min(result, 1 + dp(amount-coin))

			memo[amount] = result
			return result

		minCoins = dp(amount)
		return -1 if minCoins == float("inf") else minCoins

def main():
	solution = Solution()
	assert solution.coinChange([1,5,10], 12) == 3
	assert solution.coinChange([2], 3) == -1
	assert solution.coinChange([1], 0) == 0
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
