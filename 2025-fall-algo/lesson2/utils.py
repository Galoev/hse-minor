class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def push_front(head, x):
    node = ListNode(x)
    node.next = head
    head = node