import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sorter
import compute
import copy
global datalis
global operands

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
builder.add_from_file("gui.glade")

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
window.set_icon_from_file("spic.png")
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()