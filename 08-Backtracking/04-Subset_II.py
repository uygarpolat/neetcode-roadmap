"""
Subsets II

https://neetcode.io/problems/subsets-ii?list=neetcode150

You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

The solution must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,1]

Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]
Example 2:

Input: nums = [7,7]

Output: [[],[7], [7,7]]
Constraints:

1 <= nums.length <= 11
-20 <= nums[i] <= 20
"""
from typing import List

class Solution:
	def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

		result = []
		subset = []
		nums.sort()

		def dfs(index):

			result.append(subset.copy())

			for i in range(index, len(nums)):
				if i > index and nums[i] == nums[i-1]:
					continue
				subset.append(nums[i])
				dfs(i+1)
				subset.pop()

		dfs(0)
		return result
	
def main():
	solution = Solution()
	assert solution.subsetsWithDup([1,2,1]) == [[], [1], [1, 1], [1, 1, 2], [1, 2], [2]]
	assert solution.subsetsWithDup([7,7]) == [[], [7], [7,7]]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
