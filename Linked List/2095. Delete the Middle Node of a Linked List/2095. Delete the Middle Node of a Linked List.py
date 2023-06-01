# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: list[ListNode]) -> list[ListNode]:
    
        counter = 0
        res = head
        while res:
            counter +=1
            res = res.next

        if counter<=1: return None
             
        middle = (counter//2)+1
        

        temp =head
        for i in range(middle-2):
            temp = temp.next

        temp.next = temp.next.next

        return head