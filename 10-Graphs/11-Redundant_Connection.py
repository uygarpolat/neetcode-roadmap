"""
Redundant Connection

https://neetcode.io/problems/redundant-connection?list=neetcode150

You are given a connected undirected graph with n nodes labeled from 1 to n. Initially, it contained no cycles and consisted of n-1 edges.

We have now added one additional edge to the graph. The edge has two different vertices chosen from 1 to n, and was not an edge that previously existed in the graph.

The graph is represented as an array edges of length n where edges[i] = [ai, bi] represents an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the graph is still a connected non-cyclical graph. If there are multiple answers, return the edge that appears last in the input edges.

Example 1:

Input: edges = [[1,2],[1,3],[3,4],[2,4]]

Output: [2,4]
Example 2:

Input: edges = [[1,2],[1,3],[1,4],[3,4],[4,5]]

Output: [3,4]
Constraints:

n == edges.length
3 <= n <= 100
1 <= edges[i][0] < edges[i][1] <= edges.length
There are no repeated edges and no self-loops in the input.
"""
from typing import List
from collections import defaultdict

class Solution:
	def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

		paths = defaultdict(list)
		for left, right in edges:
			paths[left].append(right)
			paths[right].append(left)

		visited = [False] * (len(edges)+1)
		cycle = set()
		cycleStart = -1

		def dfs(node, parent):
			nonlocal cycleStart
			if visited[node]:
				cycleStart = node
				return True
			
			visited[node] = True
			for localNode in paths[node]:
				if localNode == parent:
					continue
				if dfs(localNode, node):
					if cycleStart != -1:
						cycle.add(node)
					if node == cycleStart:
						cycleStart = -1
					return True
			return False

		dfs(1,-1)
		
		for left, right in reversed(edges):
			if left in cycle and right in cycle:
				return [left,right]
			
		return []

def main():
	solution = Solution()
	assert solution.findRedundantConnection([[1,2],[1,3],[3,4],[2,4]]) == [2,4]
	assert solution.findRedundantConnection([[1,2],[1,3],[1,4],[3,4],[4,5]]) == [3,4]
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
