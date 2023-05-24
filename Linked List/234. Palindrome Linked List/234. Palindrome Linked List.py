# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: list[ListNode]) -> bool:
        #Approach 01
        arr = []
        current = head
        
        while current:
            arr.append(current.val)
            current = current.next
            
        if arr == arr[::-1]: 
            return True
        else:
            return False
        

        #Approach 01
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
    
#         prev = None
#         while slow:
#             temp = slow.next
#             slow.next = prev
#             prev = slow
#             slow = temp
        
#         while head and prev:
#             if head.val != prev.val:
#                 return False
#             else:
#                 head = head.next
#                 prev = prev.next
#         return True
        