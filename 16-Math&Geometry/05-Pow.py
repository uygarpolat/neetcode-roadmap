"""
Pow(x, n)

https://neetcode.io/problems/pow-x-n?list=neetcode150

Pow(x, n) is a mathematical function to calculate the value of x raised to the power of n (i.e., x^n).

Given a floating-point value x and an integer value n, implement the myPow(x, n) function, which calculates x raised to the power n.

You may not use any built-in library functions.

Example 1:

Input: x = 2.00000, n = 5

Output: 32.00000
Example 2:

Input: x = 1.10000, n = 10

Output: 2.59374
Example 3:

Input: x = 2.00000, n = -3

Output: 0.12500
Constraints:

-100.0 < x < 100.0
-1000 <= n <= 1000
n is an integer.
If x = 0, then n will be positive.
"""
class Solution:
	def myPow(self, x: float, n: int) -> float:
		result: float = 1
		if n < 0:
			m = -n
		else:
			m = n
		
		while m:
			if m % 2 == 1:
				result *= x
			x *= x
			m >>= 1
		
		if n < 0:
			result = 1 / result

		return round(result, 5)

def main():
	solution = Solution()
	assert solution.myPow(2.00000, 5) == 32.00000
	assert solution.myPow(1.10000, 10) == 2.59374
	assert solution.myPow(2.00000, -3) == 0.12500
	assert solution.myPow(34.00515, -3) == 0.00003
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
