def node(left, value, right):
    return (left, value, right)

tree1 = node(node(node(None, 1, None),
                  2,
                  node(None, 3, None)),
             5,
             node(node(None, 6, None),
                  7,
                  None))
