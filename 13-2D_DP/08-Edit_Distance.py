"""
Edit Distance

https://neetcode.io/problems/edit-distance?list=neetcode150

You are given two strings word1 and word2, each consisting of lowercase English letters.

You are allowed to perform three operations on word1 an unlimited number of times:

Insert a character at any position
Delete a character at any position
Replace a character at any position
Return the minimum number of operations to make word1 equal word2.

Example 1:

Input: word1 = "monkeys", word2 = "money"

Output: 2
Explanation:
monkeys -> monkey (remove s)
monkey -> monkey (remove k)

Example 2:

Input: word1 = "neatcdee", word2 = "neetcode"

Output: 3
Explanation:
neatcdee -> neetcdee (replace a with e)
neetcdee -> neetcde (remove last e)
neetcde -> neetcode (insert o)

Constraints:

0 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""
class Solution:
	def minDistance(self, word1: str, word2: str) -> int:

		memo = {}
		m = len(word1)
		n = len(word2)

		def dp(index1, index2):
			if index1 == m:
				return n - index2
			if index2 == n:
				return m - index1
			
			if (index1, index2) in memo:
				return memo[(index1, index2)]
			
			if word1[index1] == word2[index2]:
				memo[(index1, index2)] = dp(index1+1, index2+1)
			else:
				memo[(index1, index2)] = 1 + min(dp(index1+1, index2), dp(index1, index2+1), dp(index1+1, index2+1))
			return memo[(index1, index2)]

		return dp(0,0)

def main():
	solution = Solution()
	assert solution.minDistance("monkeys", "money") == 2
	assert solution.minDistance("neatcdee", "neetcode") == 3
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
