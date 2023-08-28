from kivy.app import A
from kivy.uix.button import B1
from kivy.uix.label import B2
from kivy.uix.textinput import C
from kivy.uix.boxlayout import D
from kivy.uix.screenmanager import E, F
from kivy.uix.scrollview import G
from instructions import H, I, J
from ruffier import K
from kivy.uix.popup import L
from kivy.core.window import M
from coloredLayout import N
from coloredLayout1 import O

X = (.53, .53, .53, 1)
M.Y = X
Z = 7
Q = ""
R = 0
S = 0
T = 0

def U(V):
    try:
        return int(V)
    except:
        return False

class W(F):
    def __init__(self, **aa):
        super().__init__(**aa)
        bb = B2(text=H)
        cc = D(orientation='vertical', padding=8, spacing=8)
        dd = '[i][color=#003300]'+'Введите имя:'+'[/color][/i]'
        ee = B2(text=dd, halign='right', markup=True)
        self.ff = C(multiline=False)
        gg = B2(text='Введите возраст:', halign='right')
        self.hh = C(text='7', multiline=False)
        self.ii = B1(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        jj = (1, 1, 0, .5)
        self.ii.background_color = jj
        self.ii.on_press = self.kk
        ll = D(size_hint=(0.8, None), height='30sp')
        mm = D(size_hint=(0.8, None), height='30sp')
        ll.add_widget(ee)
        ll.add_widget(self.ff)
        mm.add_widget(gg)
        mm.add_widget(self.hh)
        cc.add_widget(bb)
        cc.add_widget(ll)
        cc.add_widget(mm)
        cc.add_widget(self.ii)
        self.add_widget(cc)

    def kk(self):
        global Z, Q
        Q = self.ff.text
        Z = self.hh.text
        Z = U(Z)
        if Z == False or Z < 7:
            Z = 7
            self.hh.text = str(Z)
            nn = L(title='Error', content=B2(text='Возраст должен быть больше 7'), size_hint=(None, None), size=(300, 300), pos_hint={'center_x': 0.5, 'center_y': 0.5})
            nn.open()
        else:
            self.manager.current='oo'

class PP(F):
    def __init__(self, **qq):
        super().__init__(**qq)
        rr = B2(text=I)
        ss = D(orientation='vertical', padding=8, spacing=8)
        tt = B2(text='Введите результат:', halign='right')
        self.uu = C(multiline=False)
        self.vv = B1(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.vv.on_press = self.ww
        self.xx = B1(text="Назад", size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.xx.on_press = self.yy
        zz = N(lcolor=(0, 0.5, 0.01, 1))
        zz.add_widget(tt)
        zz.add_widget(self.uu)
        aa1 = N(lcolor=(0.5, 0.5, 0.5, 1))
        aa1.add_widget(self.xx)
        aa1.add_widget(self.vv)
        ss.add_widget(rr)
        ss.add_widget(zz)
        ss.add_widget(aa1)
        self.add_widget(ss)

    def ww(self):
        global R
        R = self.uu.text
        R = U(R)
        if R == False or R <= 0:
            R = 0
            self.uu.text = str(R)
        else:
            self.manager.current='bb1'

    def yy(self):
        self.manager.current = self.manager.previous()

class CC(F):
    def __init__(self, **dd1):
        super().__init__(**dd1)
        ee1 = B2(text=J)
        ff1 = D(orientation='vertical', padding=8, spacing=8)
        gg1 = B2(text='Введите результат:', halign='right')
        self.hh1 = C(multiline=False)
        self.ii1 = C(multiline=False)
        self.jj1 = B1(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.jj1.on_press = self.kk1
        ll1 = O(lcolor=(0.44, 0.44, 0.44, 1))
        ll1.add_widget(gg1)
        ll1.add_widget(self.hh1)
        ll1.add_widget(self.ii1)
        ff1.add_widget(ee1)
        ff1.add_widget(ll1)
        ff1.add_widget(self.jj1)
        self.add_widget(ff1)

    def kk1(self):
        global S, T
        S = self.hh1.text
        S = U(R)
        T = self.ii1.text
        T = U(T)
        if S == False or S <= 0:
            S = 0
            self.hh1.text = str(S)
        elif T == False or T <= 0:
            T = 0
            self.ii1 = T
        else:
            self.manager.current='mm1'

class NN(F):
    pass

class OO(F):
    def __init__(self, **pp1):
        super().__init__(**pp1)
        global R, S, T
        qq1 = D(orientation='vertical', padding=8, spacing=8)
        rr1 = K(R, S, T, Z)
        ss1 = B2(text='Результат:' + str(rr1), halign='right')
        qq1.add_widget(ss1)
        self.add_widget(qq1)


class P(A):
    def build(self):
        tt1 = E()
        tt1.add_widget(W(name='uu1'))
        tt1.add_widget(PP(name='oo'))
        tt1.add_widget(CC(name='bb1'))
        tt1.add_widget(NN(name='vv1'))
        tt1.add_widget(OO(name='mm1'))
        return tt1

uu2 = P()
uu2.run()
