"""
Merge Triplets to Form Target

https://neetcode.io/problems/merge-triplets-to-form-target?list=neetcode150

You are given a 2D array of integers triplets, where triplets[i] = [ai, bi, ci] represents the ith triplet. You are also given an array of integers target = [x, y, z] which is the triplet we want to obtain.

To obtain target, you may apply the following operation on triplets zero or more times:

Choose two different triplets triplets[i] and triplets[j] and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
* E.g. if triplets[i] = [1, 3, 1] and triplets[j] = [2, 1, 2], triplets[j] will be updated to [max(1, 2), max(3, 1), max(1, 2)] = [2, 3, 2].

Return true if it is possible to obtain target as an element of triplets, or false otherwise.

Example 1:

Input: triplets = [[1,2,3],[7,1,1]], target = [7,2,3]

Output: true
Explanation:
Choose the first and second triplets, update the second triplet to be [max(1, 7), max(2, 1), max(3, 1)] = [7, 2, 3].

Example 2:

Input: triplets = [[2,5,6],[1,4,4],[5,7,5]], target = [5,4,6]

Output: false
Constraints:

1 <= triplets.length <= 1000
1 <= ai, bi, ci, x, y, z <= 100
"""
from typing import List

class Solution:
	def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

		n1_max, n2_max, n3_max = 0, 0, 0

		for n1, n2, n3 in triplets:
			if n1 > target[0] or n2 > target[1] or n3 > target[2]:
				continue
			n1_max = max(n1_max, n1)
			n2_max = max(n2_max, n2)
			n3_max = max(n3_max, n3)

		return [n1_max, n2_max, n3_max] == target

def main():
	solution = Solution()
	assert solution.mergeTriplets([[1,2,3],[7,1,1]], [7,2,3]) == True
	assert solution.mergeTriplets([[2,5,6],[1,4,4],[5,7,5]], [5,4,6]) == False
	assert solution.mergeTriplets([[3,4,2],[1,3,6],[5,1,5]],[5,4,6]) == True
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
