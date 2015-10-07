def insert(x, tree):
    if tree is None:
        return node(None, x, None)
    else:
        left, value, right = tree
        if x < value:
            return node(insert(x, left), value, right)
        elif x > value:
            return node(left, value, insert(x, right))
        else:
            return tree

tree2 = insert(4, tree1)
