"""Render test for Manim CE. Uses Text (no LaTeX needed).

    .venv-viz/bin/manim -ql viz/hello.py Hello
Output lands in media/ (git-ignored).
"""
from manim import DOWN, FadeIn, FadeOut, Scene, Text, Write


class Hello(Scene):
    def construct(self):
        title = Text("World-Model Ladder")
        sub = Text("image -> latent -> dynamics", font_size=28).next_to(title, DOWN)
        self.play(Write(title))
        self.play(FadeIn(sub))
        self.wait(0.5)
        self.play(FadeOut(title), FadeOut(sub))
