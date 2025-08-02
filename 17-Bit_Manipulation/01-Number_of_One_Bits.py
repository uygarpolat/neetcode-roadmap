"""
Number of One Bits

https://neetcode.io/problems/number-of-one-bits?list=neetcode150
 
You are given an unsigned integer n. Return the number of 1 bits in its binary representation.

You may assume n is a non-negative integer which fits within 32-bits.

Example 1:

Input: n = 00000000000000000000000000010111

Output: 4
Example 2:

Input: n = 01111111111111111111111111111101

Output: 30
"""
class Solution:
	def hammingWeight(self, n: int) -> int:
		result = 0
		while n:
			if n & 1:
				result += 1
			n >>= 1
		return result

def main():
	solution = Solution()
	assert solution.hammingWeight(23) == 4
	assert solution.hammingWeight(2147483645) == 30
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
