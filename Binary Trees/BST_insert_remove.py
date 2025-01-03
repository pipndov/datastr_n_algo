class Binary_Tree:
    def __init__(self, val):
        self.val = val
        self.root
        self.right = None 
        self.left = None

def insert(root, val):
    if root is None:
        return Binary_Tree(val)
    
    if root.val < val:
        root.right = insert(root.right, val)
    elif root.val > val:
        root.left = insert(root.left, val)
    return root

def min_Value(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def max_Value(root):
    curr = root
    while curr and curr.right:
        curr = curr.right
    return curr

def remove(root, val):
    if root is None:
        return None
    
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            minNode = min_Value(root.right)
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root
