# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def oddEvenList(self, head: list[ListNode]) -> list[ListNode]:
#Approach 01
        
        if not head or not head.next:
            return head
        
        po, pe  = head, head.next
        pe_head = pe

        while pe and pe.next:
            po.next = pe.next
            po = po.next
            
            pe.next = po.next
            pe = pe.next
        
        po.next = pe_head
        
        return head


#Approach 02
#        if not head or not head.next:
#            return head
#         po, pe  = head, head.next
#         pe_head = pe
        
#         while pe and pe.next:
#             po.next = po.next.next
#             po = po.next
            
#             pe.next = pe.next.next
#             pe = pe.next
        
#         po.next = pe_head
        
#         return head