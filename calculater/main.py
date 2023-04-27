import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk ,GdkPixbuf, GLib
import base64
import sorter
import compute
import copy
global datalis
global operands
image_data = "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"
# Add padding characters until the length is a multiple of 4
while len(image_data) % 4 != 0:
    image_data += "="

# Decode the Base64 string
decoded_data = base64.b64decode(image_data)

# load decoded data for icon file input
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
    <property name="default-width">370</property>
    <property name="default-height">640</property>
    <child>
      <object class="GtkFixed">
        <property name="visible">True</property>
        <property name="can-focus">False</property>
        <child>
          <object class="GtkButton" id="b7">
            <property name="label" translatable="yes">7</property>
            <property name="width-request">80</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="b7" swapped="no"/>
          </object>
          <packing>
            <property name="x">10</property>
            <property name="y">280</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="b4">
            <property name="label" translatable="yes">4</property>
            <property name="width-request">80</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="b4" swapped="no"/>
          </object>
          <packing>
            <property name="x">10</property>
            <property name="y">370</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="b1">
            <property name="label" translatable="yes">1</property>
            <property name="width-request">80</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="b1" swapped="no"/>
          </object>
          <packing>
            <property name="x">10</property>
            <property name="y">460</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="b8">
            <property name="label" translatable="yes">8</property>
            <property name="width-request">80</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="b8" swapped="no"/>
          </object>
          <packing>
            <property name="x">100</property>
            <property name="y">280</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="b9">
            <property name="label" translatable="yes">9</property>
            <property name="width-request">80</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="b9" swapped="no"/>
          </object>
          <packing>
            <property name="x">190</property>
            <property name="y">280</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="b5">
            <property name="label" translatable="yes">5</property>
            <property name="width-request">80</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="b5" swapped="no"/>
          </object>
          <packing>
            <property name="x">100</property>
            <property name="y">370</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="b2">
            <property name="label" translatable="yes">2</property>
            <property name="width-request">80</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="b2" swapped="no"/>
          </object>
          <packing>
            <property name="x">100</property>
            <property name="y">460</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="b6">
            <property name="label" translatable="yes">6</property>
            <property name="width-request">80</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="b6" swapped="no"/>
          </object>
          <packing>
            <property name="x">190</property>
            <property name="y">370</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="b3">
            <property name="label" translatable="yes">3</property>
            <property name="width-request">80</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="b3" swapped="no"/>
          </object>
          <packing>
            <property name="x">190</property>
            <property name="y">460</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="b0">
            <property name="label" translatable="yes">0</property>
            <property name="width-request">170</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="b0" swapped="no"/>
          </object>
          <packing>
            <property name="x">10</property>
            <property name="y">550</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="point">
            <property name="label" translatable="yes">.</property>
            <property name="width-request">80</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="point" swapped="no"/>
          </object>
          <packing>
            <property name="x">190</property>
            <property name="y">550</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="plus">
            <property name="label" translatable="yes">+</property>
            <property name="width-request">80</property>
            <property name="height-request">170</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="plus" swapped="no"/>
          </object>
          <packing>
            <property name="x">280</property>
            <property name="y">280</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="enter">
            <property name="label" translatable="yes">enter</property>
            <property name="width-request">80</property>
            <property name="height-request">170</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="calculate" swapped="no"/>
          </object>
          <packing>
            <property name="x">280</property>
            <property name="y">460</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="back">
            <property name="label" translatable="yes">←</property>
            <property name="width-request">80</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="back" swapped="no"/>
          </object>
          <packing>
            <property name="x">10</property>
            <property name="y">192</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="divide">
            <property name="label" translatable="yes">/</property>
            <property name="width-request">80</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="divide" swapped="no"/>
          </object>
          <packing>
            <property name="x">100</property>
            <property name="y">192</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="multiply">
            <property name="label" translatable="yes">*</property>
            <property name="width-request">80</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="multiply" swapped="no"/>
          </object>
          <packing>
            <property name="x">190</property>
            <property name="y">192</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="minus">
            <property name="label" translatable="yes">-</property>
            <property name="width-request">80</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="minus" swapped="no"/>
          </object>
          <packing>
            <property name="x">280</property>
            <property name="y">192</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="display">
            <property name="width-request">350</property>
            <property name="height-request">75</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="max-length">40</property>
            <property name="input-purpose">number</property>
          </object>
          <packing>
            <property name="x">10</property>
            <property name="y">10</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="delete">
            <property name="label" translatable="yes">Del</property>
            <property name="width-request">80</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="delete" swapped="no"/>
          </object>
          <packing>
            <property name="x">280</property>
            <property name="y">100</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="leftpara">
            <property name="label" translatable="yes">(</property>
            <property name="width-request">80</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="leftpara" swapped="no"/>
          </object>
          <packing>
            <property name="x">10</property>
            <property name="y">100</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="rightpara">
            <property name="label" translatable="yes">)</property>
            <property name="width-request">80</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="rightpara" swapped="no"/>
          </object>
          <packing>
            <property name="x">100</property>
            <property name="y">100</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="sqrt">
            <property name="label" translatable="yes">√</property>
            <property name="name">80</property>
            <property name="width-request">80</property>
            <property name="height-request">80</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="sqrt" swapped="no"/>
          </object>
          <packing>
            <property name="x">190</property>
            <property name="y">100</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
</interface>"""
operands=["+","*","-","/"]
datalis=[]


def Calculate(case):
    global datalis
    global operands
    dp=builder.get_object("display").get_property("text")
    if len(datalis)==0 or dp=="" or dp==None:
        return 0
    if dp!="" or dp!=None:
        datalis.clear()
        for i in range(0,len(dp)):
            datalis.append(dp[i])

    datalis=copy.deepcopy(sorter.fn(datalis))
    
    r=check()
    if r:
        builder.get_object("display").set_property("text", "Error")
        datalis.clear()
        return 0
    result=compute.fn(datalis,operands)
    builder.get_object("display").set_property("text", str(result))
    datalis.clear()


    
    
def check():
    global datalis
    global operands



    r=0
    if datalis[0] in operands or datalis[-1] in operands:
        
        return 1
    
    for i in range(0,len(datalis)):
        if i!=0:
            if datalis[i] in operands:
                if datalis[i-1] in operands:
                    r=1
                    break
    if r:
        
        return 1
    cl=0
    cr=0
    for i in range(0,len(datalis)):
        if datalis[i]=="√":
            if i+1==len(datalis):
                r=1
                break
            if datalis[i+1] in operands:
                r=1
                break
            if datalis[i+1]=="√" or datalis[i+1]==")":
                r=1
                break
        if datalis[i]=="(":
            cl=cl+1
        if datalis[i]==")":
            cr=cr+1
    if cl!=cr:
        r=1
    if r:
        
        return 1
    if datalis[0]==")" or datalis[-1]=="(":
        
        return 1
    
    











def on_button_clicked(widget, button_id):
    global datalis
    if button_id!="back":
        inp=builder.get_object(button_id).get_property("label")
        datalis.append(inp)
        builder.get_object("display").set_property("text", ''.join(datalis))
    if button_id=="back":
        del datalis[-1]
        builder.get_object("display").set_property("text", ''.join(datalis))
    if button_id=="delete":
        datalis.clear()
        builder.get_object("display").set_property("text", "")







builder = Gtk.Builder()
builder.add_from_string(xml)

b1= builder.get_object("b1")
b2= builder.get_object("b2")
b3= builder.get_object("b3")
b4= builder.get_object("b4")
b5= builder.get_object("b5")
b6= builder.get_object("b6")
b7= builder.get_object("b7")
b8= builder.get_object("b8")
b9= builder.get_object("b9")
b0=builder.get_object("b0")
plus=builder.get_object("plus")
minus=builder.get_object("minus")
multipply=builder.get_object("multiply")
divide=builder.get_object("divide")
back=builder.get_object("back")
enter=builder.get_object("enter")
delete=builder.get_object("delete")
enter=builder.get_object("enter")
builder.connect_signals({
"b1": lambda widget: on_button_clicked(widget, "b1"),
"b2": lambda widget: on_button_clicked(widget, "b2"),
"b3": lambda widget: on_button_clicked(widget, "b3"),
"b4": lambda widget: on_button_clicked(widget, "b4"),
"b5": lambda widget: on_button_clicked(widget, "b5"),
"b6": lambda widget: on_button_clicked(widget, "b6"),
"b7": lambda widget: on_button_clicked(widget, "b7"),
"b8": lambda widget: on_button_clicked(widget, "b8"),
"b9": lambda widget: on_button_clicked(widget, "b9"),
"b0": lambda widget: on_button_clicked(widget, "b0"),
"plus": lambda widget: on_button_clicked(widget, "plus"),
"minus": lambda widget: on_button_clicked(widget, "minus"),
"multiply": lambda widget: on_button_clicked(widget, "multiply"),
"divide": lambda widget: on_button_clicked(widget, "divide"),
"back": lambda widget: on_button_clicked(widget, "back"),
"point": lambda widget: on_button_clicked(widget, "point"),
"delete": lambda widget: on_button_clicked(widget, "delete"),
"sqrt": lambda widget: on_button_clicked(widget, "sqrt"),
"leftpara": lambda widget: on_button_clicked(widget, "leftpara"),
"rightpara": lambda widget: on_button_clicked(widget, "rightpara"),
"delete": lambda widget: on_button_clicked(widget, "delete"),"calculate":Calculate
})


window = builder.get_object("window")
window.set_title("Calculater")
window.set_position(Gtk.WindowPosition.CENTER)
window.set_icon(pixbuf)
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()