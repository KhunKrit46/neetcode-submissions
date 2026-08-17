class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0 

    def get(self, index: int) -> int:
        if self.size <= index: 
            return -1
        else: 
            pointer = self.head
            for i in range(index): 
                pointer = pointer.next
            return pointer.val
        
    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        if not self.head: 
            self.head = new
            self.size += 1 
        else: 
            new.next = self.head
            self.head = new
            self.size += 1 

    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        pointer = self.head
        for i in range(self.size-1): 
            pointer = pointer.next
        pointer.next = new
        self.size += 1 

    def addAtIndex(self, index: int, val: int) -> None:
        pointer = self.head
        for i in range(index-1): 
            pointer = pointer.next
        oldNext = pointer.next
        pointer.next = ListNode(val)
        pointer = pointer.next
        pointer.next = oldNext
        self.size += 1 

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        pointer = self.head
        for i in range(index-1): 
            pointer = pointer.next
        pointer.next = pointer.next.next
        self.size -= 1
class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)