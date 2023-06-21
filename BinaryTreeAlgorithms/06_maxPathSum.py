class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(2)
f = Node(2)
g = Node(1)

a.left = b
a.right = c

b.left = d
b.right = e

# c.left = f
c.right = g


#depth first recursive approach
def maxPathSum(root):
    if(root == None): return 0
    # return (maxPathSum(root.left) + root.val) if((maxPathSum(root.left) + root.val) < (root.val + maxPathSum(root.right))) else (root.val + maxPathSum(root.right)) 
    return max((maxPathSum(root.left) + root.val), (root.val + maxPathSum(root.right))) 
    
print(maxPathSum(a))


# depth first iterative approach