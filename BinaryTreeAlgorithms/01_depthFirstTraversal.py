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


def treeTraversalDepthFirstIterative(root):
    if(root == None):
        return []

    myStack = [root]
    result = []

    while(len(myStack) > 0):
        current = myStack.pop()
        result.append(current.val)
        # print(current.val)

        if(current.right != None):
            myStack.append(current.right)
        
        if(current.left != None):
            myStack.append(current.left)
    
    return result
        
print(treeTraversalDepthFirstIterative(a))


# recursive approach to the breadth first search
def treeTraversalDepthFirst(root):
    if(root == None):
        return []
    
    leftValues = treeTraversalDepthFirst(root.left)
    rightValues = treeTraversalDepthFirst(root.right)
    return [root.val, *leftValues, *rightValues]

print(treeTraversalDepthFirst(a))

