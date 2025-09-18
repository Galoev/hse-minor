import time

from utils import push_front


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

N = 200_000
a = []
start_time = time.perf_counter()
for x in range(N):
    a.insert(0, x)
res_time = time.perf_counter() - start_time
print(f'list {N} insert front', f'{res_time:.2f}')

head = ListNode(0)
start_time = time.perf_counter()
for x in range(N):
    push_front(head, x)
res_time = time.perf_counter() - start_time
print(f'Linked List {N} insert front', f'{res_time:.2f}')