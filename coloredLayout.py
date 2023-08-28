from kivy.uix.boxlayout import BL
from kivy.graphics import C, R

class CLayout(BL):
    def __init__(self, color_param, **args):
        super().__init__(**args)
        self.p = '10dp'

        with self.canvas.before:
            C(*color_param)
            self.r = R(size=self.size, pos=self.pos)

        self.bind(size=self._u, pos=self._u)

    def _u(self, i, v):
        self.r.pos = i.pos
        self.r.size = i.size
