from manim import *
from manim_slides import Slide
import numpy as np

class TokenizationScene(Slide):
    def construct(self):

        sentence = "The cat sat on the mat."
        words = sentence.split(" ")

        # Slide 1 — write sentence instantly, correctly centered

        word_objs = VGroup(*[Text(w, font_size=48) for w in words])
        word_objs.arrange(RIGHT, buff=0.15)
        word_objs.move_to(ORIGIN)

        self.play(FadeIn(word_objs))
        self.next_slide()


        # Slide 2 — spacing + separators simultaneously
        spaced_layout = word_objs.copy().arrange(RIGHT, buff=0.7).move_to(ORIGIN)

        separators = VGroup()
        for i in range(len(words) - 1):
            left = spaced_layout[i].get_right()
            right = spaced_layout[i+1].get_left()
            midpoint = (left + right) / 2
            sep = Text("|", font_size=48, color=YELLOW)
            sep.move_to(midpoint)
            sep.set_opacity(0)
            separators.add(sep)

        self.play(
            *[word.animate.move_to(target.get_center())
              for word, target in zip(word_objs, spaced_layout)],
            *[sep.animate.set_opacity(1) for sep in separators],
            run_time=1.0
        )

        self.next_slide()

        # Slide 3 - Fade out everything except "mat." and highlight problem

        mat_word = word_objs[-1]
        old_pos = mat_word.get_center()
        others = VGroup(*word_objs[:-1])

        self.play(
            FadeOut(others),
            *[FadeOut(sep) for sep in separators],
        )
        self.play(mat_word.animate.move_to(ORIGIN+RIGHT*2))

        other_mat = Text("mat", font_size=48).move_to(ORIGIN+LEFT*2)
        relation = Tex("$\\neq$", font_size=72).move_to(ORIGIN)

        self.play(
            FadeIn(other_mat),
            FadeIn(relation)
        )

        self.next_slide()

        # Slide 4 - Show the old tokenization method and add a new sepparator between "mat" and "."
        self.play(
            FadeOut(other_mat),
            FadeOut(relation),
            FadeOut(mat_word)
        )

        mat_word.move_to(old_pos)

        split_mat = Text("mat", font_size=48).move_to(old_pos+LEFT*0.08)
        split_dot = Text(".", font_size=48).next_to(split_mat, RIGHT).shift(DOWN*0.18 + LEFT*0.15)

        self.play(
            FadeIn(word_objs),
            FadeIn(separators)
        )

        new_sep = Text("|", font_size=48, color=YELLOW)
        left = split_mat.get_right()
        right = split_dot.get_left()
        midpoint = (left + right) / 2
        new_sep.move_to(midpoint)
        new_sep.set_opacity(0)

        word_objs.remove(mat_word)

        self.play(
            split_mat.animate.shift(LEFT * 0.2),
            split_dot.animate.shift(RIGHT * 0.22),
            new_sep.animate.set_opacity(1),
        )

        self.next_slide()

        # Slide 5 - Fade out everything and show splitting of "unbelievable"
        self.play(
            FadeOut(word_objs),
            *[FadeOut(sep) for sep in separators],
            FadeOut(new_sep),
            FadeOut(split_mat),
            FadeOut(split_dot)
        )

        example_word = Text("unbelievable", font="Times New Roman").move_to(ORIGIN + LEFT*2)

        self.play(Write(example_word))

        middle = Text("believe", font="Times New Roman").move_to(ORIGIN + RIGHT*3)
        prefix = Text("un", font="Times New Roman").next_to(middle, UP)
        suffix = Text("able", font="Times New Roman").next_to(middle, DOWN)

        arrow1 = Arrow(example_word.get_right()+RIGHT*0.2, middle.get_left()+LEFT*0.2, buff=0, stroke_width=4)
        arrow2 = Arrow(example_word.get_right()+RIGHT*0.2, prefix.get_left()+LEFT*0.2, buff=0, stroke_width=4)
        arrow3 = Arrow(example_word.get_right()+RIGHT*0.2, suffix.get_left()+LEFT*0.2, buff=0, stroke_width=4)

        arrows = VGroup(arrow1, arrow2, arrow3)

        self.play(
            Write(prefix),
            Write(middle),
            Write(suffix),
            *[GrowArrow(arrow) for arrow in arrows]
        )
        self.next_slide()

        # Slide 6 - Show example table with token IDs (random) for a few tokens
        self.play(
            FadeOut(example_word),
            FadeOut(prefix),
            FadeOut(middle),
            FadeOut(suffix),
            *[FadeOut(arrow) for arrow in arrows]
        )

        table_data = [
            ["cat", "1023"],
            ["dog", "2045"],
            ["mat", "1502"],
            [".", "12"],
            ["the", "305"],
            ["mat.", "1503"],
            ["on", "450"],
            ["sat", "789"]
        ]

        table = Table(
            table_data,
            col_labels=[Text("Token"), Text("ID")],
            include_outer_lines=True,
            arrange_in_grid_config={"cell_alignment": LEFT}
            )
        table.get_labels().set_color(BLUE)

        table.scale(0.6)
        self.play(Create(table))
        self.wait(1)

        self.next_slide()

        # Slide 7 - Show how the sentence is represented as a list of token IDs
        self.play(FadeOut(table))

        sentence_ids = [305, 1023, 789, 450, 305, 1503]

        sentence_text = Text(sentence, font_size=36).move_to(ORIGIN+UP*1)
        ids_text = Text("[" + ", ".join(map(str, sentence_ids)) + "]", font_size=36).move_to(ORIGIN+DOWN*1)

        self.play(Write(sentence_text))
        self.play(Write(ids_text))