"""
Partition Equal Subset Sum

https://neetcode.io/problems/partition-equal-subset-sum?list=neetcode150

You are given an array of positive integers nums.

Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.

Example 1:

Input: nums = [1,2,3,4]

Output: true
Explanation: The array can be partitioned as [1, 4] and [2, 3].

Example 2:

Input: nums = [1,2,3,4,5]

Output: false
Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 50
"""
from typing import List

class Solution:
	def canPartition(self, nums: List[int]) -> bool:

		n = len(nums)
		sumNums = sum(nums)
		if sumNums % 2 == 1:
			return False
		target = sumNums // 2
		memo = [[0] * (target + 1) for _ in range(n + 1)]

		def dp(index, target):
			if index >= n or target < 0:
				return False
			if target == 0:
				return True
			if memo[index][target]:
				return memo[index][target]
			
			memo[index][target] = (dp(index + 1, target) or dp(index + 1, target - nums[index]))
			return memo[index][target]

		return dp(0, target)

def main():
	solution = Solution()
	assert solution.canPartition([1,2,3,4]) == True
	assert solution.canPartition([1,2,3,4,5]) == False
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
