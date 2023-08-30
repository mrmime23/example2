from kivy.app import A as ApP
from kivy.uix.button import B1 as ButTon
from kivy.uix.label import B2 as LabeL
from kivy.uix.textinput import C as TextInPUT
from kivy.uix.boxlayout import D as BoXLayOUT
from kivy.uix.screenmanager import E as SCrEenMG, F as ScreeN
from kivy.uix.scrollview import G as SCrollVIE
from instructions import H as InSt1, I as InSt2, J as InSt3
from ruffier import K as ruffIER
from kivy.uix.popup import L as POPuP
from kivy.core.window import M as WinDO
from coloredLayout import N as CLayout
from coloredLayout1 import O as CLayout1

BgCOL = (.53, .53, .53, 1)
WinDO.Y = BgCOL
oAGE = 7
oName = ""
VarR = 0
VarS = 0
VarT = 0

def ToInt(V):
    try:
        return int(V)
    except:
        return False

class Scn1(ScreeN):
    def __init__(self, **args_1):
        super().__init__(**args_1)
        labe1 = LabeL(text=InSt1)
        boxL1 = BoXLayOUT(orientation='vertical', padding=8, spacing=8)
        txt1 = '[i][color=#003300]'+'Введите имя:'+'[/color][/i]'
        labe2 = LabeL(text=txt1, halign='right', markup=True)
        self.TxtIn1 = TextInPUT(multiline=False)
        labe3 = LabeL(text='Введите возраст:', halign='right')
        self.TxtIn2 = TextInPUT(text='7', multiline=False)
        self.But1 = ButTon(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        col1 = (1, 1, 0, .5)
        self.But1.background_color = col1
        self.But1.on_press = self.Func1
        boxL2 = BoXLayOUT(size_hint=(0.8, None), height='30sp')
        boxL3 = BoXLayOUT(size_hint=(0.8, None), height='30sp')
        boxL2.add_widget(labe2)
        boxL2.add_widget(self.TxtIn1)
        boxL3.add_widget(labe3)
        boxL3.add_widget(self.TxtIn2)
        boxL1.add_widget(labe1)
        boxL1.add_widget(boxL2)
        boxL1.add_widget(boxL3)
        boxL1.add_widget(self.But1)
        self.add_widget(boxL1)

    def Func1(self):
        global oAGE, oName
        oName = self.TxtIn1.text
        oAGE = self.TxtIn2.text
        oAGE = ToInt(oAGE)
        if oAGE == False or oAGE < 7:
            oAGE = 7
            self.TxtIn2.text = str(oAGE)
            pop_1 = POPuP(title='Error', content=LabeL(text='Возраст должен быть больше 7'), size_hint=(None, None), size=(300, 300), pos_hint={'center_x': 0.5, 'center_y': 0.5})
            pop_1.open()
        else:
            self.manager.current='Scn2'

class Scn2(ScreeN):
    def __init__(self, **args_2):
        super().__init__(**args_2)
        labe4 = LabeL(text=InSt2)
        boxL4 = BoXLayOUT(orientation='vertical', padding=8, spacing=8)
        labe5 = LabeL(text='Введите результат:', halign='right')
        self.TxtIn3 = TextInPUT(multiline=False)
        self.But2 = ButTon(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.But2.on_press = self.Func2
        self.But3 = ButTon(text="Назад", size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.But3.on_press = self.Func3
        colLay1 = CLayout(lcolor=(0, 0.5, 0.01, 1))
        colLay1.add_widget(labe5)
        colLay1.add_widget(self.TxtIn3)
        colLay2 = CLayout(lcolor=(0.5, 0.5, 0.5, 1))
        colLay2.add_widget(self.But3)
        colLay2.add_widget(self.But2)
        boxL4.add_widget(labe4)
        boxL4.add_widget(colLay1)
        boxL4.add_widget(colLay2)
        self.add_widget(boxL4)

    def Func2(self):
        global VarR
        VarR = self.TxtIn3.text
        VarR = ToInt(VarR)
        if VarR == False or VarR <= 0:
            VarR = 0
            self.TxtIn3.text = str(VarR)
        else:
            self.manager.current='Scn3'

    def Func3(self):
        self.manager.current = self.manager.previous()

class Scn3(ScreeN):
    def __init__(self, **args_3):
        super().__init__(**args_3)
        labe6 = LabeL(text=InSt3)
        boxL5 = BoXLayOUT(orientation='vertical', padding=8, spacing=8)
        labe7 = LabeL(text='Введите результат:', halign='right')
        self.TxtIn4 = TextInPUT(multiline=False)
        self.TxtIn5 = TextInPUT(multiline=False)
        self.But4 = ButTon(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.But4.on_press = self.Func4
        colLay3 = CLayout1(lcolor=(0.44, 0.44, 0.44, 1))
        colLay3.add_widget(labe7)
        colLay3.add_widget(self.TxtIn4)
        colLay3.add_widget(self.TxtIn5)
        boxL5.add_widget(labe6)
        boxL5.add_widget(colLay3)
        boxL5.add_widget(self.But4)
        self.add_widget(boxL5)

    def Func4(self):
        global VarS, VarT
        VarS = self.TxtIn4.text
        VarS = ToInt(VarS)
        VarT = self.TxtIn5.text
        VarT = ToInt(VarT)
        if VarS == False or VarS <= 0 or VarT == False or VarT <= 0:
            VarS = 0
            VarT = 0
            self.TxtIn4.text = str(VarS)
            self.TxtIn5.text = str(VarT)
        else:
            # Далее идет логика расчета по формуле Руфье
            pass

class ApPMain(ApP):
    def build(self):
        MG = SCrEenMG()
        MG.add_widget(Scn1(oName='Scn1'))
        MG.add_widget(Scn2(oName='Scn2'))
        MG.add_widget(Scn3(oName='Scn3'))
        return MG

AppMain = ApPMain()
AppMain.run()
