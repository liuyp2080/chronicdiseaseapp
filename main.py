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
from kivy.uix.popup import Popup
from kivy.core.text import LabelBase
import evassistant as ev
from kivy.uix.label import Label
# # 加载字体资源
kivy.resources.resource_add_path("./")
# font1 = kivy.resources.resource_find("MSYH.TTC")
# #通过labelBase
LabelBase.register("Droid","Droid-Sans-Fallback.ttf")
kivy.core.text.Label.register("Droid","Droid-Sans-Fallback.ttf")
Builder.load_string("""

<MenuScreen>:
    name:'Menu'
    BoxLayout:
        orientation:'vertical' 
        ActionBar:
            id:bar
            ActionView:
                ActionPrevious:
                    title:'慢性病预测模型'
                    font_name:"Droid"
                    markup:True
                    with_previous:False
                    app_icon:'logo.png'
                ActionButton:
                    text:"遇病一测，防微杜渐"
                    font_name:"Droid"
        Accordion:
            orientation:'vertical'
            AccordionItem:
                title:"预测模型筛选原则"
                collapse:False
                GridLayout:
                    cols:1
                    canvas:
                        Color:
                            rgb:1,1,0.8
                        Rectangle:
                            pos:self.pos
                            size:self.size
                    ScrollView:
                        do_scroll_x:False
                        do_scroll_y:True
                        Label:
                            size_hint_y:None
                            text:root.txt
                            font_name:"Droid"
                            color: 0,0.2,0.4,1
                            markup:True
                            height:self.texture_size[1]
                            text_size:self.width, None
                            line_height:1.2
                            # padding_x:2
                            valign: 'center'               
            AccordionItem:
                title:"慢性疾病"
                GridLayout:
                    cols:3
                    pos_hint: {"center_x": .5, "center_y": .5}
                    row_force_default:True
                    row_default_height:200
                    padding_y:10
                    canvas:
                        Color:
                            rgb:0.6,0.8,0.2
                        Rectangle:
                            pos:self.pos
                            size:self.size
                    Button:
                        text:'2型糖尿病肾病'
                        on_press:root.manager.current='screen1'  
                        # background_normal:''
                        # background_color:(0,0.6,1,1)
                    Button:
                        text:"2型糖尿病脑卒中"
                        on_press:root.manager.current='screen2'  
                    Button:
                        text:"2型糖尿病"
                        on_press:root.manager.current='screen4'  
                    Button:
                        text:"冠心病"
                        on_press:root.manager.current='screen5' 
            AccordionItem:
                title:"妊娠糖尿病"
                GridLayout:
                    cols:3
                    pos_hint: {"center_x": .5, "center_y": .5}
                    row_force_default:True
                    row_default_height:100
                    padding_y:10
                    Button:
                        text:'妊娠期糖尿病'
                        on_press:root.manager.current='screen3'  
                            # background_normal:''
                            # background_color:(0,0.6,1,1)
                        # Button:
                        #     text:"2型糖尿病脑卒中"
                        #     on_press:root.manager.current='screen2'  
                        # Button:
                        #     text:"2型糖尿病眼底病"
                        # Button:
                        #     text:"早老性痴呆"

            
<screen1>:
    name:'screen1'
    BoxLayout:
        orientation:'vertical'
        ActionBar:
            id:bar
            ActionView:
                ActionPrevious:
                    title:'2型糖尿病肾病'
                    font_name:"Droid"
                    markup:True
                    app_icon:'logo.png'
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
                text:"ID31865340"
                font_name:"Droid"
                # border:'off'
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
                        panding:10
                        DarkLabel:
                            text:"性别"
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
                        spacing:10
                        DarkLabel:
                            text:"糖尿病病程"
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
                            text:"视网膜病变"
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
                            text:"血尿"
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
                            text:'贫血'
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
                            text:'糖化血红蛋白'
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
                            text:'肾小球滤过率'
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
                            text:"尿蛋白排出量"
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
                            text:"高血压"
                        ToggleButton:
                            id:bp_normal
                            text:'SBP<140且DBP<90'
                            font_size:13
                            group:'bp'
                            state:'down'
                        ToggleButton:
                            id:bp_unnormal
                            text:'SBP≥140或DBP≥90'
                            font_size:13
                            group:'bp'
                    AButton:
                        text:'计算'
                        on_state: root.on_press_prob()
                        pos_hint:{'center_x':.5,'center_y':.5}
                        size_hint:(0.9,0.9)              
                    Label:
                        id:prob_label
                        text:" "
                        color:(0.4,0.4,0.6,1)
                    GridLayout:
                        cols:4
                        spacing: '10dp'         
                        AButton:
                            text:'模型信息表'
                            on_release:root.info_sheet()
                            pos_hint:{'center_x':.5,'center_y':.5} 
                        AButton:
                            text:'评价星级:3星'
                            on_release:root.conclusion()
                            pos_hint:{'center_x':.5,'center_y':.5}
                       
<screen2>:
    name:'screen2'
    BoxLayout:
        orientation:'vertical'
        ActionBar:
            id:bar
            ActionView:
                ActionPrevious:
                    title:'2型糖尿病脑卒中'
                    font_name:"Droid"
                    markup:True
                    app_icon:'logo.png'
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
                text:"ID32982965"
                font_name:"Droid"
                # border:'off'
                GridLayout:
                    cols:1
                    padding:'10dp'
                    spacing:'10dp' 
                    canvas.before:
                        Color:
                            rgb:0.8,0.8,1
                        Rectangle:
                            pos:self.pos
                            size:self.size 
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:"年龄"+str(age.value)
                        Slider:
                            id:age
                            min:25
                            max:90
                            step:1
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:"病程"+str(course.value)
                        Slider:
                            id:course
                            min:0
                            max:65
                            step:1
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:"收缩压"+str(sbp.value)
                        Slider:
                            id:sbp
                            min:-20
                            max:200
                            step:1
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:"舒张压"+str(dbp.value)
                        Slider:
                            id:dbp
                            min:45
                            max:120
                            step:1
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:'BMI'+str(bmi.value)
                        Slider:
                            id:bmi
                            min:14
                            max:40
                            step:1
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:'糖化血红蛋白'+str(HbA1c.value)
                        Slider:
                            id:HbA1c
                            min:4
                            max:13
                            step:1  
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:'甘油三酯'+str(tg.value)
                        Slider:
                            id:tg
                            min:0
                            max:13
                            step:1
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:"低密度脂蛋白"+str(ldl.value)
                        Slider:
                            id:ldl
                            min:0
                            max:3.5
                            step:0.1
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:"高密度脂蛋白"+str(hdl.value)
                        Slider:
                            id:hdl
                            min:0.6
                            max:3.4
                            step:0.1
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:"尿酸"+str(ua.value)
                        Slider:
                            id:ua
                            min:50
                            max:700
                            step:10
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:"肾小球滤过率"+str(egfr.value)
                        Slider:
                            id:egfr
                            min:-100
                            max:400
                            step:10
                    AButton:
                        text:'计算'
                        on_state: root.on_press_prob()
                        pos_hint:{'center_x':.5,'center_y':.5}
                        size_hint:(0.9,0.9)              
                    Label:
                        id:prob_label
                        text:" "
                        color:(0.4,0.4,0.6,1)
                    GridLayout:
                        cols:4
                        spacing: '10dp'         
                        AButton:
                            text:'模型信息表'
                            on_release:root.info_sheet()
                            pos_hint:{'center_x':.5,'center_y':.5} 
                        AButton:
                            text:'评价星级:4星'
                            on_release:root.conclusion()
                            pos_hint:{'center_x':.5,'center_y':.5}
<screen3>:
    name:'screen3'
    BoxLayout:
        orientation:'vertical'
        ActionBar:
            id:bar
            ActionView:
                ActionPrevious:
                    title:'妊娠期糖尿病'
                    font_name:"Droid"
                    markup:True
                    app_icon:'logo.png'
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
                text:"ID33277541"
                font_name:"Droid"
                # border:'off'
                GridLayout:
                    cols:1
                    padding:'10dp'
                    spacing:'10dp' 
                    canvas.before:
                        Color:
                            rgb:0.8,0.8,1
                        Rectangle:
                            pos:self.pos
                            size:self.size 
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:"年龄"+str(age.value)
                        Slider:
                            id:age
                            min:20
                            max:42  
                            step:1
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:"BMI"+str(bmi.value)
                        Slider:
                            id:bmi
                            min:14
                            max:36
                            step:1
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:"HbA1c"+str(hba1c.value)
                        Slider:
                            id:hba1c
                            min:4
                            max:6.6
                            step:0.1
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:'甘油三酯'+str(tg.value)
                        Slider:
                            id:tg
                            min:0
                            max:7
                            step:0.1
    
                    AButton:
                        text:'计算'
                        on_state: root.on_press_prob()
                        pos_hint:{'center_x':.5,'center_y':.5}
                        size_hint:(0.9,0.9)              
                    Label:
                        id:prob_label
                        text:" "
                        color:(0.4,0.4,0.6,1)
                    GridLayout:
                        cols:4
                        spacing: '10dp'         
                        AButton:
                            text:'模型信息表'
                            on_release:root.info_sheet()
                            pos_hint:{'center_x':.5,'center_y':.5} 
                        AButton:
                            text:'评价星级:2星'
                            on_release:root.conclusion()
                            pos_hint:{'center_x':.5,'center_y':.5}
<screen4>:
    name:'screen4'
    BoxLayout:
        orientation:'vertical'
        ActionBar:
            id:bar
            ActionView:
                ActionPrevious:
                    title:'2型糖尿病'
                    font_name:"Droid"
                    markup:True
                    app_icon:'logo.png'
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
                text:"ID32665620"
                font_name:"Droid"
                GridLayout:
                    cols:1
                    padding:'10dp'
                    spacing:'10dp' 
                    canvas.before:
                        Color:
                            rgb:0.8,0.8,1
                        Rectangle:
                            pos:self.pos
                            size:self.size 
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:"年龄"+str(age.value)
                        Slider:
                            id:age
                            min:20
                            max:100 
                            step:1
                    GridLayout:
                        cols:3
                        DarkLabel:
                            text:"性别"
                        ToggleButton:
                            id:female
                            text:'女'
                            group:'gender'
                            state:'down'
                        ToggleButton:
                            id:male
                            text:'男'
                            group:'gender'
                    GridLayout:
                        cols:4
                        DarkLabel:
                            text:'吸烟数量'
                        ToggleButton:
                            text:'不吸烟'
                            group:'smoking'
                            state:'down'
                        ToggleButton:
                            id:smoke_less
                            text:"0-20支"
                            group:'smoking'
                        ToggleButton:
                            id:smoke_more
                            text:'>20支'
                            group:'smoking'
                    GridLayout:
                        cols:4
                        DarkLabel:
                            text:'饮酒数量'
                        ToggleButton:
                            text:'不饮酒'
                            group:'drinking'
                        ToggleButton:
                            id:drink_less
                            text:"0-25克"
                            group:'drinking'
                            state:'down'
                        ToggleButton:
                            id:drink_more
                            text:'>25克'
                            group:'drinking'
                    GridLayout:
                        cols:3
                        DarkLabel:
                            text:'锻炼'
                        ToggleButton:
                            id:exercise
                            text:'是'
                            state:'down'
                            group:'exercise'
                        ToggleButton:
                            text:'否'
                            group:"exercise"
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:'心率'+str(heart_rate.value)
                        Slider:
                            id:heart_rate
                            min:40
                            max:160
                            step:1
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:"收缩压"+str(sbp.value)
                        Slider:
                            id:sbp
                            min:60
                            max:240
                            step:1
                    GridLayout:
                        cols:5
                        DarkLabel:
                            text:"腰围/身高比"
                        ToggleButton:
                            text:'<0.4'
                            group:'whtr'
                            state:'down'
                        ToggleButton:
                            id:whtr_small
                            text:'0.4-0.5'
                            group:'whtr'
                        ToggleButton:
                            id:whtr_medium
                            text:'0.5-0.6'
                            group:'whtr'
                        ToggleButton:
                            id:whtr_large
                            text:'>0.6'
                            group:'whtr'
                    GridLayout:
                        cols:3
                        DarkLabel:
                            text:'脂肪肝史'
                        ToggleButton:
                            text:'否'
                            group:'fatty_liver'
                            state:'down'
                        ToggleButton:
                            id:fatty_liver
                            text:'是'
                            group:'fatty_liver'
                    GridLayout:
                        cols:3
                        DarkLabel:
                            text:'胆囊疾病史'
                        ToggleButton:
                            text:'否'
                            group:'gallbladder_disease'
                            state:'down'
                        ToggleButton:
                            id:gallbladder_disease
                            text:'是'
                            group:'gallbladder_disease'
                    AButton:
                        text:'计算'
                        on_state: root.on_press_prob()
                        pos_hint:{'center_x':.5,'center_y':.5}
                        size_hint:(0.9,0.9)              
                    Label:
                        id:prob_label
                        text:" "
                        color:(0.4,0.4,0.6,1)
                    GridLayout:
                        cols:4
                        spacing: '10dp'         
                        AButton:
                            text:'模型信息表'
                            on_release:root.info_sheet()
                            pos_hint:{'center_x':.5,'center_y':.5} 
                        AButton:
                            text:'评价星级:4星'
                            on_release:root.conclusion()
                            pos_hint:{'center_x':.5,'center_y':.5}             
            TabbedPanelItem:
                text:"ID33303841"
                font_name:"Droid"
                # border:'off'
                GridLayout:
                    cols:1
                    padding:'10dp'
                    spacing:'10dp' 
                    canvas.before:
                        Color:
                            rgb:0.8,0.8,1
                        Rectangle:
                            pos:self.pos
                            size:self.size 
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:"年龄"+str(age2.value)
                        Slider:
                            id:age2
                            min:20
                            max:100
                            step:1
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:"BMI"+str(bmi2.value)
                        Slider:
                            id:bmi2
                            min:14
                            max:44
                            step:1
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:"收缩压"+str(sbp2.value)
                        Slider:
                            id:sbp2 
                            min:70
                            max:210
                            step:1
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:"空腹血糖"+str(fpg2.value)
                        Slider:
                            id:fpg2
                            min:2.5
                            max:7
                            step:0.1
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:'甘油三酯'+str(tg2.value)
                        Slider:
                            id:tg2
                            min:0
                            max:35
                            step:1
                    AButton:
                        text:'计算'
                        on_state: root.on_press_prob2()
                        pos_hint:{'center_x':.5,'center_y':.5}
                        size_hint:(0.9,0.9)              
                    Label:
                        id:prob_label2
                        text:" "
                        color:(0.4,0.4,0.6,1)
                    GridLayout:
                        cols:4
                        spacing: '10dp'         
                        AButton:
                            text:'模型信息表'
                            on_release:root.info_sheet2()
                            pos_hint:{'center_x':.5,'center_y':.5} 
                        AButton:
                            text:'评价星级:3星'
                            on_release:root.conclusion2()
                            pos_hint:{'center_x':.5,'center_y':.5} 
<screen5>:
    name:'screen5'
    GridLayout:
        cols:1
        # orientation:'vertical'
        ActionBar:
            ActionView:
                ActionPrevious:
                    title:'冠心病'
                    font_name:"Droid"
                    markup:True
                    with_previous:True
                    app_icon:'logo.png'
                    on_press:root.manager.current="menu"              
        TabbedPanel:
            do_default_tab:False
            canvas.before:
                Color:
                    rgb:0.4,0.4,0.6
                Rectangle:
                    pos:self.pos
                    size:self.size
            TabbedPanelItem:
                text:'ID32350208'
                font_name:"Droid"
                border:'off'
                GridLayout:
                    cols:1
                    padding:'10dp'
                    spacing:'10dp' 
                    canvas.before:
                        Color:
                            rgb:0.8,0.8,1
                        Rectangle:
                            pos:self.pos
                            size:self.size 
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:"年龄"+str(age.value)
                        Slider:
                            id:age
                            min:39
                            max:77
                            step:1
                    GridLayout:
                        cols:3
                        DarkLabel:
                            text:"性别"
                        ToggleButton:
                            id:female
                            text:'女'
                            group:'sex'
                            state:'down'
                        ToggleButton:
                            id:male
                            text:'男'
                            group:'sex'
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:"血清肌酐"+str(scr.value)
                        Slider:
                            id:scr
                            min:46
                            max:119
                            step:1    
                    GridLayout:
                        cols:3
                        DarkLabel:
                            text:'糖尿病'
                        ToggleButton:
                            text:'否'
                            group:'diabetes'
                            state:'down'
                        ToggleButton:
                            id:diabetes
                            text:'是'
                            group:'diabetes'
                    GridLayout:
                        cols:3
                        DarkLabel:
                            text:'高血压'
                        ToggleButton:
                            text:'否'
                            group:'hypertension'
                            state:'down'
                        ToggleButton:
                            id:hypertension
                            text:'是'
                            group:'hypertension'
                    GridLayout:
                        cols:3
                        DarkLabel:
                            text:'心绞痛'
                        ToggleButton:
                            text:'非典型'
                            group:'angina'
                            state:'down'
                        ToggleButton:
                            id:angina
                            text:'典型'
                            group:'angina'
                    GridLayout:
                        cols:3
                        DarkLabel:
                            text:'吸烟'
                        ToggleButton:
                            text:'否'
                            group:'smoke'
                            state:'down'
                        ToggleButton:
                            id:smoke
                            text:'是'
                            group:'smoke'
                    GridLayout:
                        cols:2
                        DarkLabel:
                            text:'低密度脂蛋白'+str(ldl.value)
                        Slider:
                            id:ldl
                            min:2.4
                            max:4.0
                            step:0.1
                    AButton:
                        text:'计算'
                        on_state: root.on_press_prob()
                        pos_hint:{'center_x':.5,'center_y':.5}
                        size_hint:(0.9,0.9)              
                    Label:
                        id:prob_label
                        text:" "
                        color:(0.4,0.4,0.6,1)
                    GridLayout:
                        cols:2
                        spacing:'10dp'         
                        AButton:
                            text:'模型信息表'
                            on_release:root.info_sheet()
                            pos_hint:{'center_x':.5,'center_y':.5} 
                        AButton:
                            text:'评价星级:2星'
                            on_release:root.conclusion()
                            pos_hint:{'center_x':.5,'center_y':.5} 


<AButton@Button>:    
    font_name:"Droid"
    background_normal:""
    background_color: 0,0.6,1,1
<Label@Label>:
    font_name:"Droid"
<DarkLabel@Label>:
    font_name:"Droid"
    color:(0.4,0.4,0.6,1)
    size_hint_x: None
    width:220
    text_size:self.width, None
<ActionBar@ActionBar>:
    canvas:
        Color:
            rgb:0.4,0.4,0.6
        Rectangle:
            pos:self.pos
            size:self.size
<ToggleButton@ToggleButton>:
    font_name:"Droid"
<Slider@Slider>:
    value_track:True
    value_track_color:[1,0,0,1]

""")

class MenuScreen(Screen):

    txt='''
    [anchor=title]本APP选择/评价临床预测模型的原则
    [anchor=content]首先，临床预测模型的优劣一般是通过区分度和校准度两方面来进行评价。区分度最主要的参数是C统计量（逻辑回归模型）和C指数（Cox模型），其通俗理解是我们所构建的模型是否可以找出一个点将发生事件和未发生事件的人群区分开来；校准度一般是通过校准度曲线来直观评价，观察实际曲线与理想曲线的贴合程度，贴合表示校准度优良，不贴合表示高估或者低估实际概率，另外，其斜率可以作为校准度的参数指标。校准度的通俗理解是所构建的模型预测的概率与实际概率的符合程度。 
    [anchor=content]其次，临床预测模的另一个要求有一定的外推性，但是要求一个临床预测模型可以全世界通用是不现实的。构建模型的患者人群与模型应用人群之间的相似程度决定了一个模型预测表现的好和坏，所以，国内人群构建的模型在国内人群应用时会最有可能表现出最佳的性能，某地区人群构建的模型在本地区应用时最有可能表现出最佳的性能，而对于国外人群构建的模型则要通过外部验证（采用本地人群进行）来确定其效能。
    [anchor=content]再次，模型构建所用到的样本量是影响模型稳定性的一个重要参数。样本量越大代表模型学习了更多的临床情况，在应用到新的情景中时，模型更有可能做出准确的预测。
    [anchor=content]所以,本APP优先选择纳入国内患者数据构建的、样本量较大的、模型评分较高的临床预测模型。
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

    def info_sheet(self):
        self.the_info_sheet = Popup(title='模型信息表',
                                       content=Image(source='PMID31865340.png')
                                       )
        self.the_info_sheet.open()

    def conclusion(self):
        txt='''
            模型预测的效能优；
            模型预测变量多，适用性窄；
            样本量偏少；
            文中所指的外部验证，实为内部验证；
            有一定的应用价值。
            '''
        self.the_conclusion = Popup(title="Brief Comment", 
                                      content=Label(text=txt, 
                                      line_height=1.2,
                                      font_size=16
                                      ))
        self.the_conclusion.open()

class screen2(Screen):
    def on_press_prob(self,*args):
        age=self.ids['age'].value
        course=self.ids['course'].value
        sbp=self.ids['sbp'].value
        dbp=self.ids['dbp'].value
        bmi=self.ids['bmi'].value
        hba1c=self.ids['HbA1c'].value
        tg=self.ids['tg'].value
        ldl=self.ids['ldl'].value
        hdl=self.ids['hdl'].value
        ua=self.ids['ua'].value
        egfr=self.ids['egfr'].value
        
        ls_or=[1.065,1.045,1.038,1.028,1.183,1.310,1.119,4.518,0.083,1.004,1.004]
        ls_xvar=[age,course,sbp,dbp,bmi,hba1c,tg,ldl,hdl,ua,egfr]
        ls_xvar_ex=[68,2,151,83,22.84,6.5,2.42,1.04,1.77,362,85.89]
        prob_ex=0.317
        intercept=ev.logistic.intercept(ls_or=ls_or,ls_xvar=ls_xvar_ex,prob=prob_ex)
        model=ev.logistic(ls_or=ls_or,ls_xvar=ls_xvar,intercept=intercept)
        prob=model.prob()
        
        label=self.ids['prob_label']
        label.text='该患者发生脑卒中的概率为:'+str(round(prob,2)*100)+"%"
    def info_sheet(self):
        self.the_info_sheet=Popup(title='Infomation Sheet',
                                    content=Image(source='PMID32982965.png'))
        self.the_info_sheet.open()
    def conclusion(self):
        txt='''
            预测指标较多，但是易得；
            模型效能参数达到要求；
            样本量达到要求。
            '''
        
        self.the_conclusion=Popup(title="Brief Comment",
                            content=Label(text=txt, 
                             markup=True,
                             line_height=1.2,
                             font_size=16
                             ))
        self.the_conclusion.open()
class screen3(Screen):
    def on_press_prob(self,*args):
        age=self.ids['age'].value
        bmi=self.ids['bmi'].value
        hba1c=self.ids['hba1c'].value
        tg=self.ids['tg'].value
        ls_or=[1.073334331,1.127451753,5.373879032,1.729565118]
        ls_xvar=[age,bmi,hba1c,tg]
        intercept=-15.53294
        model=ev.logistic(ls_or=ls_or,ls_xvar=ls_xvar,intercept=intercept)
        prob=model.prob()
        label=self.ids['prob_label']
        label.text='该患者发生妊娠糖尿病的概率为:'+str(round(prob,2)*100)+"%"
    def info_sheet(self):
        self.the_info_sheet=Popup(title='Information Sheet',
                                    content=Image(source='PMID33277541.png'))
        self.the_info_sheet.open()
    def conclusion(self):
        txt='''
            预测指标少，适用性好；
            模型效能参数达到要求,偏低；
            样本量达到要求。
            '''
        
        self.the_conclusion=Popup(title="Brief Comment",
                            content=Label(text=txt, 
                             markup=True,
                             line_height=1.2,
                             font_size=16
                             ))
        self.the_conclusion.open()
class screen4(Screen):

    def on_press_prob(self,*args):
        age=self.ids['age'].value
        heart_rate=self.ids['heart_rate'].value
        sbp=self.ids['sbp'].value
        if self.ids['female'].state=='down':
            gender=1
        else:
            gender=0
        if self.ids['exercise'].state=='down':
            exercise=1
        else:
            exercise=0
        if self.ids['drink_less'].state=='down':
            drink_less=1
        else:
            drink_less=0
        if self.ids['drink_more'].state=='down':
            drink_more=1
        else:
            drink_more=0
        if self.ids['smoke_less'].state=='down':
            smoke_less=1
        else:
            smoke_less=0
        if self.ids['smoke_more'].state=='down':
            smoke_more=1
        else:
            smoke_more=0
        if self.ids['whtr_small'].state=='down':
            whtr_small=1
        else:
            whtr_small=0
        if self.ids['whtr_medium'].state=='down':
            whtr_medium=1
        else:
            whtr_medium=0
        if self.ids['whtr_large'].state=='down':
            whtr_large=1
        else:
            whtr_large=0
        if self.ids['fatty_liver'].state=='down':
            fatty_liver=1
        else:
            fatty_liver=0
        if self.ids['gallbladder_disease'].state=='down':
            gallbladder_disease=1
        else:
            gallbladder_disease=0
        ls_or=[1.049,1.013,1.017,0.745,0.705,0.772,1.627,1.474,3.336,1.626,2.901,3.087,1.218]
        ls_xvar=[age,heart_rate,sbp,gender,exercise,drink_less,drink_more,smoke_less,smoke_more,whtr_small,whtr_medium,whtr_large,fatty_liver,gallbladder_disease]
        ls_xvar_ex=[60,90,100,0,0,0,1,1,0,0,1,0,0,1]
        intercept=ev.logistic.intercept(ls_or=ls_or,ls_xvar=ls_xvar_ex,prob=0.5)
        model=ev.logistic(ls_or=ls_or,ls_xvar=ls_xvar,intercept=intercept)
        prob=model.prob()
        label=self.ids['prob_label']
        label.text="该患者患糖尿病的概率为:"+str(round(prob,2)*100)+"%"

    def info_sheet(self):
        self.the_info_sheet=Popup(title='Infomation Sheet',
                                content=Image(source='PMID32665620.png'))
        self.the_info_sheet.open()
    def conclusion(self):
        txt='''
        样本量大;
        模型效能达到要求;
        预测变量数量多,易用性差。
        '''
        self.the_conclusion=Popup(title='Brief Comment',
                                content=Label(text=txt,
                                font_size=16,
                                line_height=1.2
                                ))
        self.the_conclusion.open()
    def on_press_prob2(self,*args):
        age2=self.ids['age2'].value
        bmi2=self.ids['bmi2'].value
        sbp2=self.ids['sbp2'].value
        fpg2=self.ids['fpg2'].value
        tg2=self.ids['tg2'].value
        ls_or2=[1.032765339,1.112322309,1.013976774,9.472662323,1.099043219]
        ls_xvar2=[age2,bmi2,sbp2,fpg2,tg2]
        intercept2=-23.14183
        model2=ev.logistic(ls_xvar=ls_xvar2,ls_or=ls_or2,intercept=intercept2)
        prob2=model2.prob()
        label2=self.ids['prob_label2']
        label2.text='该患者三年内患糖尿病的概率为:'+str(round(prob2,2)*100)+'%'
    def info_sheet2(self):
        self.the_info_sheet=Popup(title='Infomation Sheet',
                                content=Image(source='PMID33303841.png'))
        self.the_info_sheet.open()
    def conclusion2(self):
        txt='''
        样本量达到要求;
        模型效能达到要求;
        预测变量数量适中,易用性好。
        '''
        self.the_conclusion=Popup(title='Brief Comment',
                                    content=Label(text=txt,
                                    font_size=16,
                                    line_height=1.2
                                    ))
        self.the_conclusion.open()
class screen5(Screen):
    
    def on_press_prob(self,*args):
        age=self.ids['age'].value
        if self.ids['male'].state=='down':
            sex=1
        else:
            sex=0
        scr=self.ids['scr'].value
        if self.ids['smoke'].state=='down':
            smoke=1
        else:
            smoke=0
        if self.ids['angina'].state=='down':
            angina=1
        else:
            angina=0
        if self.ids['diabetes'].state=='down':
            diabetes=1
        else:
            diabetes=0
        ldl=self.ids['ldl'].value
        if self.ids['hypertension'].state=='down':
            hypertension=1
        else:
            hypertension=0
        
        ls_or=[1.0564,1.96274,1.007,1.6126,1.7360,2.3728,1.3036,1.5941]
        ls_xvar=[age,sex,scr,smoke,angina, diabetes,ldl, hypertension]
        intercept=-5.2782
        model=ev.logistic(ls_or=ls_or,ls_xvar=ls_xvar,intercept=intercept)
        prob=model.prob()
        label=self.ids['prob_label']
        label.text='该患者患冠心病的概率为:'+str(round(prob,2)*100)+'%'
    def info_sheet(self):
        self.the_info_sheet=Popup(title='Infomation Sheet',
                                    content=Image(source='PMID32350208.png'))
        self.the_info_sheet.open()
    def conclusion(self):
        self.txt='''
        样本量达到要求;
        模型效能一般,有高估;
        预测变量数量多,易用性一般;
        仅供学术研究。
        '''
        self.the_conclusion=Popup(title='Brief Comment',
                                content=Label(text=self.txt,
                                font_size=16,
                                line_height=1.2
                                ))
        self.the_conclusion.open()

class MPDApp(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(screen1(name='screen1'))
        sm.add_widget(screen2(name='screen2'))
        sm.add_widget(screen3(name='screen3'))
        sm.add_widget(screen4(name='screen4'))
        sm.add_widget(screen5(name='screen5'))
        return sm
MPDApp().run()
