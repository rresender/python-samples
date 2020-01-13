def height(root):
    if root is None:
	    return -1
    left = height(root.left) + 1
    right = height(root.right) + 1
    if left > right:
        return left
    return right