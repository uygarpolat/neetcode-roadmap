"""
Best Time to Buy and Sell Stock

https://neetcode.io/problems/buy-and-sell-crypto

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 100
"""

from typing import List

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
        
		min_price = float('inf')
		max_profit = 0
		for price in prices:
			max_profit = max(max_profit, price - min_price)
			min_price = min(min_price, price)
		return max_profit

def main():
	solution = Solution()
	prices = [10,1,5,6,7,1]
	result = solution.maxProfit(prices)
	assert(result == 6)
    
	prices = [10,8,7,5,2]
	result = solution.maxProfit(prices)
	assert(result == 0)

	print("✅ All tests passed!")

     
if __name__ == "__main__":
     main()
