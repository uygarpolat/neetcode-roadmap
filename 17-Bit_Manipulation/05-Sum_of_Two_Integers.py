"""
Sum of Two Integers

https://neetcode.io/problems/sum-of-two-integers?list=neetcode150

Given two integers a and b, return the sum of the two integers without using the + and - operators.

Example 1:

Input: a = 1, b = 1

Output: 2
Example 2:

Input: a = 4, b = 7

Output: 11
Constraints:

-1000 <= a, b <= 1000
"""
class Solution:
	def getSum(self, a: int, b: int) -> int:

		carry = 0
		result = 0
		mask = 0xFFFFFFFF

		for i in range(32):
			old_a = (a >> i) & 1
			old_b = (b >> i) & 1
			curr_bit = old_a ^ old_b ^ carry
			carry = (old_a + old_b + carry) >= 2
			if curr_bit:
				result |= (1 << i)
			
		if result > mask:
			result = ~(result ^ mask)
			
		return result

def main():
	solution = Solution()
	assert solution.getSum(1,1) == 2
	assert solution.getSum(4,7) == 11
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
