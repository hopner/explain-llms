from manim import *
from manim_slides import Slide

import re
from collections import defaultdict, Counter

import sys

sys.path.append("./utils")

from MiniChart import MiniChart

class TriGramScene(Slide):
    def construct(self):

        # Slide 1
        # The word "the" has many possible successors
        # From the word "the", we can have "cat", "mat, "dog", "next", etc.

        the = Text("the", font_size=96)
        cat = Text("cat", font_size=72).next_to(the, DOWN, buff=2)
        mat = Text("mat", font_size=72).next_to(the, LEFT, buff=2)
        dog = Text("dog", font_size=72).next_to(the, RIGHT, buff=2)
        next = Text("next", font_size=72).next_to(the, UP, buff=2)

        u_arrow = Arrow(the.get_top(), next.get_bottom())
        d_arrow = Arrow(the.get_bottom(), cat.get_top())
        l_arrow = Arrow(the.get_left(), mat.get_right())
        r_arrow = Arrow(the.get_right(), dog.get_left())

        arrows = VGroup(u_arrow, d_arrow, l_arrow, r_arrow)

        self.play(Write(the))

        self.play(
            Write(cat),
            Write(mat),
            Write(dog),
            Write(next),
            Create(arrows)
        )
        self.next_slide()

        # Slide 2
        # From the sentence "the cat sat on the mat", turn the DiGram into a TriGram

        self.play(FadeOut(arrows), FadeOut(cat), FadeOut(mat), FadeOut(dog), FadeOut(next), FadeOut(the))

        sentence = "the cat sat on the mat"
        words = sentence.split()
        digram_pairs = [(words[i], words[i+1]) for i in range(len(words)-1)]
        trigram_triplets = [(words[i], words[i+1], words[i+2]) for i in range(len(words)-2)]

        digram_texts = VGroup(*[Text(f"({a} {b})", font_size=48) for a, b in digram_pairs])
        trigram_texts = VGroup(*[Text(f"({a} {b} {c})", font_size=48) for a, b, c in trigram_triplets])

        digram_arrangement = VGroup(*digram_texts).arrange(RIGHT, buff=0.5)
        trigram_arrangement = VGroup(*trigram_texts).arrange(RIGHT, buff=0.5)
        self.play(Write(digram_arrangement))
        self.play(Transform(digram_arrangement, trigram_arrangement))
        self.next_slide()

        # Slide 3
        # Show the frequency table of the most common pair in alice

        # Pre-processing
        with open("input/alice.txt", "r") as f:
            text = f.read().lower()
        tokens = re.findall(r"\b[a-z']+\b", text)

        following = defaultdict(Counter)
        for a, b, c in zip(tokens, tokens[1:], tokens[2:]):
            following[(a, b)][c] += 1


        most_common_pairs = Counter()
        for (a, b), counter in following.items():
            most_common_pairs[(a, b)] = sum(counter.values())
        top_pairs = [pair for pair, count in most_common_pairs.most_common(10)]

        def get_top_followers(word, n=5, mode='relative'):
            counts = following[word]
            if not counts:
                return [], []
            most = counts.most_common(n)
            words = [w for w, _ in most]
            if mode == 'total':
                total = sum(counts.values())
            else:
                total = sum(c for _, c in most)
            probs = [c / total for _, c in most]
            return words, probs
        # Pre-processing end

        table_data = []
        pair = top_pairs[0]
        next_words, probs = get_top_followers(pair, n=10, mode='total')
        for w, p in zip(next_words, probs):
            table_data.append([f"{pair[0]} {pair[1]}", w, f"{p:.2f}"])
        table = Table(
            table_data,
            col_labels=[Text("Pair"), Text("Next Word"), Text("Probability")],
            line_config={"stroke_width": 1},
        ).scale(0.5)

        self.play(ReplacementTransform(digram_arrangement, table), run_time=2)
        self.next_slide()

        # Slide 4
        # Show mini charts of the most common pairs
        table_rows = VGroup()

        for pair in top_pairs:
            next_words, probs = get_top_followers(pair, n=10)
            world_label = Text(f"{pair[0]} {pair[1]}").scale(0.3)

            if probs:
                bars = VGroup()
                for p in probs:
                    bar = Rectangle(
                        width=0.15,
                        height=p * 1.5,
                        fill_color=BLUE,
                        fill_opacity=1,
                        stroke_width=0,
                    )
                    bars.add(bar)

                bars.arrange(RIGHT, buff=0)
                bottom_y = min(bar.get_bottom()[1] for bar in bars)
                for bar in bars:
                    shift_amount = bottom_y - bar.get_bottom()[1]
                    bar.shift(UP * shift_amount)
            else:
                bars = Text("No data").scale(0.3)

            row = VGroup(world_label, bars).arrange(RIGHT, buff=0.5)
            table_rows.add(row)

        table_rows.arrange(DOWN, aligned_edge=RIGHT, buff=0.3).scale(1.2)

        table_rect = Rectangle(
            width=table_rows.width + 0.3,
            height=table_rows.height + 0.3,
            stroke_width=2
        )

        h_lines = VGroup()
        for row in table_rows[:-1]:
            y = row.get_bottom()[1] - 0.15
            line = Line(
                start=[table_rows.get_left()[0] - 0.15, y, 0],
                end=[table_rows.get_right()[0] + 0.15, y, 0],
                stroke_width=1
            )
            h_lines.add(line)

        full_table = VGroup(table_rect, h_lines, table_rows).center()

        self.play(FadeOut(table), FadeIn(full_table), run_time=3)
        self.next_slide()

        # Slide 5
        # Given promt "It was in the", the model predicts "distance" and not "cat"

        prompt = Text("It was in the", font_size=36).to_edge(LEFT)
        arrow = Arrow(prompt.get_right(), full_table.get_left()+DOWN*0.125)
        self.play(Write(prompt), Create(arrow), run_time=2)

        prediction = Text("distance", font_size=36).to_edge(RIGHT)
        arrow2 = Arrow(full_table.get_right()+DOWN*0.125, prediction.get_left())
        self.play(Create(arrow2), Write(prediction), run_time=2)

        wrong_prediction = Text("cat", font_size=36).next_to(prediction, UP, buff=2)
        red_cross = Cross(wrong_prediction, stroke_width=4, color=RED)
        self.play(Write(wrong_prediction), Create(red_cross), run_time=1)

        self.next_slide()
        # Slide 6
        self.play(FadeOut(prompt), FadeOut(arrow), FadeOut(arrow2), FadeOut(prediction), FadeOut(wrong_prediction), FadeOut(red_cross), FadeOut(full_table))

        original_sentence = "The cat sat on the mat."
        unigram_sentence = "The the the the the the."
        bigram_sentence = "The cat sat on the cat sat on the mat."
        trigram_sentence = "The cat sat on the mat."

        unigram_text = Text(f"1-gram: {unigram_sentence}").move_to(ORIGIN)
        original_text = Text(f"Original: {original_sentence}").next_to(unigram_text, UP)
        bigram_text = Text(f"2-gram: {bigram_sentence}").next_to(unigram_text, DOWN)
        trigram_text = Text(f"3-gram: {trigram_sentence}").next_to(bigram_text, DOWN)

        self.play(Create(original_text), Create(unigram_text), Create(bigram_text), Create(trigram_text), run_time=3)