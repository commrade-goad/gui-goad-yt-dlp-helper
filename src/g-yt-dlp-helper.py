# importing some library
import gi
import os
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# program start here
class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="TESTING")
        self.set_border_width(10)
        grid = Gtk.Grid()
        self.add(grid)

        button1 = Gtk.Button(label="button1")
        button2 = Gtk.Button(label="button2")
        button3 = Gtk.Button(label="button3")
        button4 = Gtk.Button(label="button4")
        button5 = Gtk.Button(label="button5")

        grid.add(button1)
#                            x   y  xs  ys
        grid.attach(button2, 1 , 0, 2, 1)
        grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 10, 1)
        grid.attach(button4, 1 , 2, 1, 1)

# window stuff
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
