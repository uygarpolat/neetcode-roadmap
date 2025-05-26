"""
Binary Search

https://neetcode.io/problems/binary-search

You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1
Constraints:

1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
"""
from typing import List

class Solution:
	def search(self, nums: List[int], target: int) -> int:

		lo = 0
		hi = len(nums) - 1
			
		while lo <= hi:
			mid = lo + (hi - lo) // 2
			if nums[mid] == target:
				return mid
			elif nums[mid] < target:
				lo = mid + 1
			else:
				hi = mid - 1
		
		return -1
    
def main():
	solution = Solution()
	nums = [-1,0,2,4,6,8]
	target = 4
	result = solution.search(nums, target)
	assert(result == 3)

	nums = [-1,0,2,4,6,8]
	target = 3
	result = solution.search(nums, target)
	assert(result == -1)

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
