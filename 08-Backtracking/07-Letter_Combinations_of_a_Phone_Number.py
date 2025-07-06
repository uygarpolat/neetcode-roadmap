"""
Letter Combinations of a Phone Number

https://neetcode.io/problems/combinations-of-a-phone-number?list=neetcode150

You are given a string digits made up of digits from 2 through 9 inclusive.

Each digit (not including 1) is mapped to a set of characters as shown below:

A digit could represent any one of the characters it maps to.

Return all possible letter combinations that digits could represent. You may return the answer in any order.

Example 1:

Input: digits = "34"

Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
Example 2:

Input: digits = ""

Output: []
Constraints:

0 <= digits.length <= 4
2 <= digits[i] <= 9
"""
from typing import List

class Solution:
	def letterCombinations(self, digits: str) -> List[str]:

		if not digits:
			return []
        
		result = []
		numberpad = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

		def dfs(index, currentStr):
			if len(currentStr) == len(digits):
				result.append(currentStr)
				return

			for c in numberpad[int(digits[index])]:
				dfs(index+1, currentStr+c)

		dfs(0, "")
		return result
    
def main():
	solution = Solution()
	assert solution.letterCombinations("34") == ["dg","dh","di","eg","eh","ei","fg","fh","fi"]
	assert solution.letterCombinations("") == []
	print("✅ All tests passed!")

if __name__ == "__main__":
    main()
