"""
Maximum Subarray

https://neetcode.io/problems/maximum-subarray?list=neetcode150

Given an array of integers nums, find the subarray with the largest sum and return the sum.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [2,-3,4,-2,2,1,-1,4]

Output: 8
Explanation: The subarray [4,-2,2,1,-1,4] has the largest sum 8.

Example 2:

Input: nums = [-1]

Output: -1
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
"""
from typing import List

class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		result = nums[0]
		curr = 0
		for num in nums:
			if curr < 0:
				curr = 0
			curr += num
			result = max(result, curr)
		return result

def main():
	solution = Solution()
	assert solution.maxSubArray([2,-3,4,-2,2,1,-1,4]) == 8
	assert solution.maxSubArray([-1]) == -1
	assert solution.maxSubArray([-2,-1]) == -1
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
