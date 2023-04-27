""" This GUI program ia multiplayer xox game """
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GdkPixbuf,GLib
import base64
image_data = "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"

# Add padding characters until the length is a multiple of 4
while len(image_data) % 4 != 0:
    image_data += "="

# Decode the Base64 string
decoded_data = base64.b64decode(image_data)


# Using image loader
loader = GdkPixbuf.PixbufLoader.new()
loader.write(decoded_data)
loader.close()
pixbuf = loader.get_pixbuf()

xml="""<?xml version="1.0" encoding="UTF-8"?>
<!-- Generated with glade 3.38.2 -->
<interface>
  <requires lib="gtk+" version="3.24"/>
  <object class="GtkWindow" id="window">
    <property name="can-focus">False</property>
    <property name="resizable">False</property>
    <property name="default-width">260</property>
    <property name="default-height">400</property>
    <child>
      <object class="GtkFixed">
        <property name="visible">True</property>
        <property name="can-focus">False</property>
        <child>
          <object class="GtkButton" id="b12">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <property name="use-underline">True</property>
            <signal name="clicked" handler="b12" swapped="no"/>
          </object>
          <packing>
            <property name="x">100</property>
            <property name="y">20</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="b13">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="b13" swapped="no"/>
          </object>
          <packing>
            <property name="x">180</property>
            <property name="y">20</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="b11">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="b11" swapped="no"/>
          </object>
          <packing>
            <property name="x">20</property>
            <property name="y">20</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="b21">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="b21" swapped="no"/>
          </object>
          <packing>
            <property name="x">20</property>
            <property name="y">100</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="b22">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="b22" swapped="no"/>
          </object>
          <packing>
            <property name="x">100</property>
            <property name="y">100</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="b23">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="b23" swapped="no"/>
          </object>
          <packing>
            <property name="x">180</property>
            <property name="y">100</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="b31">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="b31" swapped="no"/>
          </object>
          <packing>
            <property name="x">20</property>
            <property name="y">180</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="b32">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="b32" swapped="no"/>
          </object>
          <packing>
            <property name="x">100</property>
            <property name="y">180</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="b33">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="b33" swapped="no"/>
          </object>
          <packing>
            <property name="x">180</property>
            <property name="y">180</property>
          </packing>
        </child>
        <child>
          <object class="GtkSwitch" id="slider">
            <property name="width-request">100</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
          </object>
          <packing>
            <property name="x">77</property>
            <property name="y">257</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel">
            <property name="width-request">200</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <property name="label" translatable="yes">O            X</property>
            <attributes>
              <attribute name="weight" value="normal"/>
              <attribute name="scale" value="3"/>
            </attributes>
          </object>
          <packing>
            <property name="x">28</property>
            <property name="y">247</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel" id="status">
            <property name="width-request">100</property>
            <property name="height-request">35</property>
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <attributes>
              <attribute name="weight" value="bold"/>
              <attribute name="foreground" value="#08a6ffff0000"/>
            </attributes>
          </object>
          <packing>
            <property name="x">80</property>
            <property name="y">325</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="reset">
            <property name="label" translatable="yes">Reset</property>
            <property name="width-request">50</property>
            <property name="height-request">34</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="reset" swapped="no"/>
          </object>
          <packing>
            <property name="x">160</property>
            <property name="y">360</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="start">
            <property name="label" translatable="yes">start</property>
            <property name="width-request">50</property>
            <property name="height-request">34</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="start" swapped="no"/>
          </object>
          <packing>
            <property name="x">30</property>
            <property name="y">360</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel" id="timer">
            <property name="width-request">50</property>
            <property name="height-request">35</property>
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <property name="label" translatable="yes">0:00</property>
          </object>
          <packing>
            <property name="x">37</property>
            <property name="y">325</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
</interface>
"""
global result
global timetra
timetra=int(0)

result=False
def fnstart(case):
    global timetra
    global result
    timer = builder.get_object("timer")
    stop_flag = False
    if result:
    	resetfn(0)
    
    def update():
        global timetra
        nonlocal stop_flag
        timer_value = timetra
        timer_value += 1
        
            
        minute=int(timer_value/60)
        sec=int(timer_value%60)
        timeminsec=str(minute)+":"+str(sec)
        timer.set_label(timeminsec)
        timetra=timer_value
        if stop_flag:
            return False  # Stop the timer
        else:
            return True   # Continue the timer

    def start_stop_button_clicked(button):
        nonlocal stop_flag
        if button.get_label() == "start":
            button.set_label("stop")
            stop_flag = False
            button.timer_id = GLib.timeout_add(1000, update)
        else:
            button.set_label("start")
            stop_flag = True
            GLib.source_remove(button.timer_id)
            button.timer_id = None
    start_stop_button_clicked(builder.get_object("start"))


    

def resetfn(case):
    global timetra
    global result
    builder.get_object("timer").set_property("label","0:00")
    timetra=int(0)
    builder.get_object("status").set_property("label",None)
    result= False
    for i in range(0,3):
        for j in range(0,3):
            x="b"+str(i+1)+str(j+1)
            obj=builder.get_object(x)
            obj.set_property("label","")

def on_button_clicked(widget, button_id):
    global result
    if result==True or builder.get_object("start").get_label()=="start":
        
        return 0
    slider=builder.get_object("slider")
    button = builder.get_object(button_id)
    cell=button.get_property("label")
    
    
    
    if slider.get_active():
        
        
        if cell==None or cell=="":
            button.set_property("label", "X")
            

    elif slider.get_active()==False:
        if cell==None or cell=="":
            button.set_property("label", "O")
            
    mat2d=[["" for _ in range(0,3)] for _ in range(0,3)]
    for i in range(0,3):
        for j in range(0,3):
            x="b"+str(i+1)+str(j+1)
            obj=builder.get_object(x)
            value=obj.get_property("label")
            
            if obj.get_property("label")==None or obj.get_property("label")=="":
                mat2d[i][j]="nan"
            else:
                mat2d[i][j]=obj.get_property("label")
    result,winner=check(mat2d)
    if result:
        if winner=="O" or winner=="X":
            builder.get_object("status").set_property("label",winner+" won")
        else:
            builder.get_object("status").set_property("label",winner)
    else:
        if slider.get_active():
            slider.set_active(False)
        else:
            slider.set_active(True)

def check(mat2d):
    result=False
    winner=""
    

    #rowwise
    for i in range(0,3):
        if all(x == mat2d[i][0] for x in mat2d[i]):
            if mat2d[i][0]!="nan":
                result=True
                winner=mat2d[i][0]
                break
        
    #coumnwise
    for i in range(0,3):
        if mat2d[0][i]==mat2d[1][i]:
            if mat2d[1][i]==mat2d[2][i]:
                if mat2d[0][i]!="nan":
                    result=True
                    winner=mat2d[0][i]
                    break

    #diagonal
    if mat2d[0][0]==mat2d[2][2]:
        if mat2d[2][2]==mat2d[1][1]:
            if mat2d[0][0]!="nan":
                result=True
                winner=mat2d[0][0]
            
    if mat2d[0][2]==mat2d[1][1]:
        if mat2d[1][1]==mat2d[2][0]:
            if mat2d[0][2]!="nan":
                result=True
                winner=mat2d[0][2]
    #check for draw
    if result==False:
        for i in range (0,3):
            for j in range(0,3):
                if mat2d[i][j]!="nan":
                    result=True
                    winner="Draw !"
                else:
                    result=False
                    winner=""
                    break
            if result==False:
                break

    if result==True:
            builder.get_object("start").set_property("label","stop")
            global timetra
            
            fnstart(0)
            timetra=0

    return result,winner

builder = Gtk.Builder()
builder.add_from_string(xml)
b11= builder.get_object("b11")
b12= builder.get_object("b12")
b13= builder.get_object("b13")
b21= builder.get_object("b21")
b22= builder.get_object("b22")
b23= builder.get_object("b23")
b31= builder.get_object("b31")
b32= builder.get_object("b32")
b33= builder.get_object("b33")
reset=builder.get_object("reset")
start=builder.get_object("start")
builder.connect_signals({"b11": lambda widget: on_button_clicked(widget, "b11"),
"b12": lambda widget: on_button_clicked(widget, "b12"),
"b13": lambda widget: on_button_clicked(widget, "b13"),
"b21": lambda widget: on_button_clicked(widget, "b21"),
"b22": lambda widget: on_button_clicked(widget, "b22"),
"b23": lambda widget: on_button_clicked(widget, "b23"),
"b31": lambda widget: on_button_clicked(widget, "b31"),
"b32": lambda widget: on_button_clicked(widget, "b32"),
"b33": lambda widget: on_button_clicked(widget, "b33"),"reset":resetfn,"start":fnstart})


window = builder.get_object("window")
window.set_title("XOX Game")
window.set_position(Gtk.WindowPosition.CENTER)
window.set_icon(pixbuf)
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
