from PIL import Image, ImageDraw
from pymag_trees.buchheim import DrawTree, buchheim


DIAMETER = 30
SPACING_VERTICAL = DIAMETER * 1.5
SPACING_HORIZONTAL = DIAMETER * 1.5


def drawt(draw, root, depth):
    global DIAMETER
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

def save_draw(drawtree, filename='figura.png'):
    im = Image.new('L', (1000, 500), (255))
    draw = ImageDraw.Draw(im)
    drawconn(draw, drawtree, 0)
    drawt(draw, drawtree, 0)
    im.save(filename)
