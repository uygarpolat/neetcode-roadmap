"""
Climbing Stairs

https://neetcode.io/problems/climbing-stairs?list=neetcode150

You are given an integer n representing the number of steps to reach the top of a staircase. You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase.

Example 1:
Input: n = 2
Output: 2
Explanation:

1 + 1 = 2
2 = 2

Example 2:
Input: n = 3
Output: 3
Explanation:
1 + 1 + 1 = 3
1 + 2 = 3
2 + 1 = 3

Constraints:
1 <= n <= 30
"""
class Solution:
	def climbStairs(self, n: int) -> int:
		cache = [0] * n

		def dp(level):
			if level >= n:
				return level == n
			if cache[level]:
				return cache[level]
			cache[level] = dp(level+1) + dp(level+2)
			return cache[level]
		
		return dp(0)
	
def main():
	solution = Solution()
	assert solution.climbStairs(2) == 2
	assert solution.climbStairs(3) == 3
	assert solution.climbStairs(13) == 377
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
