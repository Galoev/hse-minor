class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Шаг 1: Создание головы списка
first_node = ListNode(42)  # Голова списка, значение = 1
# Список выглядит так: 1 --> None

# Шаг 2: Добавление второго узла
second_node = ListNode(14)  # Второй узел, значение = 2
first_node.next = second_node    # Связываем первый узел со вторым
# Список выглядит так: 1 --> 2 --> None

# Шаг 3: Добавление третьего узла
third_node = ListNode(7)   # Третий узел, значение = 3
second_node.next = third_node  # Связываем второй узел с третьим
# Список выглядит так: 1 --> 2 --> 3 --> None

# Шаг 4: Добавление четвертого узла
fourth_node = ListNode(53)  # Четвертый узел, значение = 4
third_node.next = fourth_node  # Связываем третий узел с четвертым


def print_linked_list(head: ListNode):
    current = head # 1

    while current != None:
        print(current.val, end=" --> ") 
        current = current.next
    
    print("None")



# Список выглядит так: 42 --> 14 --> 7 --> 53 --> None
def get_linked_list_lenght(head: ListNode):
    count = 0
    current = head

    while current != None:
        count += 1
        current = current.next

    return count


# Список выглядит так:
# 42 --> 14 --> 7 --> 53 --> new_node --> None
# h                  cur    cur.next
# 


def append_to_tail(head: ListNode, value: int):
    current = head

    while current.next != None:
        current = current.next
    
    new_node = ListNode(value)

    current.next = new_node
    
    return head


new_linked_list = ListNode(1)
new_linked_list = append_to_tail(new_linked_list, 2)
new_linked_list = append_to_tail(new_linked_list, 3)
new_linked_list = append_to_tail(new_linked_list, 4)
# print_linked_list(new_linked_list)

# 1 -> 2 -> 3 -> 4 -> None
# 0    1    2    3
# 42 2
# 1 -> 2 -> 42 -> 3 -> 4 -> None



# 1 -> 2 -> 3 -> 4 -> None
#     cur  cur.next

# 1 -> 2 -> 3 -> 4 -> None
#     cur  cur.next
# tmp = cur.next # 3 -> 4 -> None

# 1 -> 2 -> 42 -> None
#     cur  cur.next cur.next.next
# cur.next = new_node 

# 1 -> 2 -> 42   ->   3 -> 4 -> None
#     cur cur.next cur.next.next
# cur.next.next = tmp


# 42 -> None
# nn     nn.next

# nn.next = cur.next
# 42 -> 3 -> 4 -> None
# nn
# cur.next = new_node
# 1 -> 2 -> 42 -> 3 -> 4 -> None

def insert_by_index(head: ListNode, value: int, index: int):
    current = head
    
    while index != 1:
        current = current.next
        index -= 1
    
    new_node = ListNode(value)
    new_node.next = current.next
    current.next = new_node

    return head

# Определение двусвязного списка.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None
# 1 - 2 - 3 - 4
#     e   s    


# Шаг 1: Создание головы списка (первый узел)
dd_head = ListNode(1)  # Узел со значением 1
# Структура: None <-- (1) --> None

# Шаг 2: Добавление второго узла
second_node = ListNode(2)  # Узел со значением 2
dd_head.next = second_node  # Первый узел указывает на второй
second_node.prev = dd_head  # Второй узел указывает на первый
# Структура: None <-- (1) <--> (2) --> None

# Шаг 3: Добавление третьего узла
third_node = ListNode(3)  # Узел со значением 3
second_node.next = third_node  # Второй узел указывает на третий
third_node.prev = second_node  # Третий узел указывает на второй
# Структура: None <-- (1) <--> (2) <--> (3) --> None

# Шаг 4: Добавление четвертого узла
fourth_node = ListNode(4)  # Узел со значением 4
third_node.next = fourth_node  # Третий узел указывает на четвертый
fourth_node.prev = third_node  # Четвертый узел указывает на третий
# Структура: None <-- (1) <--> (2) <--> (3) <--> (4) --> None


class Solution:
    def reorderList(self, head: ListNode, tail: ListNode) -> ListNode:
        start = head
        end = tail
        while start != end and start.prev != end:
            print(start.val, end.val)
            start = start.next
            end = end.prev

        return head
    
s = Solution()
s.reorderList(dd_head, fourth_node)

from collections import deque
q = deque()
q.append()
q.insert(len(q)//2, 3)
q.popleft()
