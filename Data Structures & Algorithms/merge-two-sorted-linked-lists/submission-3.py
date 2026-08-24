# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        l3 = dummy
        h1, h2 = list1, list2
        while h1 and h2:
            if h1.val < h2.val:
                l3.next = h1
                h1 = h1.next
            else:
                l3.next = h2
                h2 = h2.next
            l3 = l3.next
        if h1:
            l3.next = h1
        else:
            l3.next = h2
        return dummy.next