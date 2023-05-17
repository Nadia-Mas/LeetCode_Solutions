#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head:list[ListNode]) -> bool:
#Approach 1:      
        slow=head 
        fast=head
        
        while slow !=None and fast != None:
            slow=slow.next
            fast=fast.next
            if fast is None:
               continue
            else:
                fast=fast.next
            if slow==fast:
                return True
        
        return False
    
#Approach 2:               
        # if head is None:
        #     return False
        # if head.next is None:
        #     return False
        # while head.next is not None: 
        #     if head.val==None:
        #         return True 
        #     head.val=None
        #     head=head.next
        # return False
            
            
        