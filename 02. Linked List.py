# Singly Linked List
print("SINGLY LINKED LIST")
class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(5)
C = SinglyNode(2)

Head.next = A
A.next = B
B.next = C


# Traverse the list : O(n)
curr = Head
element = []
print(f"The SinglyLinked List:")
while curr:
    element.append(str(curr.val))
    curr = curr.next
print('->'.join(element))

# Search for a node: O(n)
val = int(input("Enter a value to search in linked list: "))
def search(Head):
    curr = Head
    while curr:
        if val == curr.val:
            return f"The value {curr.val} is present"
        curr = curr.next

    return f"Value {val} not present."

print(search(Head))
print("\n")


# Doubly Linked List
print("DOUBLY LINKED LIST")

class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)

head = tail = DoublyNode(1)
print(f"Head of Doubly linked list:{head}")
print(f"Tail of Doubly linked list:{tail}")


def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next

    print('<->'.join(elements))


# Insert at beginning - O(1)
def insert_at_beginning(head, tail, val):
    new_node = DoublyNode(val, next=head)
    head.prev = new_node
    return new_node, tail

head, tail = insert_at_beginning(head, tail, 3)
print("Doubly linked list after adding element.")
display(head)

# Insert at end: O(1)
def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node
    return tail, new_node

head, tail = insert_at_end(head, tail, 13)
print("Doubly linked list after adding element at end.")
display(head)
