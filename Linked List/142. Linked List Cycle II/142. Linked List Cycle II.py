#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head:list[ListNode]) -> list[ListNode]:
#Approach 1        
        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         break
        # else:
        #     return None
        # while head != slow:
        #     slow = slow.next
        #     head = head.next
        # return head  
#Approach 2
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:    #Cycle detected
                fast = head
                while fast is not slow:
                    fast = fast.next
                    slow = slow.next
                return fast