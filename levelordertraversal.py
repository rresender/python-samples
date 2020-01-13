def levelOrder(root):
    queue = []
    queue.append(root)
    while queue:
        node = queue.pop(0)
        print(node.info, end='')
        if node.left != None:
            queue.append(node)
        if node.right != None:
            queue.append(node)
