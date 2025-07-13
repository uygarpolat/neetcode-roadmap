"""
Number of Connected Components in an Undirected Graph

https://neetcode.io/problems/count-connected-components?list=neetcode150

There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.

Example 1:

Input:
n=3
edges=[[0,1], [0,2]]

Output:
1
Example 2:

Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]

Output:
2
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
"""
from typing import List
from collections import defaultdict

class Solution:
	def countComponents(self, n: int, edges: List[List[int]]) -> int:

		visited = [False] * n
		paths = defaultdict(list)
		for left, right in edges:
			paths[left].append(right)
			paths[right].append(left)

		def dfs(node):
			for localNode in paths[node]:
				if not visited[localNode]:
					visited[localNode] = True
					dfs(localNode)

		result = 0
		for node in range(n):
			if not visited[node]:
				visited[node] = True
				dfs(node)
				result += 1

		return result

def main():
	solution = Solution()
	assert solution.countComponents(3, [[0,1],[0,2]]) == 1
	assert solution.countComponents(6, [[0,1], [1,2], [2,3], [4,5]]) == 2
	assert solution.countComponents(3, [[0,1],[0,2],[1,2]]) == 1
	assert solution.countComponents(12, [[0,1],[1,2],[2,3],[3,0],[4,5],[6,7],[8,9],[10,11]]) == 5
	assert solution.countComponents(6, [[0,1],[2,3],[4,5],[1,2],[3,4]]) == 1
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
