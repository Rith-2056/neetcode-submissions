# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #SPlit using fast/slow pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #Get the second half of ll
        l2 = slow.next
        slow.next = None
        #Reverse it
        prev2, curr = None, l2
        while curr:
            tmp = curr.next
            curr.next = prev2
            prev2 = curr
            curr = tmp
        h1 = head
        h2 = prev2
        while h2:
            next1 = h1.next
            next2 = h2.next
            h1.next = h2
            h2.next = next1
            h1 = next1
            h2 = next2
