import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk, Gdk, GLib

clipboard_history = []

def get_clipboard_text():
    clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
    text = clipboard.wait_for_text()

    if text:
        clipboard_history.append(text)

def check_clipboard():
    get_clipboard_text()
    return True

GLib.timeout_add(1000, check_clipboard())

Gtk.main()