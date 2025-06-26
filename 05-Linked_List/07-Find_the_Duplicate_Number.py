"""
Find the Duplicate Number

https://neetcode.io/problems/find-duplicate-integer

You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.

Example 1:

Input: nums = [1,2,3,2,2]

Output: 2
Example 2:

Input: nums = [1,2,3,4,4]

Output: 4
Follow-up: Can you solve the problem without modifying the array nums and using  O(1) extra space?

Constraints:

1 <= n <= 10000
nums.length == n + 1
1 <= nums[i] <= n
"""
from typing import List
import math

class Solution:
	def findDuplicate(self, nums: List[int]) -> int:
		for i in range(len(nums)):
			if nums[abs(nums[i]) - 1] < 0:
				return abs(nums[i])
			nums[abs(nums[i]) - 1] *= -1

def main():
	solution = Solution()
	assert solution.findDuplicate([4,2,1,3,2]) == 2
	assert solution.findDuplicate([1,2,3,4,4]) == 4
	assert solution.findDuplicate([3,1,3,4,2]) == 3
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
