"""
Reverse Nodes in K-Group

https://neetcode.io/problems/reverse-nodes-in-k-group?list=neetcode150

You are given the head of a singly linked list head and a positive integer k.

You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.

Return the modified list after reversing the nodes in each group of k.

You are only allowed to modify the nodes' next pointers, not the values of the nodes.

Example 1:

Input: head = [1,2,3,4,5,6], k = 3

Output: [3,2,1,6,5,4]
Example 2:

Input: head = [1,2,3,4,5], k = 3

Output: [3,2,1,4,5]
Constraints:

The length of the linked list is n.
1 <= k <= n <= 100
0 <= Node.val <= 100
"""
from typing import Optional

class ListNode:
	def __init__(self, val: int=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		
		def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
			prev, curr = None, head
			while curr:
				nxt = curr.next
				curr.next = prev
				prev = curr
				curr = nxt
			return prev

		dummy = ListNode(0)
		dummy.next = head
		group_prev = dummy

		while True:
			kth = group_prev
			for _ in range(k):
				kth = kth.next
				if not kth:
					return dummy.next

			group_start = group_prev.next
			next_group = kth.next
			kth.next = None

			new_group_head = reverseList(group_start)

			group_prev.next = new_group_head
			group_start.next = next_group

			group_prev = group_start
