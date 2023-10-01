from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        return f"[{self.val}]->{self.next}"

def arrayToLinkedList(numbers):
    head = ListNode(0)
    cur = head

    for n in numbers:
        node = ListNode(n)
        cur.next = node
        cur = cur.next
    
    return head.next



# def mergeTwoLists(self, list1: Opitional[ListNode], list2: Optional[ListNode]) -> ListNode:
#     head = ListNode()
#     cur = head

#     while list1 and list2:
#         if list1.val < list2.val:
#             cur.next = list1
#             list1 = list1.next
#         else:
#             cur.next = list2
#             list2 = list2.next
        
#         cur = cur.next
    
#     if list1:
#         cur.next = list1

#     if list2:
#         cur.next = list2
    
#     return head.next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        result = ListNode(0, head)
        current = result

        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return result.next

# 0 7 7 
# c

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)
    
    node1.next = node2
    node2.next = node3
    print(node1)

    numbers = [1, 2, 3, 4]
    head = arrayToLinkedList(numbers)
    print(head)
    # 1 -> 2 -> 3 -> 4
