from manim import *
from manim_slides import Slide

class NLTKScene(Slide):
    def construct(self):

        # Slide 1 - write example sentence
        sentence = f"Dr. Hall looked at the file marked ‘N.A.S.A.’ and sighed, ‘But first... let’s take a step back.’"
        sentence_text = Text(sentence, font_size=36).scale(0.5)
        abbreviation = sentence_text[28:36]
        honorific = sentence_text[:3]
        ellipsis = sentence_text[51:58]

        others = VGroup(
            sentence_text[3:28],
            sentence_text[36:51],
            sentence_text[58:]
        )

        self.play(Write(sentence_text))
        self.next_slide()

        # Slide 2 - Highlight special cases
        self.play(
            FadeOut(others),
        )
        self.next_slide()

        # Slide 3 - Show how these are split incorrectly with whitespace/punctuation tokenizers
        a_split = VGroup(abbreviation.split())

        h_split = honorific.split()
        h_split = VGroup(VGroup(h_split[:2]), h_split[-1])

        e_split = ellipsis.split()
        e_split = VGroup(VGroup(e_split[:4]), e_split[4:])

        self.play(
            a_split.animate.arrange(RIGHT, buff=0.4).move_to(ORIGIN + DOWN * 1),
            h_split.animate.arrange(RIGHT, buff=0.4).move_to(ORIGIN + UP * 1 + LEFT * 3),
            e_split.animate.arrange(RIGHT, buff=0.4).move_to(ORIGIN + UP * 1 + RIGHT * 3),
        )
        self.next_slide()

        # Slide 4 - Show correct NLTK tokenization
        correct_a = VGroup(Text("N.A.S.A.")).scale(0.5).move_to(a_split.get_center())
        correct_h = VGroup(Text("Dr.")).scale(0.5).move_to(h_split.get_center())
        correct_e = VGroup(Text("first"),Text("...")).scale(0.5).arrange(RIGHT, buff=0.4).move_to(e_split.get_center())

        self.play(
            Transform(a_split, correct_a),
            Transform(h_split, correct_h),
            Transform(e_split, correct_e),
        )
        self.next_slide()

        # Slide 5 - language specific examples
        self.play(
            FadeOut(VGroup(a_split, h_split, e_split)),
        )
        french = Text("l'amour").move_to(ORIGIN + LEFT * 3 + DOWN * 2)
        french2 = Text("Qu'est-ce que c'est?").move_to(ORIGIN + RIGHT * 4 + UP * 1)
        italian = Text("dell’acqua fredda").move_to(ORIGIN + LEFT * 3 + UP * 2)
        spanish = MarkupText("¿Qué pasó?").move_to(ORIGIN + DOWN * 1)
        self.play(
            Write(french), Write(french2), Write(italian), Write(spanish)
        )
        self.next_slide()

        # Slide 6 - period is EOS
        self.play(
            FadeOut(VGroup(french, french2, italian, spanish)),
        )

        lbl = Tex("$. \\rightarrow EOS$").scale(1.5)
        self.play(Write(lbl))

