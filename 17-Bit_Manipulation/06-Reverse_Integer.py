"""
Reverse Integer

https://neetcode.io/problems/reverse-integer?list=neetcode150

You are given a signed 32-bit integer x.

Return x after reversing each of its digits. After reversing, if x goes outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0 instead.

Solve the problem without using integers that are outside the signed 32-bit integer range.

Example 1:

Input: x = 1234

Output: 4321
Example 2:

Input: x = -1234

Output: -4321
Example 3:

Input: x = 1234236467

Output: 0
Constraints:

-2^31 <= x <= 2^31 - 1
"""
import math

class Solution:
	def reverse(self, x: int) -> int:

		range = [-2147483648, 2147483647]
		result = 0

		while x:
			n = int(math.fmod(x, 10))
			x = int(x / 10)
			if result < range[0] // 10 or result > range[1] // 10:
				return 0
			if (result == range[1] // 10 and n > range[1] % 10) or \
				(result == range[0] // 10 and n < range[0] % 10):
				return 0
			result = result * 10 + n
			
		return result

def main():
	solution = Solution()
	assert solution.reverse(1234) == 4321
	assert solution.reverse(-1234) == -4321
	assert solution.reverse(1234236467) == 0
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
