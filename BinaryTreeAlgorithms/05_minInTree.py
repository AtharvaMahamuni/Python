class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node(10)
b = Node(6)
c = Node(56)
d = Node(-1)
e = Node(-7)
f = Node(99)
g = Node(9)

a.left = b
a.right = c

b.left = d
b.right = e

# c.left = f
c.right = g


# depth first traversal iterative approach

def minInTree(root):
    if(root == None): return None

    stack = [root]
    min = root.val

    while(len(stack) > 0):
        current = stack.pop()

        if(current.val < min): min = current.val

        if(current.left != None): stack.append(current.left)
        if(current.right != None): stack.append(current.right)

    return min

print(minInTree(a))


# breadth first traversal

def minInTree2(root):
    if(root == None): return None
    
    queue = [root]
    min = root.val

    while(len(queue) > 0):
        current = queue.pop(0)

        if(current.val < min): min = current.val

        if(current.left != None): queue.append(current.left)
        if(current.right != None): queue.append(current.right)

    return min

print(minInTree2(a))



# deapth first traversal recursive
def minInTree3(root):
    if(root.left == None or root.right == None): return root.val
    return min(root.val, minInTree3(root.left), minInTree3(root.right))

print(minInTree3(a))