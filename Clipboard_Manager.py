import os
import gi
gi.require_versions({'Gtk' : '3.0', 'Gdk' : '3.0'})
from gi.repository import Gtk, Gdk, GLib

class ClipboardManager(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = "Clipboard History")
        self.set_border_width(10)
        self.listbox = Gtk.ListBox()
        self.add(self.listbox)
        self.listbox.connect("key-press-event", self.on_key_press)

        self.clipboard_list = []

    def add_to_clipboard(self, text):
        if text not in self.clipboard_list:
            self.clipboard_list.append(text)
            label = Gtk.Label(text)
            row = Gtk.ListBoxRow()
            row.add(label)
            self.listbox.add(row)
            self.listbox.show_all()

    def on_key_press(self, widget, event):
        if event.keyval == Gdk.KEY_Return:
            selected_row = self.listbox.get_selected_row()

            if selected_row:
                selected_text = selected_row.get_child().get_text()

                clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
                clipboard.set_text(selected_text, -1)
                clipboard.request_text(lambda cb, text: print(f"Pasted: {text}"))

                os.system("xdotool key ctrl+v")

window = ClipboardManager()
window.connect("destroy", Gtk.main_quit)
window.show_all()

def check_clipboard():
    clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
    text = clipboard.wait_for_text()

    if text:
        window.add_to_clipboard(text)
    
    return True

GLib.timeout_add(1000, check_clipboard)

Gtk.main()
