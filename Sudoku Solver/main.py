import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,GdkPixbuf
import numpy as np
import pandas as pd
import compute as fn
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
  <object class="GtkFileFilter" id="csv filter">
    <patterns>
      <pattern>*.csv</pattern>
    </patterns>
  </object>
  <object class="GtkWindow" id="window">
    <property name="can-focus">False</property>
    <property name="resizable">False</property>
    <property name="window-position">center-always</property>
    <property name="default-width">680</property>
    <property name="default-height">760</property>
    <child>
      <object class="GtkFixed">
        <property name="visible">True</property>
        <property name="can-focus">False</property>
        <child>
          <object class="GtkEntry" id="n11">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">10</property>
            <property name="y">10</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n12">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">80</property>
            <property name="y">10</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n13">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">150</property>
            <property name="y">10</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n21">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">10</property>
            <property name="y">80</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n22">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">80</property>
            <property name="y">80</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n23">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">150</property>
            <property name="y">80</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n31">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">10</property>
            <property name="y">150</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n32">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">80</property>
            <property name="y">150</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n33">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">150</property>
            <property name="y">150</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="generater">
            <property name="label" translatable="yes">Generate Solution</property>
            <property name="width-request">180</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="on_button_clicked" swapped="no"/>
          </object>
          <packing>
            <property name="x">16</property>
            <property name="y">690</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n14">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">240</property>
            <property name="y">10</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n41">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">10</property>
            <property name="y">240</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n51">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">10</property>
            <property name="y">310</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n61">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">10</property>
            <property name="y">380</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n71">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">10</property>
            <property name="y">470</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n81">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">10</property>
            <property name="y">540</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n91">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">10</property>
            <property name="y">610</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n15">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">310</property>
            <property name="y">10</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n16">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">380</property>
            <property name="y">10</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n17">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">470</property>
            <property name="y">10</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n18">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">540</property>
            <property name="y">10</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n19">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">610</property>
            <property name="y">10</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n42">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">80</property>
            <property name="y">240</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n43">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">150</property>
            <property name="y">240</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n52">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">80</property>
            <property name="y">310</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n53">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">150</property>
            <property name="y">310</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n54">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">240</property>
            <property name="y">310</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n55">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">310</property>
            <property name="y">310</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n56">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">380</property>
            <property name="y">310</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n57">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">470</property>
            <property name="y">310</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n88">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">540</property>
            <property name="y">540</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n58">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">540</property>
            <property name="y">310</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n59">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">610</property>
            <property name="y">310</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n62">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">80</property>
            <property name="y">380</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n63">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">150</property>
            <property name="y">380</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n65">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">310</property>
            <property name="y">380</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n64">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">240</property>
            <property name="y">380</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n66">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">380</property>
            <property name="y">380</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n67">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">470</property>
            <property name="y">380</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n68">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">540</property>
            <property name="y">380</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n69">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">610</property>
            <property name="y">380</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n44">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">240</property>
            <property name="y">240</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n24">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">240</property>
            <property name="y">80</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n25">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">310</property>
            <property name="y">80</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n26">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">380</property>
            <property name="y">80</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n77">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">470</property>
            <property name="y">470</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n99">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">610</property>
            <property name="y">610</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n73">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">150</property>
            <property name="y">470</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n93">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">150</property>
            <property name="y">610</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n92">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">80</property>
            <property name="y">610</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n94">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">240</property>
            <property name="y">610</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n95">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">310</property>
            <property name="y">610</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n96">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">380</property>
            <property name="y">610</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n97">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">470</property>
            <property name="y">610</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n98">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">540</property>
            <property name="y">610</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n82">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">80</property>
            <property name="y">540</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n83">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">150</property>
            <property name="y">540</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n84">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">240</property>
            <property name="y">540</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n85">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">310</property>
            <property name="y">540</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n86">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">380</property>
            <property name="y">540</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n87">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">470</property>
            <property name="y">540</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n72">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">80</property>
            <property name="y">470</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n74">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">240</property>
            <property name="y">470</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n75">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">310</property>
            <property name="y">470</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n76">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">380</property>
            <property name="y">470</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n78">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">540</property>
            <property name="y">470</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n79">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">610</property>
            <property name="y">470</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n89">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">610</property>
            <property name="y">540</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n45">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">310</property>
            <property name="y">240</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n46">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">380</property>
            <property name="y">240</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n47">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">470</property>
            <property name="y">240</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n48">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">540</property>
            <property name="y">240</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n49">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">610</property>
            <property name="y">240</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n34">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">240</property>
            <property name="y">150</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n39">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">610</property>
            <property name="y">150</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n29">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">610</property>
            <property name="y">80</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n28">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">540</property>
            <property name="y">80</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n27">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">470</property>
            <property name="y">80</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n38">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">540</property>
            <property name="y">150</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n36">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">380</property>
            <property name="y">150</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n37">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">470</property>
            <property name="y">150</property>
          </packing>
        </child>
        <child>
          <object class="GtkEntry" id="n35">
            <property name="width-request">60</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="width-chars">0</property>
          </object>
          <packing>
            <property name="x">310</property>
            <property name="y">150</property>
          </packing>
        </child>
        <child>
          <object class="GtkFileChooserButton" id="filechoose">
            <property name="width-request">100</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <property name="tooltip-text" translatable="yes">choose csv file, missing number as zeros</property>
            <property name="filter">csv filter</property>
            <property name="title" translatable="yes"/>
          </object>
          <packing>
            <property name="x">566</property>
            <property name="y">690</property>
          </packing>
        </child>
        <child>
          <object class="GtkLabel">
            <property name="width-request">150</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">False</property>
            <property name="label" translatable="yes">or choose CSV file</property>
          </object>
          <packing>
            <property name="x">404</property>
            <property name="y">690</property>
          </packing>
        </child>
        <child>
          <object class="GtkButton" id="save">
            <property name="label" translatable="yes">save results to csv</property>
            <property name="width-request">180</property>
            <property name="height-request">60</property>
            <property name="visible">True</property>
            <property name="can-focus">True</property>
            <property name="receives-default">True</property>
            <signal name="clicked" handler="savecsv" swapped="no"/>
          </object>
          <packing>
            <property name="x">220</property>
            <property name="y">690</property>
          </packing>
        </child>
      </object>
    </child>
  </object>
</interface>
"""
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
builder.add_from_string(xml)
datagen= builder.get_object("generater")
save= builder.get_object("save")
builder.connect_signals({"on_button_clicked": on_button_clicked,"savecsv":savecsv})

window = builder.get_object("window")
window.set_title("Sudoku Sover")
window.set_position(Gtk.WindowPosition.CENTER)
window.set_icon(pixbuf)
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()