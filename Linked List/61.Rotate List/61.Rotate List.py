# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: list[ListNode], k: int) -> list[ListNode]:
        
        size=0
        res=head
        while res :
            size+=1
            res=res.next
        pa=head 
        if head is None:return
        
        if k>=size : 
            k=k%size
            
        if k==0 : return head
        
        for i in range (k):
            while pa.next:
                pb=pa
                pa=pa.next
            if size>1:
                pb.next=pa.next
                pa.next=head
                head=pa
            else:
                return head
        return head