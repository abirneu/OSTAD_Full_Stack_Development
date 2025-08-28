### **Class 3: Linked Lists**

**Duration:** 90 minutes

---

### **Part 1: Theoretical Concepts**

#### **Types of Linked Lists**
*   **Singly Linked List:** A linear data structure where each node points to the next node, forming a chain.
*   **Doubly Linked List:** Similar to a singly linked list, but each node has pointers to both the next and previous nodes, allowing traversal in both directions.
*  **Circular Linked List:** The last node points back to the first node, forming a circle. This can be either singly or doubly linked.


**Singly Linked List:**
*   Each node contains two pieces of information: the actual data and a reference (or pointer) to the very next node.
*   The last node in the list has a reference that points to `None`, signaling the end.
*   **Key Characteristic:** You can only traverse it in one direction, from head to tail. It's a one-way street.

```
  Head
   |
  [ 10 | next ] --> [ 20 | next ] --> [ 30 | None ]
```

**Doubly Linked List:**
*   This is a more advanced train car. Each node contains three pieces of information: the data, a pointer to the **next** node, and a pointer to the **previous** node.
*   **Key Characteristic:** You can traverse it both forwards and backward. It’s a two-way street, which makes some operations, like deleting a node, more efficient.

```
      Head
       |
  [ 10 | next ] <--> [ 20 | next ] <--> [ 30 | None ]
  [ None | prev ]     [    | prev ]     [    | prev ]
```

**Operations: Insertion, Deletion, and Traversal**

*   **Traversal:** The act of visiting every node in the list. For a singly linked list, you start at the `head` and follow the `next` pointers until you hit `None`.
*   **Insertion:**
    *   **At the beginning:** Create a new node, point its `next` to the current head, and then update the list's `head` to be this new node. (Very fast, O(1)).
    *   **At the end:** You must first traverse the entire list to find the last node, then point its `next` to the new node. (Slower, O(n)).
*   **Deletion:**
    *   **From the beginning:** Simply update the `head` to point to the second node. (Very fast, O(1)).
    *   **From the middle/end:** You must traverse to find the node *before* the one you want to delete and update its `next` pointer to "skip over" the deleted node. (Slower, O(n)).

---

### **Part 2: Hands-On Activities**

#### **Activity 1: Write a Python Class for a Singly Linked List**

**Step 1: Create a Node Class**
*   Each node will have `data` and a `next` pointer.
```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
```

**Step 2: Traverse and Print the List**
```python
def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

```
## Let's create a few nodes and link them together

```python
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)
```
### Delete a Node from the List
```python
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
```

### Let's delete node4 
```python
# Delete node4
node1 = deleteSpecificNode(node1, node4)

print("\nAfter deletion:")
traverseAndPrint(node1)
```
### Insert a Node at a Specific Position
```python
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
```

### Let's insert a new node with value 5 at position 3
```python
newNode = Node(5)
node1 = insertNodeAtPosition(node1, newNode, 3)
print("\nAfter inserting 5 at position 3:")
traverseAndPrint(node1)
```

