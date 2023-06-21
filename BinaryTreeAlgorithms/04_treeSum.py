class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node(1)
b = Node(5)
c = Node(5)
d = Node(8)
e = Node(6)
f = Node(9)
g = Node(4)

a.left = b
a.right = c

b.left = d
b.right = e

# c.left = f
c.right = g


# depth first search iterative approach

def treeSum(root, sum = 0):
    if(root == None): return sum

    stack = [root]

    while(len(stack) > 0):
        current = stack.pop()
        sum += current.val

        if(current.right != None): stack.append(current.right)
        if(current.left != None): stack.append(current.left)

    return sum

print(treeSum(a))


# depth first recursive approach tree sum
def treeSum2(root):
    if(root == None): return 0
    return treeSum2(root.left) + root.val + treeSum2(root.right)

print(treeSum2(a))



# breadth first iterative approach
def treeSum3(root):
    if(root == None): return 0

    queue = [root]
    sum = 0

    while(len(queue) > 0):
        current = queue.pop(0)
        sum += current.val

        if(current.left != None): queue.append(current.left)
        if(current.right != None): queue.append(current.right)

    return sum

print(treeSum3(a))