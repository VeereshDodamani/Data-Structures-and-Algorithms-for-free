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
