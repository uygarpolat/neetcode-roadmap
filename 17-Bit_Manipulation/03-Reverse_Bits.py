"""
Reverse Bits

https://neetcode.io/problems/reverse-bits?list=neetcode150

Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.

Example 1:

Input: n = 00000000000000000000000000010101

Output:    2818572288 (10101000000000000000000000000000)
Explanation: Reversing 00000000000000000000000000010101, which represents the unsigned integer 21, gives us 10101000000000000000000000000000 which represents the unsigned integer 2818572288.
"""
class Solution:
	def reverseBits(self, n: int) -> int:
		result = 0
		for i in range(32):
			current = (n >> i) & 1
			result += (current << (31-i))
		return result

def main():
	solution = Solution()
	assert solution.reverseBits(21) == 2818572288
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
