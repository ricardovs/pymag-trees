from sys import stdout
from pymag_trees.reingold_thread import DrawTree, reingold_tilford


# given an array of nodes, print them out reasonably on one line


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


# root = gentree("/Users/llimllib/Movies")
# root.children.reverse()
# drawtree = reingold_tilford(root)
# p(drawtree)
