from manim import *
from manim_slides import Slide
import random

def token_rect(color = None, width = None, height = 0.3):
    if color is None:
        color = random.choice([BLUE, GREEN, RED, YELLOW, ORANGE, PURPLE])
    if width is None:
        width = random.uniform(0.3, 1.2)
    return Rectangle(width=width, height=height, fill_color=color, fill_opacity=1, stroke_width=0)

def generate_text_block(lines=5, tokens_per_line=8, color=None):
    block = VGroup()
    for _ in range(lines):
        line = VGroup(*[token_rect(color=color) for _ in range(tokens_per_line)])
        line.arrange(RIGHT, buff=0.06)
        block.add(line)
    block.arrange(DOWN, buff=0.15)
    return block

def make_word_box(word, color=RED):
    txt = Text(word)
    box = Rectangle(
        width=txt.width + 0.3,
        height=txt.height + 0.2,
        fill_color=color,
        fill_opacity=1,
        stroke_width=0
    )
    group = VGroup(box, txt)
    txt.move_to(box.get_center())
    return group

class MoreDataScene(Slide):

    def construct(self):
        # Slide 1
        # Starting with text generally found in Moby Dick
        sentence = "the whale and the ship ...".split()
        word_boxes = VGroup(*[make_word_box(word, color=RED) for word in sentence])
        word_boxes.arrange(RIGHT, buff=0.1)

        self.play(LaggedStart(*[
            FadeIn(word_box) for word_box in word_boxes
        ], lag_ratio=0.1))

        self.next_slide()

        # Slide 2

        self.play(
            word_boxes.animate.to_edge(UP)
        )

        ai_box = Rectangle(width=3, height=3, fill_color=LIGHT_GRAY, fill_opacity=1, stroke_width=2)
        ai_label = Text("AI", font_size=36).move_to(ai_box.get_center())
        ai_model = VGroup(ai_box, ai_label)
        self.play(FadeIn(ai_model))

        self.play(
            word_boxes.animate.move_to(ai_model.get_center()).scale(0.1)
        )
        self.remove(word_boxes)

        self.next_slide()
        # Slide 3

        red_text = generate_text_block(lines=5, tokens_per_line=10, color=RED).scale(0.5).to_corner(UL)
        blue_text = generate_text_block(lines=5, tokens_per_line=10, color=BLUE).scale(0.5).to_corner(UR)
        green_text = generate_text_block(lines=5, tokens_per_line=10, color=GREEN).scale(0.5).to_corner(DL)
        yellow_text = generate_text_block(lines=5, tokens_per_line=10, color=YELLOW).scale(0.5).to_corner(DR)

        self.play(
            FadeIn(red_text),
            FadeIn(blue_text),
            FadeIn(green_text),
            FadeIn(yellow_text),
        )

        self.bring_to_front(ai_model)

        self.play(
            red_text.animate.move_to(ai_model.get_center()).scale(0.1),
            blue_text.animate.move_to(ai_model.get_center()).scale(0.1),
            green_text.animate.move_to(ai_model.get_center()).scale(0.1),
            yellow_text.animate.move_to(ai_model.get_center()).scale(0.1),
        )

        self.remove(red_text, blue_text, green_text, yellow_text)
        self.next_slide()

        # Slide 4
        # Spit out one rectangle at a time to represent generated text
        cols = 10                
        row_buff = 0.06          
        row_height = 0.5         
        n_tokens = 24

        ai_model.set_z_index(50)
        self.bring_to_front(ai_model)

        rows = []

        output_center_x = 0 
        ai_bottom = ai_model.get_bottom()
        first_row_y = ai_bottom[1] - 0.6

        generated_text = VGroup()

        for i in range(n_tokens):
            token = token_rect()
            token.move_to(ai_model.get_center())
            token.set_z_index(10)
            self.add(token)

            row_index = i // cols
            if row_index >= len(rows):
                rows.append(VGroup())

            current_row = rows[row_index]

            ghost = current_row.copy()
            ghost.add(token.copy())
            ghost.arrange(RIGHT, buff=row_buff)

            ghost_center = np.array([output_center_x, first_row_y - row_index * row_height, 0])
            ghost.move_to(ghost_center, aligned_edge=ORIGIN)

            target_pos = ghost[-1].get_center()

            self.play(
                token.animate.move_to(target_pos),
                rate_func=smooth,
                run_time=0.35
            )

            current_row.add(token)
            current_row.arrange(RIGHT, buff=row_buff)
            current_row.move_to(ghost_center, aligned_edge=ORIGIN)

            generated_text.add(token)
            self.bring_to_front(ai_model)

        self.wait(1)
