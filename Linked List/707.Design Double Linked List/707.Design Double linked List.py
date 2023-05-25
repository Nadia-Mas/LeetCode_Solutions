class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        add = Node(val)
        if self.size == 0:
            add.next = None
            self.tail = add
        else:
            add.next = self.head
            self.head.prev = add
        add.prev = None
        self.head = add
        
        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        add = Node(val)
        if self.size == 0:
            add.prev = None
            self.head = add
        else:
            add.prev = self.tail
            self.tail.next = add
        add.next = None
        self.tail = add    

        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            add = Node(val)
            prev = self.head
            for _ in range(index-1):
                prev = prev.next
            next_ = prev.next
            add.prev = prev
            add.next = next_
            prev.next = add
            next_.prev = add
            self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or index >= self.size:
            return
        cur = self.head
        for _ in range(index):
            cur = cur.next
        if self.size == 1:
            self.head = None
            self.tail = None
        elif cur is self.head:
            cur.next.prev = cur.prev
            self.head = cur.next
        elif cur is self.tail:
            cur.prev.next = cur.next
            self.tail = cur.prev
        else:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            
        self.size -= 1