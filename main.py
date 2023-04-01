import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import numpy as np
import pandas as pd
import compute as fn
global result
global path
def savecsv(case):
    dg=pd.DataFrame(result)
    dg.to_csv(path,header=False,index=False)


def on_button_clicked(case):
    global result
    global path
    path=builder.get_object("filechoose").get_filename()
    if(path==None):
        
        for i in range(0,9):
            for j in range(0,9):
                x="n"+str(i+1)+str(j+1)
                
                tx=builder.get_object(x)
                if(tx.get_property("text")==""):
                    num=0
                else:
                    num=tx.get_property("text")
                mat2d[i][j]=int(num)
    else:
        
        mat2d=np.array(pd.DataFrame(pd.read_csv(path, header=None)).fillna(0))
        mat2d=[[int(x) for x in col] for col in mat2d]
  
    result=fn.solve(mat2d)
    
    
    for i in range(0,9):
        for j in range(0,9):
            x="n"+str(i+1)+str(j+1)
            builder.get_object(x).set_property("text",str(result[i][j]))
    return result

builder = Gtk.Builder()
builder.add_from_file("gui.glade")
datagen= builder.get_object("generater")
save= builder.get_object("save")
builder.connect_signals({"on_button_clicked": on_button_clicked,"savecsv":savecsv})

window = builder.get_object("window")
window.set_title("Sudoku Sover")
window.set_position(Gtk.WindowPosition.CENTER)
window.set_icon_from_file("spic.png")
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()