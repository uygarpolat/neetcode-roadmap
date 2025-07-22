"""
Alien Dictionary

https://neetcode.io/problems/foreign-dictionary?list=neetcode150

There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

The first letter where they differ is smaller in a than in b.
There is no index i such that a[i] != b[i] and a.length < b.length.
Example 1:

Input: ["z","o"]

Output: "zo"
Explanation:
From "z" and "o", we know 'z' < 'o', so return "zo".

Example 2:

Input: ["hrn","hrf","er","enn","rfnn"]

Output: "hernf"
Explanation:

from "hrn" and "hrf", we know 'n' < 'f'
from "hrf" and "er", we know 'h' < 'e'
from "er" and "enn", we know get 'r' < 'n'
from "enn" and "rfnn" we know 'e'<'r'
so one possibile solution is "hernf"
Constraints:

The input words will contain characters only from lowercase 'a' to 'z'.
1 <= words.length <= 100
1 <= words[i].length <= 100
"""
from typing import List
from collections import deque

class Solution:
	def foreignDictionary(self, words: List[str]) -> str:

		adj = {}
		for w in words:
			for c in w:
				adj[c] = set()

		indegree = {}
		for c in adj:
			indegree[c] = 0
		
		for i in range(len(words)-1):
			word1, word2 = words[i], words[i+1]
			localMin = min(len(word1), len(word2))
			if len(word1) > len(word2) and word1[:localMin] == word2[:localMin]:
				return ""
			for j in range(localMin):
				if word1[j] != word2[j]:
					if word2[j] not in adj[word1[j]]:
						adj[word1[j]].add(word2[j])
						indegree[word2[j]] += 1
					break

		q = deque([c for c in indegree if indegree[c] == 0])
		result = []
        
		while q:
			char = q.popleft()
			result.append(char)
			for neighbor in adj[char]:
				indegree[neighbor] -= 1
				if indegree[neighbor] == 0:
					q.append(neighbor)
        
		if len(result) != len(indegree):
			return ""
        
		return "".join(result)

def main():
	solution = Solution()
	assert solution.foreignDictionary(["z","o"]) == "zo"
	assert solution.foreignDictionary(["hrn","hrf","er","enn","rfnn"]) == "hernf"
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
