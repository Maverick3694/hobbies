import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, GLib
import base64


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
  <object class="GtkWindow" id="my_window">
    <property name="can-focus">False</property>
    <property name="default-width">500</property>
    <property name="default-height">300</property>
    <child>
      <object class="GtkFixed">
        <property name="visible">True</property>
        <property name="can-focus">False</property>
        <child>
          <object class="GtkEntry" id="base642">
            <property name="width-request">100</property>
            <property name="height-request">50</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="placeholder-text" translatable="yes">Base64 Data</property>
          </object>
          <packing>
            <property name="x">20</property>
            <property name="y">180</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="base641">
            <property name="width-request">100</property>
            <property name="height-request">50</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="placeholder-text" translatable="yes">Output Base64 Data</property>
          </object>
          <packing>
            <property name="x">302</property>
            <property name="y">60</property>
          </packing>
        </child>
        <child>
          <object class="GtkFileChooserButton" id="file">
            <property name="width-request">100</property>
            <property name="height-request">50</property>
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <property name="tooltip-text" translatable="yes">Select file</property>
            <property name="title" translatable="yes"/>
            <property name="width-chars">15</property>
          </object>
          <packing>
            <property name="x">20</property>
            <property name="y">60</property>
          </packing>
        </child>
        <child>
          <object class="GtkFileChooserButton" id="folder">
            <property name="width-request">80</property>
            <property name="height-request">50</property>
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <property name="tooltip-text" translatable="yes">Choose Folder</property>
            <property name="action">select-folder</property>
            <property name="title" translatable="yes"/>
          </object>
          <packing>
            <property name="x">300</property>
            <property name="y">180</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel">
            <property name="width-request">300</property>
            <property name="height-request">25</property>
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <property name="label" translatable="yes">File to Base64 encoding</property>
          </object>
          <packing>
            <property name="x">90</property>
            <property name="y">24</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel">
            <property name="width-request">300</property>
            <property name="height-request">25</property>
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <property name="label" translatable="yes">Base64 encoding to  File</property>
          </object>
          <packing>
            <property name="x">89</property>
            <property name="y">142</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="conv2">
            <property name="label" translatable="yes">→</property>
            <property name="width-request">50</property>
            <property name="height-request">34</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="btof" swapped="no"/>
          </object>
          <packing>
            <property name="x">216</property>
            <property name="y">192</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="conv1">
            <property name="label" translatable="yes">→</property>
            <property name="width-request">50</property>
            <property name="height-request">34</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="ftob" swapped="no"/>
          </object>
          <packing>
            <property name="x">216</property>
            <property name="y">69</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="fileext">
            <property name="name">fileext</property>
            <property name="width-request">50</property>
            <property name="height-request">20</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="placeholder-text" translatable="yes">Filename with extension</property>
          </object>
          <packing>
            <property name="x">300</property>
            <property name="y">240</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
</interface>
"""
def ftob(case):
    
    path=builder.get_object("file").get_filename()
    with open(path, "rb") as f:
    # read the contents of the file as bytes
        file_bytes = f.read()
    base64_bytes = base64.b64encode(file_bytes)
    base64_string = base64_bytes.decode('utf-8')
    builder.get_object("base641").set_property("text",base64_string)

def btof(case):
    data=builder.get_object("base642").get_property("text")
    while len(image_data) % 4 != 0:
        data += "="
    # Decode the Base64 string
    decoded_data = base64.b64decode(data)
    path=str(builder.get_object("folder").get_filename())
    path=path+"/"+str(builder.get_object("fileext").get_property("text"))
    with open(path, 'wb') as f_out:
        f_out.write(decoded_data)
builder = Gtk.Builder()
builder.add_from_string(xml)
builder.connect_signals({"ftob": ftob,"btof":btof})
window = builder.get_object("my_window")
window.set_title("Base64 encoder")
window.set_position(Gtk.WindowPosition.CENTER)
window.set_icon(pixbuf)
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()