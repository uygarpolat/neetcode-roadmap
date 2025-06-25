"""
Copy Linked List with Random Pointer

https://neetcode.io/problems/copy-linked-list-with-random-pointer

You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.

Create a deep copy of the list.

The deep copy should consist of exactly n new nodes, each including:

The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node
Note: None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

Example 1:

Input: head = [[3,null],[7,3],[4,0],[5,1]]

Output: [[3,null],[7,3],[4,0],[5,1]]
Example 2:

Input: head = [[1,null],[2,2],[3,2]]

Output: [[1,null],[2,2],[3,2]]
Constraints:

0 <= n <= 100
-100 <= Node.val <= 100
random is null or is pointing to some node in the linked list.
"""
from typing import Optional

class Node:
	def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
		self.val = int(x)
		self.next = next
		self.random = random
        
class Solution:
	def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
		if not head:
			return None
		old_to_new = {}
		curr = head
		while curr:
			old_to_new[curr] = Node(curr.val)
			curr = curr.next
		curr = head
		while curr:
			copy = old_to_new[curr]
			copy.next = old_to_new.get(curr.next)
			copy.random = old_to_new.get(curr.random)
			curr = curr.next
		return old_to_new[head]
