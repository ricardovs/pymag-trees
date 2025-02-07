class DrawTree:
    def __init__(self, tree, depth=-1):
        self.x = -1
        self.y = depth
        self.tree = tree
        self.children = []
        self.thread = None

    def left(self):
        return self.thread or len(self.children) and self.children[0]

    def right(self):
        return self.thread or len(self.children) and self.children[-1]


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
    wl = contour(left, "right")
    wr = contour(right, "left")
    if len(wl) != len(wr):
        fix_threads(left, right, len(wl), len(wr))

    diff = max(x - y for x, y in zip(wl, wr)) + 1
    diff += (right.x + diff + left.x) % 2  # stick to the integers

    addtotree(right, diff)
    return (left.x + right.x) / 2


def fix_threads(left, right, ldepth, rdepth):
    if ldepth > rdepth:
        rattach(left, right, rdepth)
    else:
        lattach(left, right, ldepth)


# when the left tree is deeper than the right tree, descend rdepth levels
# down the right side of both trees and attach the last node on the right
# to the rightmost node on the left


def rattach(left, right, depth):
    if depth > 1:
        return rattach(left.right(), right.right(), depth - 1)
    right.thread = left.right()


def lattach(left, right, depth):
    if depth > 1:
        return lattach(left.left(), right.left(), depth - 1)
    left.thread = right.left()


def addtotree(tree, val):
    tree.x += val
    if len(tree.children):
        for child in tree.children[:2]:
            addtotree(child, val)


def contour(tree, next):
    next_node = getattr(tree, next)()
    if not next_node:
        return [tree.x]
    else:
        return [tree.x] + contour(next_node, next)
