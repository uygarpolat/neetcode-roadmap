"""
Interleaving String

https://neetcode.io/problems/interleaving-string?list=neetcode150

You are given three strings s1, s2, and s3. Return true if s3 is formed by interleaving s1 and s2 together or false otherwise.

Interleaving two strings s and t is done by dividing s and t into n and m substrings respectively, where the following conditions are met

|n - m| <= 1, i.e. the difference between the number of substrings of s and t is at most 1.
s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
Interleaving s and t is s1 + t1 + s2 + t2 + ... or t1 + s1 + t2 + s2 + ...
You may assume that s1, s2 and s3 consist of lowercase English letters.

Example 1:

Input: s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa"

Output: true
Explanation: We can split s1 into ["aa", "aa"], s2 can remain as "bbbb" and s3 is formed by interleaving ["aa", "aa"] and "bbbb".

Example 2:

Input: s1 = "", s2 = "", s3 = ""

Output: true
Example 3:

Input: s1 = "abc", s2 = "xyz", s3 = "abxzcy"

Output: false
Explanation: We can't split s3 into ["ab", "xz", "cy"] as the order of characters is not maintained.

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
"""
class Solution:
	def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

		n1 = len(s1)
		n2 = len(s2)
		n3 = len(s3)

		if n1+n2 != n3:
			return False
		
		memo = {}

		def dp(index1, index2, index3):
			if index3 == n3:
				return index1 == n1 and index2 == index2
			if (index1, index2) in memo:
				return memo[(index1, index2)]
			
			result = False

			if index1 < n1 and s1[index1] == s3[index3]:
				result = dp(index1+1, index2, index3+1)
			if not result and index2 < n2 and s2[index2] == s3[index3]:
				result = dp(index1, index2+1, index3+1)

			memo[(index1, index2)] = result
			return result

		return dp(0, 0, 0)
	
def main():
	solution = Solution()
	assert solution.isInterleave("aaaa", "bbbb", "aabbbbaa") == True
	assert solution.isInterleave("", "", "") == True
	assert solution.isInterleave("abc", "xyz", "abxzcy") == False
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
