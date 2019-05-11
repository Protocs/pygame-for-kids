from planetjump.utils import load_image, Point


class Background:
    def __init__(self, x, y):
        self.image = load_image("background.png")
        self.point = Point(x, y)
