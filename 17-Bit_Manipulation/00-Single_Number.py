"""
Single Number

https://neetcode.io/problems/single-number?list=neetcode150

You are given a non-empty array of integers nums. Every integer appears twice except for one.

Return the integer that appears only once.

You must implement a solution with O(n) runtime complexity and use only O(1) extra space.

Example 1:

Input: nums = [3,2,3]

Output: 2
Example 2:

Input: nums = [7,6,6,7,8]

Output: 8
Constraints:

1 <= nums.length <= 10000
-10000 <= nums[i] <= 10000
"""
from typing import List
from functools import reduce
from operator import xor

class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		return reduce(xor, nums)

def main():
	solution = Solution()
	assert solution.singleNumber([3,2,3]) == 2
	assert solution.singleNumber([7,6,6,7,8]) == 8
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
