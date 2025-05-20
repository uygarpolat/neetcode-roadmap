"""
Longest Substring Without Repeating Characters

https://neetcode.io/problems/longest-substring-without-duplicates
 
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1
Constraints:

0 <= s.length <= 1000
s may consist of printable ASCII characters.


Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(m) space, where n is the length of the string and m is the number of unique characters in the string.
"""
class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		
		left = 0
		right = 0
		set_s = set()
		result = 0
		
		while left <= right and right < len(s):
			if s[right] in set_s:
				set_s.discard(s[left])
				left += 1
			else:
				set_s.add(s[right])
				right += 1
				result = max(result,len(set_s))
		return result
    
def main():
	solution = Solution()
	s = "zxyzxyz"
	result = solution.lengthOfLongestSubstring(s)
	assert(result == 3)
    
	s = "xxxx"
	result = solution.lengthOfLongestSubstring(s)
	assert(result == 1)

	s = "pwwkew"
	result = solution.lengthOfLongestSubstring(s)
	assert(result == 3)

	print("✅ All tests passed!")

     
if __name__ == "__main__":
	main()
