# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = head
        length  = 0
        while cur:
            length += 1
            cur = cur.next
        #travel to the (length - n - 1)st node
        cur1 = dummy
        for i in range(length - n):
            cur1 = cur1.next
        cur1.next = cur1.next.next
        return dummy.next