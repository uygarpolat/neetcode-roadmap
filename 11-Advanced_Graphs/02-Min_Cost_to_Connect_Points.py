"""
Min Cost to Connect Points

https://neetcode.io/problems/min-cost-to-connect-points?list=neetcode150

You are given a 2-D integer array points, where points[i] = [xi, yi]. Each points[i] represents a distinct point on a 2-D plane.

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between the two points, i.e. |xi - xj| + |yi - yj|.

Return the minimum cost to connect all points together, such that there exists exactly one path between each pair of points.

Example 1:

Input: points = [[0,0],[2,2],[3,3],[2,4],[4,2]]

Output: 10
Constraints:

1 <= points.length <= 1000
-1000 <= xi, yi <= 1000
"""

from typing import List

class DSU:
	def __init__(self, n):
		self.parent = list(range(n))
		self.rank   = [0] * n

	def find(self, x):
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]
	
	def union(self, a, b):
		ra = self.find(a)
		rb = self.find(b)
		if ra == rb:
			return False

		if self.rank[ra] < self.rank[rb]:
			self.parent[ra] = rb
		elif self.rank[rb] < self.rank[ra]:
			self.parent[rb] = ra
		else:
			self.parent[rb] = ra
			self.rank[ra] += 1

		return True

class Solution:
	
	def minCostConnectPoints(self, points: List[List[int]]) -> int:

		edges = []
		n = len(points)

		for i in range(n):
			for j in range(i+1, n):
				weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
				edges.append((weight, i, j))

		edges.sort()

		dsu = DSU(n)
		total_cost = 0
		edges_used = 0

		for w, i, j in edges:
			if dsu.union(i, j):
				total_cost += w
				edges_used += 1
				if edges_used == n - 1:
					break

		return total_cost
    
def main():
	solution = Solution()
	assert solution.minCostConnectPoints([[0,0],[2,2],[3,3],[2,4],[4,2]]) == 10
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
