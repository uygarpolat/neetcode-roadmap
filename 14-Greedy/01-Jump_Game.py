"""
Jump Game

https://neetcode.io/problems/jump-game?list=neetcode150

You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.

Return true if you can reach the last index starting from index 0, or false otherwise.

Example 1:

Input: nums = [1,2,0,1,0]

Output: true
Explanation: First jump from index 0 to 1, then from index 1 to 3, and lastly from index 3 to 4.

Example 2:

Input: nums = [1,2,1,0,1]

Output: false
Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000
"""
from typing import List

class Solution:
	def canJump(self, nums: List[int]) -> bool:
		mark = 0
		for i, num in enumerate(nums):
			mark = max(mark, num)
			if not mark and i != len(nums) - 1:
				return False
			mark -= 1
		return True

def main():
	solution = Solution()
	assert solution.canJump([1,2,0,1,0]) == True
	assert solution.canJump([2,5,0,0]) == True
	assert solution.canJump([2,0,0,5,0,0]) == False
	assert solution.canJump([1,2,1,0,1]) == False
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
