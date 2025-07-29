"""
Burst Balloons

https://neetcode.io/problems/burst-balloons?list=neetcode150
 
You are given an array of integers nums of size n. The ith element represents a balloon with an integer value of nums[i]. You must burst all of the balloons.

If you burst the ith balloon, you will receive nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then assume the out of bounds value is 1.

Return the maximum number of coins you can receive by bursting all of the balloons.

Example 1:

Input: nums = [4,2,3,7]

Output: 143

Explanation:
nums = [4,2,3,7] --> [4,3,7] --> [4,7] --> [7] --> []
coins =  4*2*3    +   4*3*7   +  1*4*7  + 1*7*1 = 143
Constraints:

n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
"""
from typing import List

class Solution:
	def maxCoins(self, nums: List[int]) -> int:

		nums = [1] + nums + [1]
		memo = {}

		def dp(l, r):
			if l > r:
				return 0
			if (l,r) in memo:
				return memo[(l,r)]

			memo[(l,r)] = 0
			for i in range(l, r + 1):
				coins = nums[l - 1] * nums[i] * nums[r + 1] + dp(l, i - 1) + dp(i + 1, r)
				memo[(l, r)] = max(memo[(l, r)], coins)
			return memo[(l, r)]
		return dp(1, len(nums)-2)
        
def main():
	solution = Solution()
	assert solution.maxCoins([4,2,3,7]) == 143
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
