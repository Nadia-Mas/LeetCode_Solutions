# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head:list(ListNode), n: int) -> list(ListNode):
        
        slow, fast = head, head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head