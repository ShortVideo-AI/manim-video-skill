from manim import *


config.pixel_width = 854
config.pixel_height = 480
config.frame_width = 16
config.frame_height = 9


class GeneratedScene(Scene):
    def construct(self):
        title = Text("Manim Skill Smoke Test", font_size=40).to_edge(UP)
        circle = Circle(radius=1.2, color=BLUE).shift(LEFT * 1.6)
        square = Square(side_length=2.0, color=YELLOW).shift(RIGHT * 1.6)
        label = Text("render helper OK", font_size=32).next_to(VGroup(circle, square), DOWN)

        self.play(Write(title), run_time=0.7)
        self.play(Create(circle), Create(square), run_time=1.0)
        self.play(FadeIn(label), run_time=0.5)
        self.wait(0.8)
