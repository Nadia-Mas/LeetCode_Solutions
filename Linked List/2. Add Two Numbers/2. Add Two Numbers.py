# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       
        #Approach 01
#         head = ListNode()
#         current = head
#         carry = 0
#         while (l1 != None or l2 != None or carry != 0):
#             l1_value = l1.val if l1 else 0
#             l2_value = l2.val if l2 else 0
#             total = l1_value + l2_value + carry
#             current.next = ListNode(total % 10)
#             carry = total // 10
            
#             # Move list pointers forward
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#             current = current.next
#         return head.next
    
        #Approach 02
        d = n = ListNode(0)
        num1 = num2 = ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        res = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        print(res)
        for i in res:
            d.next = ListNode(i)
            d = d.next
        return n.next  
    
