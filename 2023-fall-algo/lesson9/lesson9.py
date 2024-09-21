from utils import TreeNodeUtils
from collections import deque



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def find(root, x):
    if not root:
        return None

    if root.val == x:
        return root
    elif root.val < x:
        return find(root.right, x)
    else:
        return find(root.left, x)



def insert(root, x):
    if not root:
        return TreeNode(x)

    if x < root.val:
        root.left = insert(root.left, x)
    elif x > root.val:
        root.right = insert(root.right, x)
    
    return root


u = TreeNodeUtils()
nums = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
root = u.buildTree(nums)
print(u.printTree(root))

# ABCDEFG

def bfs(root):
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        print(node.val, end='')

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)



def dfs(root):
    if not root:
        return
    print(root.val, end='')
    dfs(root.left)
    dfs(root.right)

dfs(root)
# ABDECFG