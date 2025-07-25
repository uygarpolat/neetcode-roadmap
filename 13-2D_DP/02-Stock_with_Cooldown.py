"""
Best Time to Buy and Sell Stock with Cooldown

https://neetcode.io/problems/buy-and-sell-crypto-with-cooldown?list=neetcode150

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may buy and sell one NeetCoin multiple times with the following restrictions:

After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
You may only own at most one NeetCoin at a time.
You may complete as many transactions as you like.

Return the maximum profit you can achieve.

Example 1:

Input: prices = [1,3,4,0,4]

Output: 6
Explanation: Buy on day 0 (price = 1) and sell on day 1 (price = 3), profit = 3-1 = 2. Then buy on day 3 (price = 0) and sell on day 4 (price = 4), profit = 4-0 = 4. Total profit is 2 + 4 = 6.

Example 2:

Input: prices = [1]

Output: 0
Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 1)]  

        for i in range(n - 1, -1, -1):
            for action in ["buy", "sell"]:
                if action == "buy":
                    buy = dp[i + 1][0] - prices[i] if i + 1 < n else -prices[i]
                    cooldown = dp[i + 1][1] if i + 1 < n else 0
                    dp[i][1] = max(buy, cooldown)
                else:
                    sell = dp[i + 2][1] + prices[i] if i + 2 < n else prices[i]
                    cooldown = dp[i + 1][0] if i + 1 < n else 0
                    dp[i][0] = max(sell, cooldown)

        return dp[0][1]

def main():
	solution = Solution()
	assert solution.maxProfit([1,3,4,0,4]) == 6
	assert solution.maxProfit([1]) == 0
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
