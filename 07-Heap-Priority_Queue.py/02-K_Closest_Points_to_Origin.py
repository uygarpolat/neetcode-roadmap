"""
K Closest Points to Origin

https://neetcode.io/problems/k-closest-points-to-origin?list=neetcode150

You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order.

Example 1:

Input: points = [[0,2],[2,2]], k = 1

Output: [[0,2]]
Explanation : The distance between (0, 2) and the origin (0, 0) is 2. The distance between (2, 2) and the origin is sqrt(2^2 + 2^2) = 2.82842. So the closest point to the origin is (0, 2).

Example 2:

Input: points = [[0,2],[2,0],[2,2]], k = 2

Output: [[0,2],[2,0]]
Explanation: The output [2,0],[0,2] would also be accepted.

Constraints:

1 <= k <= points.length <= 1000
-100 <= points[i][0], points[i][1] <= 100
"""
from typing import List
import heapq, math

class Solution:
	def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
		result = []
		heapq.heapify(result)
		for x, y in points:
			dis = math.sqrt(pow(x,2)+pow(y,2))
			heapq.heappush(result, [-dis, [x,y]])
			if len(result) == k + 1:
				heapq.heappop(result)
		return [coordinate for _, coordinate in result]
    
def main():
    solution = Solution()
    assert solution.kClosest([[0,2],[2,2]], 1) == [[0,2]] or print(solution.kClosest([[0,2],[2,2]], 1)) or False
    assert solution.kClosest([[0,2],[2,0],[2,2]], 2) == [[0,2],[2,0]]
    print("✅ All tests passed!")

if __name__ == "__main__":
	main()
