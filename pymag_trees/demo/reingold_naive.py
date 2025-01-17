from pymag_trees.tree import Tree, gentree
from pymag_trees.reingold_naive import DrawTree, reingold_tilford
from sys import stdout


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
            # stdout.write("%s%s%s" % (t.x*"____", str(t)[:3], t.x))
            newlevel.extend(t.children[:2])
        print
        if not newlevel:
            break
        level = newlevel


# root = gentree("/Users/llimllib/Movies")
# root.children.reverse()
# drawtree = reingold_tilford(root)
# p(drawtree)
