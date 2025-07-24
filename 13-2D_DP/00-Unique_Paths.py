"""
Unique Paths

https://neetcode.io/problems/count-paths?list=neetcode150

There is an m x n grid where you are allowed to move either down or to the right at any point in time.

Given the two integers m and n, return the number of possible unique paths that can be taken from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).

You may assume the output will fit in a 32-bit integer.

Example 1:

Input: m = 3, n = 6

Output: 21
Example 2:

Input: m = 3, n = 3

Output: 6
Constraints:

1 <= m, n <= 100
"""
class Solution:
	def uniquePaths(self, m: int, n: int) -> int:

		memo = [[0] * n for _ in range(m)]

		def dp(i, j):
			if i == m-1 and j == n-1:
				return 1
			if not 0 <= i < m or not 0 <= j < n:
				return 0
			if memo[i][j]:
				return memo[i][j]
			
			memo[i][j] = dp(i+1,j) + dp(i,j+1)
			return memo[i][j]

		return dp(0,0)

def main():
	solution = Solution()
	assert solution.uniquePaths(3,6) == 21
	assert solution.uniquePaths(3,3) == 6
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
