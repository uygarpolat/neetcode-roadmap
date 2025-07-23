"""
House Robber

https://neetcode.io/problems/house-robber?list=neetcode150

You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:

Input: nums = [1,1,3,3]

Output: 4
Explanation: nums[0] + nums[2] = 1 + 3 = 4.

Example 2:

Input: nums = [2,9,8,3,6]

Output: 16
Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
from typing import List

class Solution:
	def rob(self, nums: List[int]) -> int:

		n = len(nums)
		if n == 1:
			return nums[0]
		
		memo = [[0] * 2 for _ in range(n)]

		def dp(house, started_with_zero):
			if house >= n or (started_with_zero and house == n - 1):
				return 0
			
			if memo[house][started_with_zero]:
				return memo[house][started_with_zero]
			memo[house][started_with_zero] = max(dp(house + 1, started_with_zero), nums[house] + dp(house + 2, started_with_zero or (house == 0)))
			return memo[house][started_with_zero]
		
		return max(dp(0, True), dp(1, False))

def main():
	solution = Solution()
	assert solution.rob([1]) == 1
	assert solution.rob([3,4,3]) == 4
	assert solution.rob([2,9,8,3,6]) == 15
	assert solution.rob([5,1,2,6,12,7,9,3,4,10]) == 33
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
