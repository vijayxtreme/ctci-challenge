#RemoveDups
'''
Remove dups from an unsorted linked list.  
How would you solve this problem if a temporary buffer is not allowed?

Questions:
- Can I assume that 2 is different from "2"?
- Are we allowing any types to be in LinkedList or is it strict?
- Is this a doubly linked list or singly linked list?

My Idea:
Fill up this linkedlist with different values
Go through each node.  If we can use a buffer we can store each node visited.  If the node matches what's already in our buffer, we can remove it.  

To remove a node, simply just set its current data (value) to the next node, and its next pointer to the next node's pointer.
If it's a doubly linked list then we just want to also update the prev's node's next to be the current node's next, as well as make the curr node's next's prev be the prev node.  A little confusing but that's the gist.  Same with setting the values.

If we don't have a buffer, then we may need to run a double while loop, one that looks at every node then a second loop that runs ahead and looks at every other node; compares it.  This would be O(N^2).

'''
from collections import defaultdict


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

    #O(1) helper method
    def remove(self, node):
        if node.next is not None:
            node.data = node.next.data 
            node.next = node.next.next
        else:
            node.data = None
            node.next = None

    # O(N)
    def removeNode(self, node):
        current = self.head 
        while current is not None:
            #it might be smarter to have a node id
            if current.data == node.data:
                self.remove(current)
                break;
            current = current.next
    #O(1)
    def getHeadValue(self):
        print(self.head.data)

    #Answer with a buffer
    def removeDups(self):
        d = defaultdict(lambda : 0)
        current = self.head 
        while current is not None: 
            if d[current.data] == current.data:
                self.remove(current)
            d[current.data] = current.data
            current = current.next                

    #Answer without a buffer O(N^2)
    def removeDupsNoBuffer(self):
        i = self.head
        while i is not None:
            j = i.next
            while j is not None:
                if i.data == j.data:
                    self.remove(j)
                j = j.next
            i = i.next

    #O(N)
    def print(self):
        next = self.head
        out = ""
        while next is not None:
            if next.data is not None:
                out += (str(next.data) + "->")
            next = next.next
        out += "%"
        print(out)

n = Node(1)
ll = LinkedList(n)
ll.add(Node(2))
ll.add(Node(2))
ll.add(Node(3))
ll.add(Node(1))
ll.add(Node(0))
ll.add(Node(4))
ll.add(Node(3))
ll.print()
ll.removeDupsNoBuffer()
ll.print()



