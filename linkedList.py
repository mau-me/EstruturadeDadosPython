class Node(object):
    def __init__(self, data):
        
        self.data = data
        self.nextNode = None

class LinkedList(object):
    
    def __init__(self):
        
        self.head = None
        self.size = 0
    
    def insertStart(self, data):
        
        self.size += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def remove(self, data):

        if self.head is None:
            return
        
        self.size -= 1

        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode
        
        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode
    
    def size1(self):
        
        return self.size
    
    def size2(self):
        
        actualNode = self.head
        size = 0

        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode

        return size

    def insertEnd(self, data):
        
        self.size += 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        
        actualNode.nextNode = newNode

    def traverseList(self):

        actualNode = self.head


        while actualNode is not None:
            print("%d " % actualNode.data)
            actualNode = actualNode.nextNode



#Examples#

linkdList = LinkedList()

linkdList.insertStart(12)
linkdList.insertStart(122)
linkdList.insertStart(3)
linkdList.insertEnd(7)

linkdList.traverseList()
print(linkdList.size1())

print("\n ------------ \n")

linkdList.remove(122)
linkdList.traverseList()
print(linkdList.size1())

print("\n ------------ \n")

linkdList.remove(12)
linkdList.remove(3)
linkdList.remove(7)
linkdList.traverseList()
print(linkdList.size1())