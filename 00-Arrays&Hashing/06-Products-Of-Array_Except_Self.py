"""
Products of Array Except Self

Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
Constraints:

2 <= nums.length <= 1000
-20 <= nums[i] <= 20

Recommended Time & Space Complexity
You should aim for a solution as good or better than O(n) time and O(n) space, where n is the size of the input array.
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        for i in range(1,len(nums)):
             prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1,-1):
             suffix[i] = suffix[i+1] * nums[i+1]
        return [a*b for a, b in zip(prefix, suffix)]
    
def main():
	solution = Solution()
	nums = [1,2,4,6]
	assert(solution.productExceptSelf(nums) == [48,24,12,8])
	nums = [-1,0,1,2,3]
	assert(solution.productExceptSelf(nums) == [0,-6,0,0,0])
	print("✅ All tests passed!")

if __name__ == "__main__":
    main()