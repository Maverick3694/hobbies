import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GLib
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
builder.add_from_file("gui.glade")
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
window.set_icon_from_file("spic.png")
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
