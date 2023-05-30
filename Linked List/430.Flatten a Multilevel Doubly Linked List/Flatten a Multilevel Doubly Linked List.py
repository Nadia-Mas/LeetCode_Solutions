
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: list[Node]) -> list[Node]:
        parents = []
        pa = head
        while pa:      
            if pa.child:     
                pa.next and parents.append(pa.next)
                pa.next = pa.child
                pa.next.prev = pa
                pa.child = None   
            elif not pa.next and len(parents)>0:
                pa.next= parents.pop()
                pa.next.prev = pa     
            pa = pa.next  
        return head