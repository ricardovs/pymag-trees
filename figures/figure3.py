import os
from src.tree import Tree
from demo.demo_trees import trees
from src.ws1 import layout
from PIL import Image, ImageDraw


DIAMETER = 30
SPACING_VERTICAL = DIAMETER * 1.5
SPACING_HORIZONTAL = DIAMETER * 1.5


def drawt(draw, root, depth):
    draw.ellipse(
        [
            root.x * SPACING_HORIZONTAL,
            depth * SPACING_VERTICAL,
            root.x * SPACING_HORIZONTAL + DIAMETER,
            depth * SPACING_VERTICAL + DIAMETER,
        ],
        fill=(225),
        outline=(0),
    )
    for child in root.children:
        drawt(draw, child, depth + 1)


def drawconn(draw, root, depth):
    for child in root.children:
        draw.line(
            [
                root.x * SPACING_HORIZONTAL + (DIAMETER / 2),
                depth * SPACING_VERTICAL + (DIAMETER / 2),
                child.x * SPACING_HORIZONTAL + (DIAMETER / 2),
                (depth + 1) * SPACING_VERTICAL + (DIAMETER / 2),
            ],
            fill=(0),
        )
        drawconn(draw, child, depth + 1)


if __name__ == '__main__':
    t = layout(trees[4])

    im = Image.new("L", (1000, 500), (255))
    draw = ImageDraw.Draw(im)
    drawconn(draw, t, 0)
    drawt(draw, t, 0)

    if not os.path.exists('out/'):
        os.makedirs('out/')
    im.save("out/figure3.png")
