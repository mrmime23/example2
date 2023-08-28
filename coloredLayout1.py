from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle, Ellipse

class C1(BoxLayout):   # Unklarer Name
    def __init__(self, c, **kwargs):   # Kurzer, unklarer Name für den Parameter
        super().__init__(**kwargs)
        self.p = '10dp'   # Kurzer, unklarer Name

        with self.canvas.before:
            Color(*c)   # Kurzer, unklarer Name für den Parameter
            self.r = Ellipse(size=self.size, pos=self.pos)   # Kurzer, unklarer Name

        self.bind(size=self.ur, pos=self.ur)   # Kurzer, unklarer Name für die Methode

    def ur(self, i, v):   # Kurze und unklare Namen für die Methode und Parameter
        self.r.pos = i.pos   # Kurzer, unklarer Name für den Parameter
        self.r.size = i.size   # Kurzer, unklarer Name für den Parameter
