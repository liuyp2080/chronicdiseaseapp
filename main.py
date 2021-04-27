# -*-coding:utf-8-*-
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
import numpy as np
import kivy
from kivy.garden.xpopup import XPopup
from kivy.core.text import LabelBase
import evassistant as ev
# # 加载字体资源
kivy.resources.resource_add_path("f://pyground/kivy/Fonts")
# font1 = kivy.resources.resource_find("MSYH.TTC")
# #通过labelBase
LabelBase.register("MSYH","MSYH.TTC")
# kivy.core.text.Label.register("MSYH","MSYH.TTC")
Builder.load_string("""
# kivy=2.0.0
<MenuScreen>:
    BoxLayout:
        orientation:'vertical' 
        ActionBar:
            id:bar
            ActionView:
                ActionPrevious:
                    title:'M.D.N'
                    font_name:"MSYH"
                    markup:True
                    with_previous:False
                ActionButton:
                    text:"按钮"
                    font_name:"MSYH"
        Accordion:
            orientation:'vertical'
            AccordionItem:
                title:'Introduction'
                GridLayout:
                    cols:1
                    canvas:
                        Color:
                            rgb:1,1,0.8
                        Rectangle:
                            pos:self.pos
                            size:self.size
                    Label:
                        text:root.txt
                        font_name:"MSYH"
                        color: 0,0.2,0.4,1
                        markup:True
                        text_size: self.size
                        line_height:1.2
                        padding_x:2
                        halign: 'center'
                        valign:'center'
            AccordionItem:
                title:"Content"
                GridLayout:
                    cols:1
                    pos_hint: {"center_x": .5, "center_y": .5}
                    Button:
                        text:'2型糖尿病肾病'
                        on_press:root.manager.current='thyroid'  
                        # background_normal:''
                        # background_color:(0,0.6,1,1)
                    Button:
                        text:"其它"
                    Button:
                        text:"儿科"
                    Button:
                        text:"重症"
            
<screen1>:
    BoxLayout:
        orientation:'vertical'
        ActionBar:
            id:bar
            ActionView:
                ActionPrevious:
                    title:'2型糖尿病肾病'
                    font_name:"MSYH"
                    markup:True
                    with_previous:True
                    on_press:root.manager.current="menu"
                
        TabbedPanel:
            id:tp
            do_default_tab:False
            canvas.before:
                Color:
                    rgb:0.4,0.4,0.6
                Rectangle:
                    pos:self.pos
                    size:self.size
            TabbedPanelItem:
                text:"计算器一"
                font_name:"MSYH"
                border:'off'
                GridLayout:
                    cols:1
                    padding: '10dp'
                    spacing:'10dp' 
                    canvas.before:
                        Color:
                            rgb:0.8,0.8,1
                        Rectangle:
                            pos:self.pos
                            size:self.size 
                    GridLayout:
                        cols:3
                        DarkLabel:
                            text:"性别："
                        ToggleButton:
                            id:female
                            text:'女' 
                            group:'gender'
                            state:'down'
                        ToggleButton:
                            id:male
                            text:"男"
                            group:'gender'
                    GridLayout:
                        cols:4
                        DarkLabel:
                            text:"糖尿病病程："
                        ToggleButton:
                            id:<5year
                            text:'<5年' 
                            group:'duration'
                            state:'down'
                        ToggleButton:
                            id:5-10year
                            text:"5-10年"
                            group:'duration'
                        ToggleButton:
                            id:>10year
                            text:">10年"
                            group:'duration'
                    GridLayout:
                        cols:3
                        DarkLabel:
                            text:"糖尿病视网膜病变："
                        ToggleButton:
                            text:"无"
                            group:'dr'
                            state:"down"
                        ToggleButton:
                            id:dr_yes
                            text:'有'
                            group:'dr'
                    GridLayout:
                        cols:4
                        DarkLabel:
                            text:"血尿："
                        ToggleButton:
                            id:<5num
                            text:'<5个' 
                            group:'hematuria'
                            state:'down'
                        ToggleButton:
                            id:5-10num
                            text:"5-10个"
                            group:'hematuria'
                        ToggleButton:
                            id:>10num
                            text:">10个"
                            group:'hematuria'
                    GridLayout:
                        cols:3
                        DarkLabel:
                            text:'贫血:'
                        ToggleButton:
                            id:anemia_no
                            text:'否'
                            group:'anemia'
                            state:'down'
                        ToggleButton:
                            id:anemia_yes
                            text:'是'
                            group:'anemia'
                    GridLayout:
                        cols:3
                        DarkLabel:
                            text:'糖化血红蛋白:'
                        ToggleButton:
                            id:HbA1c_no
                            text:'<7%'
                            group:'HbA1c'
                            state:'down'
                        ToggleButton:
                            id:HbA1c_yes
                            text:'≥7%'
                            group:'HbA1c'   
                    GridLayout:
                        cols:3
                        DarkLabel:
                            text:'肾小球滤过率:'
                        ToggleButton:
                            id:eGFR_high
                            text:'≥90'
                            group:'gfr'
                            state:'down'
                        ToggleButton:
                            id:eGFR_low
                            text:'<90'
                            group:'gfr'
                    GridLayout:
                        cols:4
                        DarkLabel:
                            text:"尿蛋白排除量："
                        ToggleButton:
                            id:<1g
                            text:'<1g/24h' 
                            group:'upe'
                            state:'down'
                        ToggleButton:
                            id:1-3g
                            text:"1-3.5g/24h"
                            group:'upe'
                        ToggleButton:
                            id:>3g
                            text:">3.5g/24h"
                            group:'upe'
                    GridLayout:
                        cols:3
                        DarkLabel:
                            text:"血压："
                        ToggleButton:
                            id:bp_normal
                            text:'SBP<140且DBP<90'
                            group:'bp'
                            state:'down'
                        ToggleButton:
                            id:bp_unnormal
                            text:'SBP≥140或DBP≥90'
                            group:'bp'
                    AButton:
                        text:'计算'
                        on_state: root.on_press_prob()
                        pos_hint:{'center_x':.5,'center_y':.5}
                        size_hint:(0.9,0.9)              
                    DarkLabel:
                        id:prob_label
                        text:" "
                        halign:'left'
                    GridLayout:
                        cols:4
                        spacing: '10dp'         
                        AButton:
                            text:'摘要'
                            on_release:root.abstract_cN0()
                            pos_hint:{'center_x':.5,'center_y':.5} 
                            size_hint:(0.9,0.9)
                        AButton:
                            text:'列线图'
                            on_release:root.thyroid_cN0()
                            pos_hint:{'center_x':.5,'center_y':.5}
                            size_hint:(0.9,0.9)
                        AButton:
                            text:"说明"

                            
<AButton@Button>:
    font_name:"MSYH"
    background_normal:""
    background_color: 0,0.6,1,1
<Label@Label>:
    font_name:"MSYH"

<DarkLabel@Label>:
    font_name:"MSYH"
    color:(0.4,0.4,0.6,1)
<ActionBar@ActionBar>:
    canvas:
        Color:
            rgb:0.4,0.4,0.6
        Rectangle:
            pos:self.pos
            size:self.size
<ToggleButton@ToggleButton>:
    font_name:"MSYH"

""")

class MenuScreen(Screen):

    txt='''
    [anchor=title][size=24]列线图使用说明[/size]
    [anchor=content]首先要明确的一点就是,模型都有一定的适用范围,也有优劣(区分度和校准度)之分,信息集中反映在"摘要"和"列线图"中,为此,我们在每个模型的下方提供了摘要和列线图原图.在使用列线图辅助临床决策之前，还需要确定该列线图是不是顺利通过了外部验证来证明其有效性.区分度和校准度是反应模型有效性的指标。区分度的通俗理解是"模型中是否能够找出一个点来区分发生事件和未发生事件的人群";校准度通俗的理解是"模型的预测概率和人群实际的发生概率的一致性".我们了解到做过外部验证的模型会在模型名称后面做标记,没有标记的模型代表没有经过外部验证,使用时要谨慎.
    '''

class screen1(Screen):

    def on_press_prob(self, *args):
        duration1 = self.ids['5-10year'].state
        if duration1=="down":
            duration_5=1
        else:
            duration_5=0
        duration2=self.ids['>10year'].state
        if duration2=='down':
            duration_10=1
        else:
            duration_10=0
        sex = self.ids['female'].state
        if sex == 'down':
            sex_female = 1
        else:
            sex_female = 0
        dr=self.ids['dr_yes'].state
        if dr=='down':
            dr_yes =1
        else:
            dr_yes=0
        hematuria1=self.ids['>10num'].state
        if hematuria1=='down':
            hematuria_10 = 1
        else:
            hematuria_10 = 0
        hematuria2=self.ids['5-10num'].state
        if hematuria2=='down':
            hematuria_5=1
        else:
            hematuria_5=0
        anemia=self.ids['anemia_yes'].state
        if anemia=='down':
            anemia_yes=1
        else:
            anemia_yes=0
        HbA1c=self.ids['HbA1c_yes'].state
        if HbA1c=='down':
            hba1c=1
        else:
            hba1c=0
        gfr=self.ids['eGFR_low'].state
        if gfr=='down':
            egfr_90=1
        else:
            egfr_90=0
        upe1=self.ids['>3g'].state
        if upe1=='down':
            upe_3=1
        else:
            upe_3=0
        upe2=self.ids['1-3g'].state
        if upe2=='down':
            upe_1=1
        else:
            upe_1=0
        bp=self.ids['bp_unnormal'].state
        if bp=='down':
            bp_unnormal=1
        else:
            bp_unnormal=0

        list_or = [0.35, 7.46, 2.99, 8.27, 0.15,0.70,3.48,1.43,3.78,2.24,1.76,2.17]
        list_para = [sex_female, duration_10, duration_5,dr_yes,hematuria_10,hematuria_5,anemia_yes,hba1c,bp_unnormal,upe_3,upe_1,egfr_90]
        intercept = 0.017   
        model=ev.logistic(ls_or=list_or,ls_xvar=list_para,intercept=intercept)
        prob = model.prob()
        label = self.ids['prob_label']
        label.text = "患者患糖尿病肾病的概率为: " + str(round(prob, 2) * 100) + '%'

    def abstract_cN0(self):
        self.the_abstract_cN0 = XPopup(title='The Abstract',
                                       content=Image(source='abs_diabete2_kidney1.png'),
                                       title_size=20, size_hint=(1, 1), min_width=600, min_height=800)
        self.the_abstract_cN0.open()

    def thyroid_cN0(self):
        self.the_thyroid_cN0 = XPopup(title="Alignment", 
                                      title_size=20,
                                      content=Image(source='alignment_diabete_kidney1.png'), size_hint=(1, 1), min_width=600,
                                      min_height=800)
        self.the_thyroid_cN0.open()


class DynamicnomoApp(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(screen1(name='thyroid'))
        return sm
DynamicnomoApp().run()
