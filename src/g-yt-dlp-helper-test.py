# importing some library
import gi
import os
from urllib.parse import urlparse

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# program start here
class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="goad-yt-dlp-helper GUI")
        self.set_border_width(10)
        self.set_size_request(400, 200)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.add(vbox)
        self.linkLabel = Gtk.Label()
        self.linkLabel.set_text("Link")
        #self.linkLabel.set_justify(Gtk.Justification.LEFT)
        vbox.pack_start(self.linkLabel, True, True, 0)
        self.link = Gtk.Entry()
        vbox.pack_start(self.link, True, True, 0)

        self.pathLabel = Gtk.Label()
        self.pathLabel.set_text("Path")
        #self.pathLabel.set_justify(Gtk.Justification.LEFT)
        vbox.pack_start(self.pathLabel, True, True, 0)

        cwdPrint = os.getcwd()
        self.cwdLabel = Gtk.Label()
        self.cwdLabel.set_text("Current working dir : "+cwdPrint)
        vbox.pack_start(self.cwdLabel, True, True, 0)

        self.path = Gtk.Entry()
        vbox.pack_start(self.path, True, True, 0)

        self.formatLabel = Gtk.Label()
        self.formatLabel.set_text("Format")
        #self.formatLabel.set_justify(Gtk.Justification.LEFT)
        vbox.pack_start(self.formatLabel, True, True, 0)
        self.vFormat = Gtk.Entry()
        vbox.pack_start(self.vFormat, True, True, 0)

        self.downButton = Gtk.Button(label="Download")
        self.downButton.connect("clicked", self.button_download)
        vbox.pack_start(self.downButton, True, True, 0)

        self.statusLabel = Gtk.Label()
        self.statusLabel.set_text("Status :")
        vbox.pack_start(self.statusLabel, True, True, 0)

    def button_download(self, widget):
        linkInput = self.link.get_text()
        pathInput = self.path.get_text()
        formatInput = self.vFormat.get_text()

        #checking link
        urlcheck = urlparse(linkInput)
        urlcheckbol = (all([urlcheck.scheme, urlcheck.netloc, urlcheck.path])
                        and len(urlcheck.netloc.split(".")) > 1)
        if urlcheckbol == False:
            self.statusLabel.set_text("Status : not a valid url!")
            return
        #checking dir
        dircheck=os.path.isdir(pathInput)
        if dircheck == False:
            self.statusLabel.set_text("Status : not a valid dir.")
            return

        os.chdir(pathInput)
        os.system("yt-dlp -f "+formatInput+" "+linkInput)
        self.statusLabel.set_text("Status : Done!")

# window stuff
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
