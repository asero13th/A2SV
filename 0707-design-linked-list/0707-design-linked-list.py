class Node:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if not self.head:
            return  -1
        counter = 0
        itr = self.head
        while itr:
            if counter == index:
                return itr.val
            itr = itr.next
            counter += 1
        return -1
    def addAtHead(self, val: int) -> None:
        node = Node(val,self.head)
        self.head = node
    def addAtTail(self, val: int) -> None:
        node = Node(val,None)
        if self.head == None:
            self.head = node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = node
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        itr = self.head
        counter = 0
        node = Node(val,None)
        while itr:
            if counter == index - 1:
                node.next = itr.next
                itr.next = node
                break
            itr = itr.next
            counter += 1
    def deleteAtIndex(self, index: int) -> None:
        tmp = self.head
        c = 0
        while tmp:
            tmp = tmp.next
            c += 1
        if index == 0 and self.head:
            self.head = self.head.next
        itr = self.head
        counter  = 0
        while  itr and 0 < index < c:
            if counter == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            counter += 1
            
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)