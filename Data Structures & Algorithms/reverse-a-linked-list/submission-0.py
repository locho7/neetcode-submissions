# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return reverseListHelper(head, None)

def reverseListHelper(node, prev):
    if not node: return
    if node.next == None:
        node.next = prev
        return node
    next = node.next
    node.next = prev
    return reverseListHelper(next, node)
    
    