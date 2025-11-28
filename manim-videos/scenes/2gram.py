from manim import *
from manim_slides import Slide
from collections import Counter
import numpy as np
from collections import defaultdict, Counter
import re
import sys

sys.path.append("./utils")

from MiniChart import MiniChart



class DiGramScene(Slide):
    def construct(self):

        # Slide 1
        # The histogram of the word frequencies from "The cat sat on the mat."
        sentence = "The cat sat on the mat."
        tokens = [w.lower().strip(".,") for w in sentence.split()]
        freq = Counter(tokens)
        unique = []
        for word in tokens:
            if word not in unique:
                unique.append(word)
        
        bar_width = 0.6
        gap = 0.35
        max_height = 3
        max_count = max(freq.values())
        total_width = len(unique) * bar_width + (len(unique) - 1) * gap
        values = [freq[word] for word in unique]
        chart = BarChart(
            values,
            bar_names=unique,
            y_range=[0, max_count + 1, 1],
            x_length=total_width,
            y_length=max_height,
            bar_colors=[BLUE],
            bar_fill_opacity=1,
        )

        self.play(Create(chart), run_time=3)

        self.next_slide()

        # Slide 2
        # Show how the word "the" has two possible following words: "cat" and "mat"
        self.play(FadeOut(chart))
        
        nodes = VGroup()
        left = Text("the").move_to(LEFT * 2)
        right1 = Text("cat").move_to(RIGHT * 2 + UP)
        right2 = Text("mat").move_to(RIGHT * 2 + DOWN)
        nodes.add(left, right1, right2)
        edges = VGroup()
        edge1 = Arrow(left.get_right(), right1.get_left(), buff=0.2)
        edge2 = Arrow(left.get_right(), right2.get_left(), buff=0.2)
        edges.add(edge1, edge2)

        self.play(Create(nodes), Create(edges), run_time=3)

        self.next_slide()

        # Slide 3
        # Rescale current graph and add the other words for the entire bigram model from the sentence

        
        self.play(
            nodes.animate.scale(0.7).move_to(LEFT * 2.5),
            edges.animate.scale(0.7).move_to(LEFT * 2.5),
            run_time=2
        )

        rright1 = Text("sat").scale(0.7).next_to(right1, RIGHT, buff=1.4)
        rrright1 = Text("on").scale(0.7).next_to(rright1, RIGHT, buff=1.4)
        rright2 = Text(".").scale(0.7).next_to(right2, RIGHT, buff=1.4)

        nodes.add(rright1, rrright1, rright2)

        edge3 = Arrow(right1.get_right(), rright1.get_left(), buff=0.2)
        edge4 = Arrow(rright1.get_right(), rrright1.get_left(), buff=0.2)
        edge5 = Arrow(right2.get_right(), rright2.get_left(), buff=0.2)

        loop = CurvedArrow(
            rrright1.get_top() + UP * 0.1,
            left.get_top() + UP * 0.1,
            angle=PI / 2
        )

        edges.add(edge3, edge4, edge5, loop)

        self.play(Create(rright1), Create(rrright1), Create(rright2), Create(edge3), Create(edge4), Create(edge5), Create(loop), run_time=2)
        
        self.next_slide()

        # Slide 4
        # The graph turns into a table with each word as a key and the possible following words as a value
        table_data = [
            ["the", "cat, mat"],
            ["cat", "sat"],
            ["sat", "on"],
            ["on", "the"],
            ["mat", "."]
        ]

        table = Table(
            table_data,
            col_labels=[Text("Word"), Text("Follows")],
            include_outer_lines=True,
            line_config={"stroke_width": 1},
        )

        self.play(Transform(nodes, table), FadeOut(edges), run_time=3)
        self.remove(nodes)
        self.add(table)
        
        self.next_slide()
        # Slide 5
        # Huge body of text rolls on the left side
        # On the right side we see the probabilities of some whords for the most common word "the"

        self.play(FadeOut(table), run_time=1.5)


        # Pre-processing
        text_content = ""
        with open("input/alice.txt", "r") as f:
            for i in range(50):
                line = f.readline()
                if not line:
                    break
                text_content += line
            text = f.read().lower()
        
        tokens = re.findall(r"\b[a-z']+\b", text)

        following = defaultdict(Counter)
        for a, b in zip(tokens, tokens[1:]):
            following[a][b] += 1

        freqs = Counter(tokens)
        top_words = [word for word, count in freqs.most_common(8)]

        def get_top_followers(word, n=5):
            counts = following[word]
            if not counts:
                return [], []
            most = counts.most_common(n)
            words = [w for w, _ in most]
            total = sum(c for _, c in most)
            probs = [c / total for _, c in most]
            return words, probs
        # Pre-processing end


        para = Paragraph(text_content, line_spacing=0.4).scale(0.3).to_edge(LEFT)

        most_popular_word = top_words[0]
        next_words, probs = get_top_followers(most_popular_word, n=10)
        chart = BarChart(
            values=probs,
            bar_names=next_words,
            y_range=[0, 0.3, 0.1]
        ).scale(0.7)

        label = Text(most_popular_word).scale(0.5).next_to(chart, DOWN, buff=0.3)

        chart_group = VGroup(chart, label).to_edge(RIGHT)

        self.play(Create(para), Create(chart_group), run_time=6)
        
        self.next_slide()
        
        # Slide 6
        self.play(FadeOut(chart_group), FadeOut(para), run_time=1.5) 

        table_rows = VGroup()

        for word in top_words:
            next_words, probs = get_top_followers(word, n=10)
            world_label = Text(word).scale(0.3)

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

        label_width = max(row[1][1].width for row in table_rows)  # adjust if needed
        x = table_rows.get_left()[0] + label_width + 0.45

        v_line = Line(
            start=[x, table_rows.get_top()[1] + 0.15, 0],
            end=[x, table_rows.get_bottom()[1] - 0.15, 0],
            stroke_width=1
        )

        full_table = VGroup(table_rect, h_lines, v_line, table_rows).center()
        
        self.play(Create(full_table), run_time=3)
        self.next_slide()

        # Slide 7
        # The prompt "the" appears on the left, an arrow points to top row of the table
        # Then an arrow goes to the middle right where the predicted word "queen" appears

        prompt = Text("the").scale(1).to_edge(LEFT)
        prediction = Text("queen").scale(1).to_edge(RIGHT)
        target_row = full_table[3][0]
        arrow1 = Arrow(
            prompt.get_right(),
            target_row.get_left() + LEFT * 0.2,
            buff=0.2
        )
        arrow2 = Arrow(
            target_row.get_right() + RIGHT * 0.2,
            prediction.get_left(),
            buff=0.2
        )
        self.play(Create(prompt), Create(arrow1), run_time=2)
        self.play(Create(arrow2), run_time=1)
        self.play(Create(prediction), run_time=1)

        self.next_slide()
        # Slide 8
        # Comparison
        self.play(FadeOut(prompt), FadeOut(arrow1), FadeOut(arrow2), FadeOut(prediction), FadeOut(full_table), run_time=1)

        original_sentence = "The cat sat on the mat."
        unigram_sentence = "The the the the the the."
        bigram_sentence = "The cat sat on the cat sat on the mat."

        unigram_text = Text(f"1-gram: {unigram_sentence}").move_to(ORIGIN)
        original_text = Text(f"Original: {original_sentence}").next_to(unigram_text, UP)
        bigram_text = Text(f"2-gram: {bigram_sentence}").next_to(unigram_text, DOWN)

        self.play(Create(original_text), Create(unigram_text), Create(bigram_text), run_time=3)