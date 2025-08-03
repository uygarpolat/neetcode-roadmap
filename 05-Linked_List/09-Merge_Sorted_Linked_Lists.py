"""
Merge K Sorted Linked Lists

https://neetcode.io/problems/merge-k-sorted-linked-lists?list=neetcode150

You are given an array of k linked lists lists, where each list is sorted in ascending order.

Return the sorted linked list that is the result of merging all of the individual linked lists.

Example 1:

Input: lists = [[1,2,4],[1,3,5],[3,6]]

Output: [1,1,2,3,3,4,5,6]
Example 2:

Input: lists = []

Output: []
Example 3:

Input: lists = [[]]

Output: []
Constraints:

0 <= lists.length <= 1000
0 <= lists[i].length <= 100
-1000 <= lists[i][j] <= 1000
"""
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
	def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

		if not lists:
			return None

		def merge_two_ordered_linked_lists(list1, list2):
			l1 = list1
			l2 = list2
			dummy = ListNode()
			curr = dummy
			while l1 and l2:
				if l1.val < l2.val:
					curr.next = l1
					l1 = l1.next
				else:
					curr.next = l2
					l2 = l2.next
				curr = curr.next
			curr.next = l1 or l2
			return dummy.next
		
		for i in range(1, len(lists)):
			lists[i] = merge_two_ordered_linked_lists(lists[i], lists[i-1])
		return lists[-1]