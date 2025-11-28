from manim import *
import numpy as np

class MiniChart(VGroup):
    def __init__(self, values=None, width=1.2, height=0.8, bar_color=BLUE, **kwargs):
        super().__init__(**kwargs)
        if values is None:
            values = np.random.rand(5)

        self.values = np.array(values)
        self.values = self.values / self.values.max()

        self.width = width
        self.height = height
        self.bar_color = bar_color

        self.chart = self.as_histogram()
        self.add(self.chart)

    def as_histogram(self):
        n = len(self.values)
        bar_width = self.width / n

        bars = VGroup()
        for i, v in enumerate(self.values):
            bar = Rectangle(
                width=bar_width,
                height=v * self.height,
                fill_opacity=1,
                fill_color=self.bar_color,
                stroke_width=0,
            )
            bar.move_to([
                i * bar_width - self.width/2 + bar_width/2,
                -self.height/2 + bar.height/2,
                0
            ])
            bars.add(bar)

        frame = Rectangle(width=self.width, height=self.height, stroke_width=1)
        return VGroup(frame, bars)

    def as_pie_chart(self):
        values = self.values
        angles = 2 * np.pi * values / values.sum()

        start = 0
        group = VGroup()

        for i, ang in enumerate(angles):
            shade = interpolate_color(self.bar_color, WHITE, i/len(angles))
            wedge = Sector(
                radius=self.height * 0.6,
                start_angle=start,
                angle=ang,
                fill_color=shade,
                fill_opacity=1,
                stroke_width=0,
            )
            group.add(wedge)
            start += ang

        return group

    def morph_to_pie(self, scene, run_time=1):
        pie = self.as_pie_chart()
        scene.play(Transform(self.chart, pie), run_time=run_time)
        self.chart = pie


    def animate_values(self, scene, new_values, run_time=0.5):
        """
        Animate the histogram bars changing height to match new_values.
        Automatically rescales and normalizes.
        Works only when currently in histogram form.
        """
        new_values = np.array(new_values, dtype=float)
        new_values = new_values / new_values.max()

        # If number of bars changed, completely rebuild
        if len(new_values) != len(self.values):
            self.values = new_values
            new_hist = self.as_histogram()
            scene.play(Transform(self.chart, new_hist), run_time=run_time)
            self.chart = new_hist
            return

        # Animate bar height changes
        _, bars = self.chart  # unpack frame, bars

        animations = []
        for bar, v in zip(bars, new_values):
            new_height = v * self.height
            animations.append(
                bar.animate.stretch_to_fit_height(new_height).move_to(
                    [bar.get_x(), -self.height/2 + new_height/2, 0]
                )
            )

        scene.play(*animations, run_time=run_time)
        self.values = new_values

    def spin_pie(self, scene, spins=0, run_time=2, clockwise=True):
        """
        Spin the pie chart around its center.
        Works only when currently in pie chart form.
        """
        direction = -1 if clockwise else 1
        if spins == 0:
            spins = np.random.uniform(1, 4)
        angle = direction * spins * TAU

        scene.play(
            Rotate(
                self.chart,
                angle=angle,
                about_point=self.chart.get_center(),
                rate_func= lambda t: 1 - np.exp(-5 * t)
            ), run_time=run_time
        )
