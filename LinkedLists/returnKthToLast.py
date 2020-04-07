#Return Kth to Last
'''
Implement an algorithm to find the kth to last element of a singly linked list

Questions
- Is this singly or doubly linked?

My idea:
Kth to last element would just mean N-K away from N,
so 3 from 10 (N=10) would be item 7.
To keep track of N, we can add a counter to the LinkedList that gets updated each time a node is added.
First determine K away to get position P, then loop thru linked list til found P.
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
        self.length = 1

    #O(P) or O(N-K) T | No extra space S
    def getKthToLast(self, k):
        p = self.length - k
        current = self.head
        i = 1
        while i < p:
            if current is not None:
                current = current.next
                i += 1
            else: 
                return False;
        
        return current.data

    #O(1) T | O(1) S
    def add(self, node):
        tail = self.tail
        tail.next = node
        self.tail = node
        self.length += 1
        
    #O(N) T | No extra space S
    def print(self):
        current = self.head
        out = ""
        while current is not None:
            out += current.data + "->"
            current = current.next
        out += "%"
        print(out)

ll = LinkedList(Node(1))
ll.add(Node(2))
ll.add(Node(3))
ll.add(Node(4))
ll.add(Node(5))
print(ll.getKthToLast(2))
