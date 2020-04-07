#Delete Middle Node
'''
Implement an algorithm to delete the node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.

Example:
Input: The Node c from the linked list a->b->c->d->e->f
Result: Nothing is returned, but the new linked list looks like a->b->d->e->f

Questions

My Idea
If we are given the node in the middle, then we can check if there's a node on the tail and if there's a prev node for the head.  If it's a singly linked list, then just remove the node if there's a tail, otherwise no op.

The weird part about this question is that we get the midpoint already, we don't need to search for it.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, node):
        self.head = node
        self.tail = node
    
    #O(1) T | O(1) S
    def add(self, node):
        tail = self.tail 
        tail.next = node
        self.tail = node 

    #O(1) T | No space S
    def deleteMidNode(self, mid):
        if mid is not None and mid.next is not None:
            mid.data = mid.next.data 
            mid.next = mid.next.next 
        else:
            return False

    #O(N) T | No space S
    def print(self):
        curr = self.head
        out = ""
        while curr is not None:
            out += curr.data + "->"
            curr = curr.next
        out += "%"
        print(out)

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
ll = LinkedList(a)
ll.add(b)
ll.add(c)
ll.add(d)
ll.add(e)
ll.add(f)
ll.print()
ll.deleteMidNode(c)
ll.print()