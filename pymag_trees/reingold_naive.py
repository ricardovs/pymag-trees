from operator import lt, gt


class DrawTree:
    def __init__(self, tree, depth=-1):
        self.x = -1
        self.y = depth
        self.tree = tree
        self.children = []


# traverse to the bottom of the tree, and place the leaves at an arbitrary
#   x coordinate
# if the node is a parent, draw its subtrees, then shift the right one as close
#   to the left as possible
# place the parent in the middle of the two trees.


def reingold_tilford(tree, depth=0):
    dt = DrawTree(tree, depth)
    if len(tree) == 0:
        dt.x = 0
        return dt

    if len(tree) == 1:
        dt.children = [reingold_tilford(tree[0], depth + 1)]
        dt.x = dt.children[0].x
        return dt

    left = reingold_tilford(tree[0], depth + 1)
    right = reingold_tilford(tree[1], depth + 1)

    dt.children = [left, right]
    dt.x = fix_subtrees(left, right)
    return dt


# place the right subtree as close to the left subtree as possible


def fix_subtrees(left, right):
    wl = contour(left, lt)
    wr = contour(right, gt)
    diff = max(map(lambda x, y: x - y, wl, wr)) + 1
    # stick to the integers
    diff += (right.x + diff + left.x) % 2
    addtotree(right, diff)
    return (left.x + right.x) / 2


def addtotree(tree, val):
    tree.x += val
    if len(tree.children):
        for child in tree.children[:2]:
            addtotree(child, val)


def contour(tree, comp, level=0, cont=None):
    if not level:
        cont = [tree.x]
    elif len(cont) < level + 1:
        cont.append(tree.x)
    elif comp(cont[level], tree.x):
        cont[level] = tree.x

    for child in tree.children[:2]:
        contour(child, comp, level + 1, cont)

    return cont
