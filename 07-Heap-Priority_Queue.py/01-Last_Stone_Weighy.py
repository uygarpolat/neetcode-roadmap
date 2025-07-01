"""
Last Stone Weight

https://neetcode.io/problems/last-stone-weight?list=neetcode150

You are given an array of integers stones where stones[i] represents the weight of the ith stone.

We want to run a simulation on the stones as follows:

At each step we choose the two heaviest stones, with weight x and y and smash them togethers
If x == y, both stones are destroyed
If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.

Example 1:

Input: stones = [2,3,6,2,4]

Output: 1
Explanation:
We smash 6 and 4 and are left with a 2, so the array becomes [2,3,2,2].
We smash 3 and 2 and are left with a 1, so the array becomes [1,2,2].
We smash 2 and 2, so the array becomes [1].

Example 2:

Input: stones = [1,2]

Output: 1
Constraints:

1 <= stones.length <= 20
1 <= stones[i] <= 100
"""
from typing import List
import heapq

class Solution:
	def lastStoneWeight(self, stones: List[int]) -> int:
		if len(stones) == 1:
			return stones[0]
		stones_flipped = [-x for x in stones]
		heapq.heapify(stones_flipped)
		while(len(stones_flipped) > 1):
			first = heapq.heappop(stones_flipped)
			second = heapq.heappop(stones_flipped)
			heapq.heappush(stones_flipped, first-second)
		return -stones_flipped[0] if len(stones_flipped) == 1 else 0

def main():
	solution = Solution()
	assert solution.lastStoneWeight([2,3,6,2,4]) == 1
	assert solution.lastStoneWeight([1,2]) == 1
	assert solution.lastStoneWeight([1]) == 1
	assert solution.lastStoneWeight([3,7,2]) == 2
	print("✅ All tests passed!")

if __name__ == "__main__":
    main()
