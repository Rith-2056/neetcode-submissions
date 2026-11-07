# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        l3 = dummy
        cur1, cur2 = list1, list2
        while cur1 and cur2:
            if cur1.val < cur2.val:
                l3.next = cur1
                cur1 = cur1.next
            else:
                l3.next = cur2
                cur2 = cur2.next
            l3 = l3.next
        if cur1:
            l3.next = cur1
        else:
            l3.next = cur2
        return dummy.next