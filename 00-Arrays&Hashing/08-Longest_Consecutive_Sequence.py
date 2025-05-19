"""
Longest Consecutive Sequence

Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
"""
from typing import List

class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		nums_set = set(nums)
		sequence_start_set = set()
    
		for num in nums_set:
			if num-1 not in nums_set:
				sequence_start_set.add(num)

		result = 0
		for num in sequence_start_set:
			count = 0
			while num in nums_set:
				count += 1
				num += 1
			if result < count:
				result = count
        
		return result
    
def main():
	solution = Solution()
	nums = [2,20,4,10,3,4,5]
	result = solution.longestConsecutive(nums)
	assert(result == 4)

	nums = [0,3,2,5,4,6,1,1]
	result = solution.longestConsecutive(nums)
	assert(result == 7)

	print("✅ All tests passed!")
    
if __name__ == "__main__":
    main()
