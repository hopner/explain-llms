from manim import *
from manim_slides import Slide

class ReadBookScene(Slide):
    def construct(self):
        
        # Slide 1: Nonsense text displayed
        nonsense_text = Text("the suberins cupellation bailor nonhieratical")
        self.play(Write(nonsense_text))

        self.next_slide()

        # Slide 2: Real text is displayed and is put into the AI model
        self.play(FadeOut(nonsense_text))

        with open("input/moby_dick_excerpt.txt", "r") as file:
            real_text_content = file.read()
        
        paragraph = Paragraph(real_text_content).scale(0.3).to_edge(LEFT)
        ai_box = Rectangle(height=3, width=3, fill_color=WHITE, fill_opacity=1).to_edge(RIGHT)
        ai_label = Text("AI Model", color=BLACK).move_to(ai_box.get_center())
        ai_model = VGroup(ai_box, ai_label)

        self.play(Write(paragraph), Create(ai_model))
        self.wait()

        self.play(
            paragraph.animate.move_to(ai_box.get_center()).scale(0.3)
        )
        self.remove(paragraph)
        self.play(
            ai_model.animate.move_to(ORIGIN)
        )
        self.next_slide()

        # Slide 3: AI model is shaken and 3 words fall out at the bottom one by one:
        # Call me Cato

        self.play(ai_model.animate.shift(UP * 0.2), run_time=0.15)
        self.play(ai_model.animate.shift(DOWN * 0.4), run_time=0.2)
        self.play(ai_model.animate.shift(UP * 0.4), run_time=0.2)
        self.play(ai_model.animate.shift(DOWN * 0.4), run_time=0.2)
        call = Text("Call", font_size=40).move_to(ai_box.get_center()+DOWN*0.5)
        self.play(call.animate.move_to(ORIGIN + DOWN * 2 + LEFT), run_time=1)
        self.play(ai_model.animate.shift(UP * 0.4), run_time=0.2)
        self.play(ai_model.animate.shift(DOWN * 0.4), run_time=0.2)
        me = Text("me", font_size=40).move_to(ai_box.get_center()+DOWN*0.5)
        self.play(me.animate.move_to(ORIGIN + DOWN * 2), run_time=1)
        self.play(ai_model.animate.shift(UP * 0.4), run_time=0.2)
        self.play(ai_model.animate.shift(DOWN * 0.4), run_time=0.2)
        self.play(ai_model.animate.shift(UP * 0.4), run_time=0.2)
        self.play(ai_model.animate.shift(DOWN * 0.4), run_time=0.2)
        self.play(ai_model.animate.shift(UP * 0.2), run_time=0.15)
        cato = Text("Cato", font_size=40).move_to(ai_box.get_center()+DOWN*0.5)
        self.play(cato.animate.move_to(ORIGIN + DOWN * 2 + RIGHT), run_time=1)
        self.next_slide()

        # Slide 4: Highlight Cato in red
        self.play(cato.animate.set_color(RED), run_time=1)
