# Definition for doubly-linked list.
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.has = {}
        self.head = None
        self.last = None
    def add(self, node):
        if self.head is None:
            self.head = node
            self.last = node
        else:
            prev = self.last
            prev.next = node
            node.prev = prev
            self.last = node
    def remove(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.last = node.prev
        else:
            node.next.prev = node.prev
    
        node.prev = None
        node.next = None
        
        

    def get(self, key: int) -> int:
        if self.has.get(key) is None:
            return -1
        curr = self.has.get(key)
        value = curr[0]
        ptr = curr[1]
        self.remove(ptr)
        newPtr = Node(key)
        self.add(newPtr)
        self.has.update({key: [value, newPtr]})
        return value
        

    def put(self, key: int, value: int) -> None:
        if self.head is None:
            self.size += 1
            ptr = Node(key)
            self.add(ptr)
            self.has.update({key: [value, ptr]})
        elif self.has.get(key) is None:
            if self.capacity > self.size:
                self.size += 1
                ptr = Node(key)
                self.add(ptr)
                self.has.update({key: [value, ptr]})
            else:
                headNode = self.head
                self.has.pop(headNode.key)
                self.remove(headNode)
                ptr = Node(key)
                self.add(ptr)
                self.has.update({key: [value, ptr]})
        else:
            newNode = Node(key)
            curr = self.has.get(key)
            ptr = curr[1]
            self.remove(ptr)
            self.add(newNode)
            self.has.update({key: [value, newNode]})
            
            

        


        
