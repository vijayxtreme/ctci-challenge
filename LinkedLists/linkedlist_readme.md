# Markdown

## Basic Linked List 

Should take a node
Can be singly linked 
Better if doubly linked
Has head
Has tail
Can add to the list
Can print the list

```python
class Node:
    def __init__(self, data):
        self.data = data 
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self, node):
        self.head = node
        self.tail = node

    #O(1)  
    def add(self, node):
        tail = self.tail
        tail.next = node
        self.tail = node

    # O(N)
    def removeNode(self, node):
        current = self.head 
        while current is not None:
            #it might be smarter to have a node id
            if current.data == node.data:
                current.data = current.next.data
                current.next = current.next.next
                break;
            current = current.next
    #O(1)
    def getHeadValue(self):
        print(self.head.data)

    #O(N)
    def print(self):
        next = self.head
        out = ""
        while next is not None:
            out += (str(next.data) + "->")
            next = next.next
        out += "%"
        print(out)

n = Node("hello")
ll = LinkedList(n)
ll.add(Node("I'm"))
ll.add(Node("Vijay"))
ll.removeNode(Node("I'm"))
ll.print()
ll.getHeadValue()
```

