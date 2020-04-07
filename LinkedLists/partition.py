#Partition
'''
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.  If x is contained within the list, the values of x only need to be after the elements less than x (see below).  The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.

Example:
Input:  3->5->8->5->10->2->1 [partition = 5]
Output: 3->1->2->10->5->5->8 

Questions?
- Is this single or double?
- Can we use a buffer?
- Does partition belong to the LinkedList class or is it a stand alone function?

My idea
Find the midpoint of the ll, which would be 5 (or I suppose last instance of it)
5 is the midpoint, so partition around it means cut at that point

3-5-8-5
10-2-1

Now we have two linked lists, left (L) and right (R)

sort each list (L & R)
3-5-8-5
3-5-5-8

10-2-1
1-2-10

put back together, insert right (R) after head before partition, may have to pop to preserve sorted order.

3-1-2-10-5-5-8
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None 

class LinkedList:
    def __init__(self, node=None):
        if node is not None:
            self.head = node 
            self.tail = node 
            self.length = 1
        else: 
            self.head = None
            self.tail = None
            self.length = 0

    def add(self, node):
        if self.head is not None:
            tail = self.tail 
            tail.next = node
        else:
            self.head = node

        self.tail = node
        self.length += 1

    def insertAfterHead(self, node):
        if self.head is not None:
            nextNode = self.head.next 
            self.head.next = node 
            node.next = nextNode
        else:
            self.head = node
            self.tail = node 
        self.length += 1
        

    def addMany(self, list):
        for i in range(0, len(list)):
            self.add(list[i])

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

    #ideally you'd want to remove the node, but data is okay for here
    def remove(self, data):
        current = self.head 
        while current is not None:
            if current.data == data: 
                current.data = current.next.data 
                current.next = current.next.next 
            current = current.next 
    
    #could write a pop method here
    def pop(self):
        current = self.head 
        tail = self.tail
        while current is not None:
            if current.next is not None:
                if current.next.data == tail.data:
                    #destroy the tail
                    current.next = None
                    self.tail = current
                    return tail
            else:
                #can't pop last element, just return it
                self.tail = current
                return current
            current = current.next
    
    def getLength(self):
        return self.length

    def sort(self):
        curr1 = self.head
        while curr1 is not None:
            curr2 = self.head
            while curr2.next is not None:
               # print(curr1.data, curr2.data)
                 # 8  > 5
                if curr2.data > curr2.next.data:
                    tempdata = curr2.data #8
                    curr2.data = curr2.next.data #5
                    curr2.next.data = tempdata #8
                curr2 = curr2.next 
            curr1 = curr1.next

    def print(self):
        current = self.head 
        out = ""
        while current is not None:
            out += str(current.data) + "->"
            current = current.next 
        out += "%"
        print(out)


ll = LinkedList()
ll.addMany([Node(3), Node(5), Node(8), Node(5), Node(10), Node(2), Node(1)])
ll.print()

def partition(ll, el):
    #iterate thru ll, find last instance of partition el.
    def find_last_partition_index(el):
        current = ll.getHead() 
        count = 1 
        found = 0
        while current is not None:
            #find last instance of partition
            if current.data == el: 
                found = count
            count += 1
            current = current.next 
        return found
    
    idx = find_last_partition_index(5)

    #divide list into two parts, left (L) and right (R) around partition point
    leftLL = LinkedList()
    curr = ll.getHead()
    for i in range(1, idx+1):
        leftLL.add(Node(curr.data))
        curr = curr.next 
    
    rightLL = LinkedList()
    for i in range(idx+1, ll.getLength()+1):
        rightLL.add(Node(curr.data))
        curr = curr.next

    # leftLL.print()
    # rightLL.print()  

    #now sort each list
    leftLL.sort()
    rightLL.sort()                


    #finally join them back together, right is inserted after left's head.
    
    # tempList = []
    # for i in range(0, rightLL.getLength()):
    #     tempList.append(Node(curr.data))
    #     curr = curr.next 
  
    #now pop them to preserve sorted order
    # for i in range(0, len(tempList)):
    #     leftLL.insertAfterHead(tempList.pop())

    #pop the right list to preserve sort order and insert after head
    for i in range(0, rightLL.getLength()):
        node = rightLL.pop()
        if node is not None:
            leftLL.insertAfterHead(node)

    p = leftLL
    p.print()

partition(ll, 5)
