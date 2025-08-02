"""
Missing Number

https://neetcode.io/problems/missing-number?list=neetcode150

Given an array nums containing n integers in the range [0, n] without any duplicates, return the single number in the range that is missing from nums.

Follow-up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Example 1:

Input: nums = [1,2,3]

Output: 0
Explanation: Since there are 3 numbers, the range is [0,3]. The missing number is 0 since it does not appear in nums.

Example 2:

Input: nums = [0,2]

Output: 1
Constraints:

1 <= nums.length <= 1000
"""
from typing import List

class Solution:
	def missingNumber(self, nums: List[int]) -> int:
		result = 0
		hi = max(nums)
		for i in range(1, hi+1):
			result ^= i
		for num in nums:
			result ^= num
		if not result:
			if 0 in nums:
				result = hi+1
		return result

def main():
	solution = Solution()
	assert solution.missingNumber([1,2,3]) == 0
	assert solution.missingNumber([0,2]) == 1
	assert solution.missingNumber([3,0,1]) == 2
	assert solution.missingNumber([0,1]) == 2
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
