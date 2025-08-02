"""
Multiply Strings

https://neetcode.io/problems/multiply-strings?list=neetcode150

You are given two strings num1 and num2 that represent non-negative integers.

Return the product of num1 and num2 in the form of a string.

Assume that neither num1 nor num2 contain any leading zero, unless they are the number 0 itself.

Note: You can not use any built-in library to convert the inputs directly into integers.

Example 1:

Input: num1 = "3", num2 = "4"

Output: "12"
Example 2:

Input: num1 = "111", num2 = "222"

Output: "24642"
Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
"""
class Solution:
	def multiply(self, num1: str, num2: str) -> str:

		def mul(num: str, digit: chr, zero: int) -> str:
			result = []
			carry = 0
			constant = int(digit)
			for _ in range(zero):
				result.append("0")
			for i in range(len(num)-1, -1, -1):
				digit = (int(num[i]) * constant + carry) % 10
				carry = (int(num[i]) * constant + carry) // 10
				result.append(str(digit))
			if carry:
				result.append(str(carry))

			return ''.join(result[::-1])

		def add(num1, num2):

			result = []
			i = len(num1) - 1
			j = len(num2) - 1
			carry = 0

			while i >= 0 or j >=0:
			
				n1 = num1[i] if i >= 0 else "0"
				n2 = num2[j] if j >= 0 else "0"
				digit = (int(n1) + int(n2) + carry) % 10
				carry = (int(n1) + int(n2) + carry) // 10
				result.append(str(digit))
				i -= 1
				j -= 1
			if carry:
				result.append(str(carry))

			return ''.join(result[::-1])

		if num1 == "0" or num2 == "0":
			return "0"
		
		if len(num1) < len(num2):
			return self.multiply(num2, num1)
		
		result = ""
		zero = 0

		for i in range(len(num2)-1, -1, -1):
			current = mul(num1, num2[i], zero)
			result = add(result, current)
			zero += 1

		return result

def main():
	solution = Solution()
	assert solution.multiply("3", "4") == "12"
	assert solution.multiply("111", "222") == "24642"
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
