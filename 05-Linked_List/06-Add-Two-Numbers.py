"""
Add Two Numbers

https://neetcode.io/problems/add-two-numbers

You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

Example 1:

Input: l1 = [1,2,3], l2 = [4,5,6]

Output: [5,7,9]

Explanation: 321 + 654 = 975.
Example 2:

Input: l1 = [9], l2 = [9]

Output: [8,1]
Constraints:

1 <= l1.length, l2.length <= 100.
0 <= Node.val <= 9
"""
from typing import Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def build_linked_list(vals: list[int]) -> Optional[ListNode]:
	dummy = ListNode()
	curr = dummy
	for v in vals:
		curr.next = ListNode(v)
		curr = curr.next
	return dummy.next

def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		head = ListNode()
		curr = head
		carry = 0
		counter = 0
		while l1 or l2 or carry > 0:
			val1 = l1.val if l1 else 0
			val2 = l2.val if l2 else 0
			curr.val = (val1 + val2 + carry) % 10
			carry = (val1 + val2 + carry) // 10
			counter += 1
			l1 = l1.next if l1 else None
			l2 = l2.next if l2 else None
			if l1 or l2 or carry > 0:
				curr.next = ListNode()
				curr = curr.next			
		return head

def main():
	solution = Solution()
     
	l1 = build_linked_list([1,2,3])
	l2 = build_linked_list([4,5,6])
	total_list = solution.addTwoNumbers(l1, l2)
	total = linked_list_to_list(total_list)
	assert total == [5,7,9] or print(total) or False
	
	l1 = build_linked_list([9])
	l2 = build_linked_list([9])
	total_list = solution.addTwoNumbers(l1, l2)
	total = linked_list_to_list(total_list)
	assert total == [8,1] or print(total) or False
	print("✅ All tests passed!")

if __name__ == "__main__":
	main()
