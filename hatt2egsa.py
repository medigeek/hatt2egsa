#!/usr/bin/python
# -*- coding: utf-8 -*-

""" Usage:
    ./hatt2egsa.py
"""

""" Example HATT lines:
1,6985.90,-14252.00,0
2,7002.70,-14366.20,0
3,7016.20,-14421.50,0
4,7033.40,-14477.40,0
5,7062.10,-14549.30,0
6,7084.00,-14611.10,0
7,7128.50,-14702.80,0
8,7143.90,-14725.10,0
9,7154.20,-14731.00,0
10,7185.70,-14761.90,0"""

""" Correct values EGSA87 (GGRS87, GR87) for Mitilini:
1,720186.936,4333162.749,0
2,720206.828,4333049.024,0
3,720221.824,4332994.100,0
4,720240.536,4332938.676,0
5,720271.179,4332867.566,0
6,720294.750,4332806.371,0
7,720341.728,4332715.893,0
8,720357.730,4332694.014,0
9,720368.188,4332688.395,0
10,720400.521,4332658.354,0
"""
    
#Gtk+ 3
from gi.repository import Gtk
#Gobject -> glib
import glib

class gui():
    def __init__(self):
        self.uifile = "hatt2egsa.ui"
        self.area = 'ΜΥΤΙΛΗΝΗ,39.15,2.45,712815.509,0.999835574,-0.02715992,3.16E-09,-2.22E-09,1.11E-09,4347222.467,0.027176178,0.99980037,-2.72E-10,3.19E-10,4.67E-09'
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.uifile)
        self.window = self.builder.get_object("window1")
        self.entry1 = self.builder.get_object("entry1")
        self.entry2 = self.builder.get_object("entry2")
        self.entry3 = self.builder.get_object("entry3")
        self.entry4 = self.builder.get_object("entry4")
        self.builder.connect_signals(self)

    def on_button1_clicked(self, widget):
        txt1 = self.entry1.get_text()
        txt2 = self.entry2.get_text()
        txt3 = self.entry3.get_text()
        if txt3:
            HATTcoords = txt3
        else:
            HATTcoords = '{0},{1}'.format(txt1, txt2)
        self.convert(HATTcoords)
    
    def gtk_main_quit(self, *args):
        Gtk.main_quit()
    
    def convert(self, HATTline):
        areaarray = self.area.split(",")
        A0=float(areaarray[3])
        A1=float(areaarray[4])
        A2=float(areaarray[5])
        A3=float(areaarray[6])
        A4=float(areaarray[7])
        A5=float(areaarray[8])
        B0=float(areaarray[9])
        B1=float(areaarray[10])
        B2=float(areaarray[11])
        B3=float(areaarray[12])
        B4=float(areaarray[13])
        B5=float(areaarray[14])

        HATTarray = HATTline.split(",")
        x = float(HATTarray[0])
        y = float(HATTarray[1])

        GR87x = round(A0 + A1 * x + A2 * y + A3 * x**2 + A4 * y**2 + A5 * x * y, 3)
        GR87y = round(B0 + B1 * x + B2 * y + B3 * x**2 + B4 * y**2 + B5 * x * y, 3)
        GR87xy = "{0}, {1}".format(GR87x, GR87y)
        print("HATT: {0}\nGR87: {1}".format(HATTline, GR87xy))
        self.entry4.set_text(GR87xy)

if __name__ == "__main__":
    gui()
    Gtk.main()
