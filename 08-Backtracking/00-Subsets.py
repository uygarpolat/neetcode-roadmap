"""
Subsets

https://neetcode.io/problems/subsets?list=neetcode150

Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [7]

Output: [[],[7]]
Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""
from typing import List

class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		result = []
		subset = []

		def dfs(index):
			if index >= len(nums):
				result.append(subset.copy())
				return
			subset.append(nums[index])
			dfs(index+1)
			subset.pop()
			dfs(index+1)
		dfs(0)
		return result
    
def main():
	solution = Solution()
	results = solution.subsets([1,2,3])
	output = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
	for result in results:
		if result not in output:
			assert False
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
