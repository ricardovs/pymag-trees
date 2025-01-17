from sys import stdout
from pymag_trees.demo.trees import trees
from pymag_trees.reingold_addmod import reingold_tilford


def printrow(level):
    x = dict((t.x, t.tree) for t in level)
    for i in range(max(x.keys()) + 1):
        try:
            stdout.write(str(x[i])[:4])
        except:
            stdout.write("    ")


def p(tree):
    level = [tree]
    while 1:
        newlevel = []
        printrow(level)
        for t in level:
            newlevel.extend(t.children[:2])
        print
        if not newlevel:
            break
        level = newlevel


def mirror(t):
    if len(t.children) > 1:
        t.children = (t.children[1], t.children[0])
    for c in t.children:
        mirror(c)
    return t

# root = gentree("/Users/llimllib/Movies")
# root.children.reverse()
# drawtree = reingold_tilford(root)
# p(drawtree)
