"""
Encode and Decode Strings
 
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.
"""
from typing import List

class Solution:

	def encode(self, strs: List[str]) -> str:
		result = ""
		for stri in strs:
			result += str(len(stri)) + "#" + stri
		return result

	def decode(self, s: str) -> List[str]:
		result = []
		i = 0
		while i < len(s):
			length = 0
			while s[i].isdigit():
				length = length * 10 + int(s[i])
				i += 1
			i += 1
			result.append(s[i:i+length])
			i += length
		return result

def main():
	solution = Solution()
	input = ["neet","code","love","you"]
	encoded = solution.encode(input)
	decoded = solution.decode(encoded)
	assert(input == decoded)

	input = ["we","say",":","yes"]
	encoded = solution.encode(input)
	decoded = solution.decode(encoded)
	assert(input == decoded)
	print("✅ All tests passed!")

if __name__ == "__main__":
    main()