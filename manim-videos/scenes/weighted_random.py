from manim import *
from manim_slides import Slide
import numpy as np

class WeightedRandomScene(Slide):
    def construct(self):
        
        # Slide 1 - An histogram gives us the word "the"

        colors=[
            BLUE,
            GREEN,
            RED,
            ORANGE,
            PURPLE,
            TEAL,
            YELLOW,
            PINK,
        ]

        probs = [0.28, 0.22, 0.15, 0.12, 0.08, 0.07, 0.05, 0.03]
        labels = ["cat", "dog", "man", "woman", "robot", "child", "city", "idea"]

        chart = BarChart(
            values=probs,
            bar_names=labels,
            y_range=[0, 0.3, 0.05],
            bar_colors=colors,
        )

        self.play(
            Create(chart),
            run_time=2
        )
        self.next_slide()

        # Slide 2 - Bar chart morphs into a lucky wheel

        sectors = VGroup()
        labels_group = VGroup()
        start_angle = 0

        for label, p, color in zip(labels, probs, colors):
            angle = p * TAU
            wedge = Sector(
                radius=3,
                start_angle=start_angle,
                angle=angle,
                color=color,
                fill_opacity=0.8,
            )

            label_angle = start_angle + angle / 2
            label_text = Text(label, font_size=24)
            label_text.move_to(
                0.7*3*np.array([
                    np.cos(label_angle),
                    np.sin(label_angle),
                    0
                ])
            )
            label_text.rotate(label_angle)

            sectors.add(wedge)
            labels_group.add(label_text)
            start_angle += angle

        wheel = VGroup(sectors, labels_group)
        wheel.move_to(chart.get_center())

        triangle = Triangle(
            fill_color=WHITE,
            fill_opacity=1,
            stroke_width=0
        ).scale(0.2).rotate(5*PI/4 - PI/2).move_to((2.65) * np.array([
            np.cos(PI/4),
            np.sin(PI/4),
            0
        ]))

        self.play(
            ReplacementTransform(chart, wheel),
            Create(triangle),
            run_time=3
        )


        final_angle = PI/2 + .6
        spins = 5
        rate_func = lambda t: 1 - np.exp(-5 * t)
        #rate_func = lambda t: np.sin(np.pi * t) ** 2
        self.next_slide()

        # Slide 3 - Spin the wheel
        self.play(
            Rotate(
                wheel,
                angle=spins * TAU + final_angle,
                rate_func=rate_func,
                run_time=4
            )
        )

        prediction = Text("robot", font_size=36).next_to(wheel, RIGHT, buff=1)
        self.play(
            Write(prediction)
        )
        self.next_slide()
        # Slide 4 - Move/scale wheel and triangle to the top half towards the right
        #   and make a split screen and show that the spin has a different outcome on the bottom half
        top_wheel_group = VGroup(wheel, triangle)
        
        sepparator = Line(
            start=5*LEFT,
            end=5*RIGHT,
            stroke_width=2
        )

        bottom_wheel = wheel.copy()
        bottom_triangle = triangle.copy()
        bottom_wheel_group = VGroup(bottom_wheel, bottom_triangle)
        bottom_wheel_group.scale(.5).move_to(3*LEFT + 2*DOWN)

        self.play(
            FadeOut(prediction),
            top_wheel_group.animate.scale(.5).move_to(3*LEFT + 2*UP),

        )
        self.wait(.5)
        self.play(
            Create(sepparator),
            Create(bottom_wheel_group),
        )
        self.wait()

        final_top_angle = PI/2 + .2
        final_bottom_angle = PI/2 + 2.4
        self.play(
            Rotate(
                wheel,
                angle=spins * TAU + final_top_angle,
                rate_func=rate_func,
                run_time=4
            ),
            Rotate(
                bottom_wheel,
                angle=spins * TAU + final_bottom_angle,
                rate_func=rate_func,
                run_time=4
            ),
        )

        top_prediction = Text("man", font_size=36).next_to(top_wheel_group, RIGHT, buff=2)
        bottom_prediction = Text("cat", font_size=36).next_to(bottom_wheel_group, RIGHT, buff=2)

        self.play(
            Write(top_prediction),
            Write(bottom_prediction)
        )

