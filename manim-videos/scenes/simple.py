from manim import *
from manim_slides import Slide

class SimpleSlideshow(Slide):
    def construct(self):
        # Slide 1: Title
        title = Text("Explain LLMs", font_size=72)
        subtitle = Text("Interactive Learning Experience", font_size=36).next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(Write(subtitle))
        self.next_slide()
        
        # Slide 2: What are LLMs?
        self.play(FadeOut(title), FadeOut(subtitle))
        
        what_title = Text("What are Large Language Models?", font_size=48)
        definition = Text(
            "AI systems trained on vast amounts of text\n"
            "to understand and generate human language",
            font_size=32
        ).next_to(what_title, DOWN, buff=1)
        
        self.play(Write(what_title))
        self.play(Write(definition))
        self.next_slide()
        
        # Slide 3: How do they work?
        self.play(FadeOut(what_title), FadeOut(definition))
        
        how_title = Text("How do they work?", font_size=48)
        steps = VGroup(
            Text("1. Tokenization", font_size=28),
            Text("2. Attention Mechanism", font_size=28),
            Text("3. Neural Networks", font_size=28),
            Text("4. Prediction", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(how_title, DOWN, buff=1)
        
        self.play(Write(how_title))
        for step in steps:
            self.play(Write(step))
        self.next_slide()
        
        # Slide 4: Build Your Own
        self.play(FadeOut(how_title), FadeOut(steps))
        
        build_title = Text("Build Your Own Model", font_size=48, color=BLUE)
        build_subtitle = Text(
            "Start with a simple model and improve it step by step",
            font_size=32
        ).next_to(build_title, DOWN, buff=0.5)
        
        arrow = Arrow(ORIGIN, RIGHT * 2, color=GREEN).next_to(build_subtitle, DOWN, buff=1)
        start_text = Text("Let's begin!", font_size=28, color=GREEN).next_to(arrow, RIGHT)
        
        self.play(Write(build_title))
        self.play(Write(build_subtitle))
        self.play(GrowArrow(arrow))
        self.play(Write(start_text))
        self.next_slide()
        
        # Slide 5: Thank you
        self.play(FadeOut(VGroup(build_title, build_subtitle, arrow, start_text)))
        
        thanks = Text("Ready to explore?", font_size=56, color=YELLOW)
        self.play(Write(thanks))
        self.wait(2)