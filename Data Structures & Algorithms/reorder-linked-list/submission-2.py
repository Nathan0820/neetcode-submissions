# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 2 4 6 8 -> 2 8 4 6 -> (2, 4) and 
        # 1. Divide into 2 lists
        # 2. Reverse 2nd half
        # 3. Connect both list

        # 1)
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2)
        prev, cur = None, slow.next
        slow.next = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # (2,4,6) and (8)
        p1, p2 = head, prev
        while p2:
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p1, p2 = temp1, temp2




