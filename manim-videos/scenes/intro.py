from manim import *
from manim_slides import Slide

class IntroScene(Slide):
    def construct(self):
        
        # Slide 1
        # AI bubble appears

        main_bubble = Ellipse(width=4, height=3, color=WHITE)
        main_bubble.set_fill(WHITE, opacity=0.9)

        small_1 = Circle(radius=0.25, color=WHITE).set_fill(WHITE, opacity=0.9)
        small_2 = Circle(radius=0.15, color=WHITE).set_fill(WHITE, opacity=0.9)

        small_1.next_to(main_bubble, DOWN+LEFT, buff=0.2)
        small_2.next_to(small_1, DOWN+LEFT, buff=0.1)

        text = Text("AI", font_size=50, color=BLACK)
        text.move_to(main_bubble.get_center())

        self.play(FadeIn(main_bubble), FadeIn(small_1), FadeIn(small_2), run_time=1)
        self.play(Write(text), run_time=1)
        self.next_slide()

        # Slide 2
        # Prompt bar is shown where the promt is typed and the prediction appears in ghosted text
        self.play(
            FadeOut(small_1), FadeOut(small_2), FadeOut(main_bubble), FadeOut(text)
        )

        prompt_bar = Rectangle(width=8, height=1, color=WHITE)
        prompt_bar.set_fill(WHITE, opacity=0.9)

        prompt = Text("The ", font_size=40, color=BLACK)
        prompt.move_to(prompt_bar.get_center() + LEFT*3)
        prediction = Text("cat", font_size=40, color=GREY)
        prediction.next_to(prompt, RIGHT, buff=0.3)

        self.play(FadeIn(prompt_bar), run_time=1)
        self.play(Write(prompt), run_time=1)
        self.wait(1)
        self.play(Add(prediction), run_time=1)

        self.next_slide()

        # Slide 3
        # The skill tree appears, one green bubble with two grey children
        # A cursor clicks on the left child, which turns green

        self.play(
            FadeOut(prompt_bar), FadeOut(prompt), FadeOut(prediction)
        )

        vertices = [1, 2, 3]
        edges = [(1, 2), (1, 3)]

        skill_tree = Graph(
            vertices,
            edges,
            layout={
                1: UP,
                2: LEFT + DOWN,
                3: RIGHT + DOWN,
            },
            vertex_config={
                1: {"fill_color": GREEN, "radius": 0.4},
                2: {"fill_color": GREY, "radius": 0.3},
                3: {"fill_color": GREY, "radius": 0.3},
            },
            edge_config={
                (1, 2): {"stroke_color": WHITE},
                (1, 3): {"stroke_color": WHITE},
            },
        )

        cursor = SVGMobject("input/cursor.svg").to_corner(DR).scale(0.15)

        self.play(Create(skill_tree), run_time=2)

        self.play(FadeIn(cursor), run_time=1)

        self.play(
            cursor.animate.move_to(skill_tree.vertices[2].get_center() + RIGHT * 0.1 + DOWN * 0.1),
            run_time=2
        )
        self.play(
            skill_tree.vertices[2].animate.set_fill(GREEN),
            run_time=1
        )
        self.next_slide()

        # Slide 4
        # Cursor clicks on the root node, which turns grey, and the children and edges disappear

        self.play(
            cursor.animate.move_to(skill_tree.vertices[1].get_center() + RIGHT * 0.1 + DOWN * 0.1),
            run_time=2
        )
        self.play(
            skill_tree.vertices[1].animate.set_fill(GREY),
            run_time=1
        )
        self.play(
            FadeOut(skill_tree.vertices[2]),
            FadeOut(skill_tree.vertices[3]),
            FadeOut(skill_tree.edges[(1, 2)]),
            FadeOut(skill_tree.edges[(1, 3)]),
            run_time=1
        )
        self.next_slide()

        # Slide 5
        # Fade out cursor and root node
        # A box appears symbolizing the AI model
        # A bunch of words from the top fall into the box
        # The box is shaken
        # A word is ejected from the box
        self.play(
            FadeOut(cursor),
            FadeOut(skill_tree.vertices[1]),
            run_time=1
        )

        model_box = Rectangle(width=4, height=2, color=WHITE)
        model_box.set_fill(WHITE, opacity=1)
        self.play(FadeIn(model_box), run_time=1)

        words = ["dog", "cat", "the", "new", "spaceship", "word", "turtle", "rabbit"]
        falling_words = VGroup()
        for i, word in enumerate(words):
            w = Text(word, font_size=30)
            w.move_to(UP * 3 + LEFT * 6 + RIGHT * (i) * 1.5)
            falling_words.add(w)

        self.play(*[FadeIn(w) for w in falling_words], run_time=2)

        self.play(
            *[w.animate.move_to(model_box.get_center()) for w in falling_words],
            run_time=3
        )

        self.play(model_box.animate.shift(LEFT * 0.2), run_time=0.15)
        self.play(model_box.animate.shift(RIGHT * 0.4), run_time=0.2)
        self.play(model_box.animate.shift(LEFT * 0.4), run_time=0.2)
        self.play(model_box.animate.shift(RIGHT * 0.4), run_time=0.2)
        self.play(model_box.animate.shift(LEFT * 0.4), run_time=0.2)
        self.play(model_box.animate.shift(RIGHT * 0.4), run_time=0.2)
        self.play(model_box.animate.shift(LEFT * 0.4), run_time=0.2)
        self.play(model_box.animate.shift(RIGHT * 0.4), run_time=0.2)
        self.play(model_box.animate.shift(LEFT * 0.4), run_time=0.2)
        self.play(model_box.animate.shift(RIGHT * 0.4), run_time=0.2)
        self.play(model_box.animate.shift(LEFT * 0.2), run_time=0.15)

        self.play(
            falling_words[1].animate.move_to(model_box.get_center() + DOWN * 2),
            run_time=2
        )
        self.next_slide()

        # Slide 6
        # Fade out everything
        # The text "Large Language Models" appears
        self.play(
            FadeOut(model_box),
            *[FadeOut(w) for w in falling_words],
            run_time=1
        )

        llm_text = Text("Large Language Models", font_size=60, color=WHITE)
        self.play(Write(llm_text), run_time=2)
        # End of the scene

