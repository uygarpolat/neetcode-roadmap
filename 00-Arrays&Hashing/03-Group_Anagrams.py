"""
Group Anagrams

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
"""
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        book = defaultdict(list)
        base = ord('a')
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c)-base] += 1
            key = tuple(count)
            book[key].append(str)
        return list(book.values())
    
def main():
    solution = Solution()
    strs = ["act","pots","tops","cat","stop","hat"]
    result = solution.groupAnagrams(strs)
    print(result) # [["hat"],["act", "cat"],["stop", "pots", "tops"]]
    
    strs = ["x"]
    result = solution.groupAnagrams(strs)
    print(result) # [["x"]]
    
    strs = [""]
    result = solution.groupAnagrams(strs)
    print(result) # [['']]
    
if __name__ == "__main__":
    main()
