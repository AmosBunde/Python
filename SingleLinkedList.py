class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head =None

    def listPrint(self):
        output = self.head
        while output is not None:
            print(output.data)
            output = output.next


listOne = SingleLinkedList()
listOne.head = Node('Monday')
nodeTwo = Node('Tuesday')
nodeThree = Node('Wednesday')
nodeFour = Node('Thursday')
nodeFive = Node('Friday')
nodeSix= Node('Saturday')
nodeSeven= Node('Sunday')
listOne.head.next = nodeTwo
nodeTwo.next = nodeThree
nodeThree.next = nodeFour
nodeFour.next = nodeFive
nodeFive.next = nodeSix
nodeSix.next =nodeSeven

listOne.listPrint()