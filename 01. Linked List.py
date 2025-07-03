# Singly Linked List

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
            print(f"The value {curr.val} is present")
        curr = curr.next

    return f"Value {val} not present."

print(search(Head))
