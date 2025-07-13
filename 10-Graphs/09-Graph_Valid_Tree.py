
"""
Graph Valid Tree

https://neetcode.io/problems/valid-tree?list=neetcode150

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output:
true
Example 2:

Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

Output:
false
Note:

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2


Recommended Time & Space Complexity
You should aim for a solution as good or better than O(V + E) time and O(V + E) space, where V is the number vertices and E is the number of edges in the graph.
"""
from typing import List
from collections import defaultdict

class Solution:
	def validTree(self, n: int, edges: List[List[int]]) -> bool:

		visited = set()
		paths = defaultdict(list)

		for node1, node2 in edges:
			paths[node1].append(node2)
			paths[node2].append(node1)

		def dfs(node, parent):
			if node in visited:
				return False
			visited.add(node)
			for localNode in paths[node]:
				if localNode != parent:
					if not dfs(localNode, node):
						return False
			return True

		return dfs(0, None) and len(visited) == n

def main():
	solution = Solution()
	assert solution.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True
	assert solution.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False
	assert solution.validTree(4, [[0,1],[2,3]]) == False
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
