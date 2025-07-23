"""
Maximum Product Subarray

https://neetcode.io/problems/maximum-product-subarray?list=neetcode150

Given an integer array nums, find a subarray that has the largest product within the array and return it.

A subarray is a contiguous non-empty sequence of elements within an array.

You can assume the output will fit into a 32-bit integer.

Example 1:

Input: nums = [1,2,-3,4]

Output: 4
Example 2:

Input: nums = [-2,-1]

Output: 2
Constraints:

1 <= nums.length <= 1000
-10 <= nums[i] <= 10
"""
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(res, curMax)
        return result

def main():
	solution = Solution()
	assert solution.maxProduct([1,2,-3,4]) == 4
	assert solution.maxProduct([-2,-1]) == 2
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
