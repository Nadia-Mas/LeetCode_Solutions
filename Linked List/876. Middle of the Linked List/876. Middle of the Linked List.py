# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import math
class Solution:
    def middleNode(self, head: list[ListNode]) -> list[ListNode]:
        counter = 0
        res = head
        while res:
            counter +=1
            res = res.next
        middle = (counter//2)+1

        for i in range(middle-1):
            head = head.next
        return head