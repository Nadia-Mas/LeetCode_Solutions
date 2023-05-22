# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: list[ListNode]) -> list[ListNode]:
    
        last, current = None, head
        
        while current:
            temp = current.next
            current.next = last
            last = current
            current = temp
        return last