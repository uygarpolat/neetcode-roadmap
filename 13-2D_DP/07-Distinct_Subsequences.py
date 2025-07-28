"""
Distinct Subsequences

https://neetcode.io/problems/count-subsequences?list=neetcode150

You are given two strings s and t, both consisting of english letters.

Return the number of distinct subsequences of s which are equal to t.

Example 1:

Input: s = "caaat", t = "cat"

Output: 3
Explanation: There are 3 ways you can generate "cat" from s.

(c)aa(at)
(c)a(a)a(t)
(ca)aa(t)
Example 2:

Input: s = "xxyxy", t = "xy"

Output: 5
Explanation: There are 5 ways you can generate "xy" from s.

(x)x(y)xy
(x)xyx(y)
x(x)(y)xy
x(x)yx(y)
xxy(x)(y)
Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""
class Solution:
	def numDistinct(self, s: str, t: str) -> int:

		n = len(s)
		m = len(t)
		memo = {}

		def dp(index_s, index_t):
			
			if index_t == m:
				return 1
			if index_s == n:
				return 0

			if (index_s, index_t) in memo:
				return memo[(index_s, index_t)]
			
			result = 0
			
			if s[index_s] == t[index_t]:
				result = dp(index_s + 1, index_t + 1)
			result += dp(index_s + 1, index_t)

			memo[(index_s, index_t)] = result
			return result

		return dp(0,0)
        
def main():
	solution = Solution()
	assert solution.numDistinct("caaat", "cat") == 3
	assert solution.numDistinct("xxyxy", "xy") == 5
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
