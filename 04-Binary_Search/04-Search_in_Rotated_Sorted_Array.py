"""
Search in Rotated Sorted Array

https://neetcode.io/problems/find-target-in-rotated-sorted-array

You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

Example 1:

Input: nums = [3,4,5,6,1,2], target = 1

Output: 4
Example 2:

Input: nums = [3,5,6,0,1,2], target = 4

Output: -1
Constraints:

1 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-1000 <= target <= 1000
"""
from typing import List

class Solution:
	def search(self, nums: List[int], target: int) -> int:
		lo = 0
		hi = len(nums) - 1

		while lo <= hi:
			mid = (lo + hi) // 2
			if nums[mid] == target:
				return mid
			if nums[mid] >= nums[hi]:
				if nums[mid] < target or nums[hi] >= target:
					lo = mid + 1
				else:
					hi = mid - 1
			else:
				if nums[mid] >= target or target > nums[hi]:
					hi = mid - 1
				else:
					lo = mid + 1

		return -1

def main():
	solution = Solution()
	assert solution.search([3,4,5,6,1,2], 1) == 4
	assert solution.search([3,5,6,0,1,2], 4) == -1
	assert solution.search([3,4,5,6,7,0,1,2], 7) == 4
	assert solution.search([6,0,1,2,3,4,5], 4) == 5
	assert solution.search([1], 1) == 0
	assert solution.search([1,3], 3) == 1
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
