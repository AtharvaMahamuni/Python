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

# It can be done in many ways

# Recursive depth first search


# depth first recursive
def findTarget(root, element):
    if(root == None):
        return False
    
    if(root.val == element):
        return True

    leftValues = findTarget(root.left, element)
    rightValues = findTarget(root.right, element)

    return leftValues or rightValues
    
print(findTarget(a, 'f'))



# depth first iterative
def findTarget2(root, element):
    
    stack = [root]

    while(len(stack) > 0):
        current = stack.pop()

        if(current.val == element):
            return True
        
        if(current.left != None): stack.append(current.left)
        if(current.right != None): stack.append(current.right)

    return False

print(findTarget2(a, 'g'))


# breadth first recursive
def findTarget3(root, element):
    if(root == None): return False

    queue = [root]
    while(len(queue) > 0):
        current = queue.pop(0)

        if(current.val == element):
            return True
    
        if(current.left != None): queue.append(current.left)
        if(current.right != None): queue.append(current.right)

    return False

print(findTarget3(a, 'h'))