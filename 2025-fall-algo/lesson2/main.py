class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(0)
first_element = head

second_element = ListNode(1)
first_element.next = second_element

third_element= ListNode(2)
second_element.next = third_element


def print_linked_list(head):
    cur = head
    while cur != None:
        print(cur.val, end='->')
        cur = cur.next
    print('None')

def len_linked_list(head):
    count = 0
    cur = head
    while cur != None:
        count += 1
        cur = cur.next
    
    return count

def push_back(head, val):
    prev = None
    cur = head
    while cur != None:
        prev = cur
        cur = cur.next
    
    node = ListNode(val)
    prev.next = node

def push_front(head, val):
    node = ListNode(val)
    node.next = head
    return node



def remove_tail(head):
    prev = None
    cur = head
    while cur.next != None:
        prev = cur
        cur = cur.next
    
    prev.next = None

def remove_val(head, val):
    prev = None
    cur = head
    while cur.val != val:
        prev = cur
        cur = cur.next
    
    prev.next = cur.next

print_linked_list(head)
remove_val(head, 1)
print_linked_list(head)

