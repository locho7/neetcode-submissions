# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        pointer = dummy

        def mergeTwoListsHelper(l1, l2):
            nonlocal pointer
            if l1 is None or l2 is None: 
                pointer.next = l1 if l1 else l2
                return
            n1, n2 = l1.next, l2.next
            if l1.val <= l2.val:
                pointer.next = l1
                n2 = l2
            else: 
                pointer.next = l2
                n1 = l1   
            pointer = pointer.next          
            return mergeTwoListsHelper(n1, n2) 
            
        mergeTwoListsHelper(list1, list2)
        return dummy.next



