"""
Permutations

https://neetcode.io/problems/permutations?list=neetcode150

Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [7]

Output: [[7]]
Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
"""
from typing import List

class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		result = []
		subset = []
		bool_array = [False] * len(nums)

		def dfs():
			if len(subset) == len(nums):
				result.append(subset.copy())
				return
			
			for i in range(len(nums)):
				if bool_array[i] == False:
					subset.append(nums[i])
					bool_array[i] = True
					dfs()
					subset.pop()
					bool_array[i] = False

		dfs()
		return result

def main():
	solution = Solution()
	result = solution.permute([1,2,3])
	assert result == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
