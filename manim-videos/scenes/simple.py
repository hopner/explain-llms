from manim import *

class ShapeTransform(Scene):
    def construct(self):
        circle = Circle(color=BLUE).scale(1.5)
        square = Square(color=GREEN).scale(1.5)

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.wait(1)
