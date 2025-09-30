# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Leetcode problem: 19


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linkedlist(lst):
    dummy = ListNode(0)
    cur = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next

def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    ahead = behind = dummy

    for _ in range(n + 1):
        ahead = ahead.next

    while ahead:
        ahead = ahead.next
        behind = behind.next

    behind.next = behind.next.next
    return dummy.next

def print_linkedlist(head):
    cur = head
    while cur:
        print(cur.val, end=" ")
        cur = cur.next
    print()

head_list = [1, 2, 3, 4, 5]
n = 2
print("Given Head: ",head_list)
print("Nth node: ",n)
head = list_to_linkedlist(head_list)
new_head = removeNthFromEnd(head, n)
print_linkedlist(new_head)
