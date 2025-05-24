"""
Evaluate Reverse Polish Notation

https://neetcode.io/problems/evaluate-reverse-polish-notation

You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
Constraints:

1 <= tokens.length <= 1000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].


Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.


Hint 1
A brute force solution would involve repeatedly finding an operator + - * / in the array and modifying the array by computing the result for that operator and two operands to its left. This would be an O(n^2) solution. Can you think of a better way? Maybe we can use a data structure to handle operations efficiently.


Hint 2
We can use a stack. We iterate through the array, and if we encounter a number, we push it onto the stack. If we encounter an operator, we pop two elements from the stack, treat them as operands, and solve the equation using the current operator. Then, we push the result back onto the stack. Why does this work?


Hint 3
As the array has postfix expression, stack helps us to maintain the correct order of operations by ensuring that we always use the most recent operands (those closest to the operator) when performing the operation. After the iteration, the final result is left in the stack.
"""
from typing import List
import operator

class Solution:
	def evalRPN(self, tokens: List[str]) -> int:

		def handle_operation(stack, token):

			ops = {
				'+': operator.add,
				'-': operator.sub,
				'*': operator.mul,
				'/': lambda a, b: int(a/b),
			}
			second = stack.pop()
			first = stack.pop()
			return ops[token](first, second) 

		stack = []

		for token in tokens:
			if not token.lstrip('+-').isdigit():
				num = handle_operation(stack, token)
				stack.append(num)
			else:
				stack.append(int(token))

		return stack[0]
    
def main():
	solution = Solution()
	tokens = ["1","2","+","3","*","4","-"]
	result = solution.evalRPN(tokens)
	assert(result == 5)

	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
