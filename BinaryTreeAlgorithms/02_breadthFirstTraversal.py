class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c

b.left = d
b.right = e

# c.left = f
c.right = g

def breadthFirstTravrsal(root):
    if(root == None): return []

    queue = [root]
    result = []

    while(len(queue) > 0):
        current = queue.pop(0)
        result.append(current.val)
        if(current.left != None): queue.append(current.left)
        if(current.right != None): queue.append(current.right)

    return result

print(breadthFirstTravrsal(a))


# There is no streaght forward way to do the breadth first traversal with the recursion
# In recurrsion we take advantage of stack but for breadth first traversal we need to use the queue
# that's why this 2 approached are counter intutive to each other.  