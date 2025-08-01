"""
Plus One

https://neetcode.io/problems/plus-one?list=neetcode150

You are given an integer array digits, where each digits[i] is the ith digit of a large integer. It is ordered from most significant to least significant digit, and it will not contain any leading zero.

Return the digits of the given integer after incrementing it by one.

Example 1:

Input: digits = [1,2,3,4]

Output: [1,2,3,5]
Explanation 1234 + 1 = 1235.

Example 2:

Input: digits = [9,9,9]

Output: [1,0,0,0]
Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
"""
from typing import List

class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		result = [0] * len(digits)
		carry = 0
		for i in range(len(digits)-1, -1, -1):
			if i == len(digits) - 1:
				carry += 1
			result[i] = (digits[i] + carry) % 10
			carry = (digits[i] + carry) // 10

		return [1] + result if carry else result
        
def main():
	solution = Solution()
	assert solution.plusOne([1,2,3,4]) == [1,2,3,5]
	assert solution.plusOne([9,9,9]) == [1,0,0,0]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
