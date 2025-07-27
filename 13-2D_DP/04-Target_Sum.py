"""
Target Sum

https://neetcode.io/problems/target-sum?list=neetcode150
 
You are given an array of integers nums and an integer target.

For each number in the array, you can choose to either add or subtract it to a total sum.

For example, if nums = [1, 2], one possible sum would be "+1-2=-1".
If nums=[1,1], there are two different ways to sum the input numbers to get a sum of 0: "+1-1" and "-1+1".

Return the number of different ways that you can build the expression such that the total sum equals target.

Example 1:

Input: nums = [2,2,2], target = 2

Output: 3
Explanation: There are 3 different ways to sum the input numbers to get a sum of 2.
+2 +2 -2 = 2
+2 -2 +2 = 2
-2 +2 +2 = 2

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
-1000 <= target <= 1000
"""
from typing import List

class Solution:
	def findTargetSumWays(self, nums: List[int], target: int) -> int:

		n = len(nums)
		memo = {}

		def dp(index, currentSum):
			if index >= n:
				if currentSum == target:
					return 1
				return 0
			
			if (index, currentSum) in memo:
				return memo[(index, currentSum)]
			
			localNum = nums[index]
			memo[(index, currentSum)] = dp(index+1, currentSum+localNum) + dp(index+1, currentSum-localNum)
			return memo[(index, currentSum)]

		return dp(0, 0)

def main():
	solution = Solution()
	assert solution.findTargetSumWays([2,2,2], 2) == 3
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
