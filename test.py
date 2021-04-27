from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Circle()
        square.flip(LEFT)
        # square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))