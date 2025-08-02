"""
Counting Bits

https://neetcode.io/problems/counting-bits?list=neetcode150

Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].

Return an array output where output[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 4

Output: [0,1,1,2,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100

Constraints:

0 <= n <= 1000
"""
from typing import List

class Solution:
	def countBits(self, n: int) -> List[int]:
		dp = [0] * (n + 1)
		offset = 1
		for i in range(1, n + 1):
			if offset * 2 == i:
				offset = i
			dp[i] = 1 + dp[i - offset]
		return dp

def main():
	solution = Solution()
	assert solution.countBits(4) == [0,1,1,2,1]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
