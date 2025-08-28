# Linked List Node class definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# A function to traverse the linked list and print its elements
def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")


# Delete a specific node from the linked list
def deleteSpecificNode(head, nodeToDelete):
    if head == nodeToDelete:
        return head.next

    currentNode = head
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next

    if currentNode.next is None:
        return head

    currentNode.next = currentNode.next.next
    return head


# Insert a new node at a specific position in the linked list
def insertNodeAtPosition(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode

    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode
    return head


node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deletion:")
traverseAndPrint(node1)

# Delete node4
node1 = deleteSpecificNode(node1, node4)

print("\nAfter deletion:")
traverseAndPrint(node1)

# Insert a new node with value 97 at position 2
newNode = Node(97)
node1 = insertNodeAtPosition(node1, newNode, 2)

print("\nAfter insertion:")
traverseAndPrint(node1)
