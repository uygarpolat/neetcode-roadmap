"""
Contains Duplicate
 
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    
def main():
	solution = Solution()
	nums = [1,2,3,3]
	result = solution.hasDuplicate(nums)
	print(result) # Expected outcome: True
     
	nums = [1,2,3,4]
	result = solution.hasDuplicate(nums)
	print(result) # Expected outcome: False
     
if __name__ == "__main__":
     main()
