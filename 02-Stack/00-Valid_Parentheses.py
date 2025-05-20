"""
Valid Parentheses

https://neetcode.io/problems/validate-parentheses

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:

1 <= s.length <= 1000
"""
class Solution:
	def isValid(self, s: str) -> bool:
		openings = ["(", "{", "["]
		closings = [")", "}", "]"]
		stack = []
        
		for c in s:
			if c in closings:
				index = closings.index(c)
				popped = stack.pop()
				if popped != openings[index]:
					return False
			else:
				stack.append(c)
		return True
    
def main():
	solution = Solution()
	s = "[]"
	result = solution.isValid(s)
	assert(result == True)
     
	s = "([{}])"
	result = solution.isValid(s)
	assert(result == True)
    
	s = "[(])"
	result = solution.isValid(s)
	assert(result == False)
    
	print("✅ All tests passed!")
    
if __name__ == "__main__":
    main()
