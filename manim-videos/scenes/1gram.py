from manim import *
from manim_slides import Slide
from collections import Counter
import numpy as np

class OneGramScene(Slide):
    def construct(self):
        # Slide 1
        #  "The cat sat on the mat." is "read" by the model
        sentence = "The cat sat on the mat."
        words = [Text(word, font_size=36) for word in sentence.split()]
        for w in words[1:]:
            w.align_to(words[0], DOWN)
        text = VGroup(*words).arrange(RIGHT, buff=0.25)
        self.play(Write(text))

        reading_box = SurroundingRectangle(text[0], color=YELLOW, buff=0.2)
        self.play(Create(reading_box))

        ai_vocab = Rectangle(width=4, height=2, color=BLUE).to_edge(UP)
        ai_label = Text("AI Vocabulary", font_size=24).move_to(ai_vocab.get_top() + DOWN * 0.3)
        self.play(Create(ai_vocab), Write(ai_label))

        placed = []
        slot_padding = 0.2

        vocab_y = ai_vocab.get_bottom()[1] + 0.5
        inside_left_x = ai_vocab.get_left()[0] + 0.3

        for i, word in enumerate(text):
            self.play(reading_box.animate.move_to(word), run_time=0.5)
            word_copy = word.copy()
            word_copy.scale(0.6)

            target_x = inside_left_x + sum(m.width for m in placed) + i * slot_padding + word_copy.width / 2
            target_position = np.array([target_x, vocab_y, 0])

            self.play(word_copy.animate.move_to(target_position), run_time=0.5)
            placed.append(word_copy)
            self.add(word_copy)


        # Slide 2
        self.next_slide()

        self.play(FadeOut(text), FadeOut(reading_box))
        ai_group = VGroup(ai_vocab, ai_label, *placed)
        self.play(ai_group.animate.scale(1.5).move_to(ORIGIN), run_time=1)

        # Turn AI Vocabulary into bar chart
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
        total_width = len(unique) * bar_width + (len(unique)-1) * gap

        values = [freq[word] for word in unique]
        chart = BarChart(
            values,
            bar_names=unique,
            y_range=[0, max_count + 1, 1],
            x_length=total_width,
            y_length=max_height,
            bar_colors=[BLUE],
            bar_fill_opacity=1,
        ).move_to(DOWN * 0.3)

        self.play(Transform(ai_group, chart), run_time=1.5)
        
        # Slide 3
        self.next_slide()
        probs = [v / sum(values) for v in values]

        probability_dist = BarChart(
            probs,
            bar_names=unique,
            y_range=[0, 1, 0.2],
            x_length=total_width,
            y_length=max_height,
            bar_colors=[GREEN],
            bar_fill_opacity=1,
        ).move_to(DOWN * 0.3)

        self.play(Transform(ai_group, probability_dist), run_time=1.5)
        self.wait(1)
        
        # Slide 4
        self.next_slide()

        # Move the bars to the top right corner
        self.play(
            ai_group.animate.scale(0.5).to_corner(UR)
        )

        # Create prompt bar
        prompt_box = Rectangle(width=8, height=1, color=WHITE).center().shift(DOWN * 1)
        start_prompt = "The cat sat on the"
        prompt_words = [Text(word, font_size=36) for word in start_prompt.split()]
        start_prompt_group = VGroup(*prompt_words).arrange(RIGHT, buff=0.25)

        left_anchor = Dot(point=prompt_box.get_left() + RIGHT*0.25, radius=0).set_opacity(0)
        start_prompt_group.next_to(left_anchor, RIGHT, buff=0)
        start_prompt_group.move_to(start_prompt_group.get_center()[0] * RIGHT + prompt_box.get_center()[1] * UP, aligned_edge=ORIGIN)
        self.add(left_anchor)

        self.play(Create(prompt_box), Write(start_prompt_group))

        # Next word "the" is generated from the probability distribution and added to the prompt
        next_word = Text("the", font_size=36)
        next_word.move_to(ai_group.get_bottom() + DOWN * 0.5)
        self.add(next_word)
        start_prompt_group.add(next_word)
        self.play(Write(next_word))
        self.wait(1)
        self.play(
            start_prompt_group.animate.arrange(RIGHT, buff=0.25).next_to(left_anchor, RIGHT, buff=0),
            run_time=0.5
        )

        # Slide 5
        self.next_slide()
        # The generated word is always "the"
        # Repeat 3 times the generation of "the"

        for _ in range(3):
            next_word = Text("the", font_size=36)
            next_word.move_to(ai_group.get_bottom() + DOWN * 0.5)
            self.add(next_word)
            start_prompt_group.add(next_word)
            self.play(Write(next_word), run_time=0.4)
            self.play(
                start_prompt_group.animate.arrange(RIGHT, buff=0.25).next_to(left_anchor, RIGHT, buff=0),
                run_time=0.5
            )
            self.wait(0.5)

        
        # Slide 6
        # Compare the generated text to the original text
        self.next_slide()

        self.play(FadeOut(ai_group), FadeOut(prompt_box), run_time=1)

        original_sentence = "The cat sat on the mat."
        original_words = [Text(word, font_size=36) for word in original_sentence.split()]
        for w in original_words[1:]:
            w.align_to(original_words[0], DOWN)
        original_text = VGroup(*original_words).arrange(RIGHT, buff=0.25)
        self.play(Write(original_text))
