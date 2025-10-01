# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.
# Leetcode probelm: 876
print("Way-1")
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for num in arr[1:]:
        curr.next = ListNode(num)
        curr = curr.next
    return head

def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def linkedlist_to_array(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

head = array_to_linkedlist([1,2,3,4,5])
mid = middleNode(head)
output = linkedlist_to_array(mid)
print(output)
