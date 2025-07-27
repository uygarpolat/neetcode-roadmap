"""
Coin Change II

https://neetcode.io/problems/coin-change-ii?list=neetcode150

You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the number of distinct combinations that total up to amount. If it's impossible to make up the amount, return 0.

You may assume that you have an unlimited number of each coin and that each value in coins is unique.

Example 1:

Input: amount = 4, coins = [1,2,3]

Output: 4
Explanation:

1+1+1+1 = 4
1+1+2 = 4
2+2 = 4
1+3 = 4
Example 2:

Input: amount = 7, coins = [2,4]

Output: 0
Constraints:

1 <= coins.length <= 100
1 <= coins[i] <= 5000
0 <= amount <= 5000
"""
from typing import List

class Solution:
	def change(self, amount: int, coins: List[int]) -> int:
		coins.sort()
		memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]

		def dp(index, amnt):
			if amnt == 0:
				return 1
			if index >= len(coins):
				return 0
			if memo[index][amnt] != -1:
				return memo[index][amnt]
			
			result = dp(index+1, amnt)
			if amnt >= coins[index]:
				result += dp(index, amnt-coins[index])

			memo[index][amnt] = result
			return result

		return dp(0, amount)

def main():
	solution = Solution()
	assert solution.change(4, [1,2,3]) == 4
	assert solution.change(7, [2,4]) == 0
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
