# Stack - стэк 
# push - добавить элемент на вершину стэка
# pop - удалить элемент с вершины
# top - посмотреть на вершину 
# size - размер 

# LIFO - Last-in First-out

stack = []

# push == append
stack.append(1)

# pop == pop
stack.pop()

# top
# v = stack[-1]

# size
len(stack)

# Queue - очередь
# push - добавить в конце очереди
# pop - вытащить первый элемент очереди
# size - размер очереди 
# front - посмотреть первый элемент 

# FIFO - First-in First-out

from collections import deque

q = deque()

# push == append

q.append(1)

# pop = popleft()

# q.popleft() 
print(q)

# front 
print(q[0])




