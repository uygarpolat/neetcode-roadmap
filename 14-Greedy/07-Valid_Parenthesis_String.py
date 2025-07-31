"""
Valid Parenthesis String

https://neetcode.io/problems/valid-parenthesis-string?list=neetcode150

You are given a string s which contains only three types of characters: '(', ')' and '*'.

Return true if s is valid, otherwise return false.

A string is valid if it follows all of the following rules:

Every left parenthesis '(' must have a corresponding right parenthesis ')'.
Every right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
A '*' could be treated as a right parenthesis ')' character or a left parenthesis '(' character, or as an empty string "".
Example 1:

Input: s = "((**)"

Output: true
Explanation: One of the '*' could be a ')' and the other could be an empty string.

Example 2:

Input: s = "(((*)"

Output: false
Explanation: The string is not valid because there is an extra '(' at the beginning, regardless of the extra '*'.

Constraints:

1 <= s.length <= 100
"""
class Solution:
	def checkValidString(self, s: str) -> bool:

		stack_left_par = []
		stack_asterisk = []

		for index, c in enumerate(s):
			if c == "(":
				stack_left_par.append(c)
			elif c == "*":
				stack_asterisk.append(c)
			else:
				if not stack_left_par and not stack_asterisk:
					return False
				if stack_left_par:
					stack_left_par.pop()
				elif stack_asterisk:
					stack_asterisk.pop()

		while stack_left_par and stack_asterisk:
			if stack_left_par.pop() > stack_asterisk.pop():
				return False

		return not stack_left_par

def main():
	solution = Solution()
	assert solution.checkValidString("((**)") == True
	assert solution.checkValidString("(((*)") == False
	assert solution.checkValidString(")()(") == False
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
