""""
            1                             0- Depth
        /       \
       2         3                        1- Depth 
     /  \      /   \
    4    5    6     7                     2- Depth
  /  \
8     9                                   3- Depth




Depth of a node is the distance between the respective node to the root node
This can be solved by using either recursive method or iterative method.
Time: O(n) and Space: O(h) 'h' is height

# Output returns Sum of depths: 16
(0+1+1+2+2+2+2+3+3) 
"""




# Using iterative method
def nodeDepths(root):
    sumOfDepths = 0
    stack = [{'node': root, 'depth': 0}]
    # we can take list instead of dict too.
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo['node'], nodeInfo['depth']
        if node is None:
            continue
        sumOfDepths+=depth
        stack.append({'node': node.left, 'depth': depth+1})
        stack.append({'node': node.right, 'depth': depth + 1})
    return sumOfDepths
# Output returns 16(0+1+1+2+2+2+2+3+3)
#-------------------------------------------------
# Using recursive method
# Time: O(n) and Space: O(h) 'h' is height

def nodeDepths(root, depth = 0):
    # Base condition
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth+1), nodeDepths(root.right, depth+1)
            # recursively calls left and right sides of each node while updating depths until it reaches None
# Output returns 16(0+1+1+2+2+2+2+3+3)
