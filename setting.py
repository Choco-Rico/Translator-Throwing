import tkinter as tk
from changeKey import HotkeyConfiguration
from saveAPIkey import APIKeyManager

class HomePage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hotkey_button = tk.Button(self)
        self.hotkey_button["text"] = "Hotkey Configuration"
        self.hotkey_button["command"] = self.open_hotkey_config
        self.hotkey_button.pack(side="top")

        self.api_button = tk.Button(self)
        self.api_button["text"] = "API Key Manager"
        self.api_button["command"] = self.open_api_manager
        self.api_button.pack(side="top")

    def open_api_manager(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = APIKeyManager(self.new_window)

    def open_hotkey_config(self):
        self.new_window = tk.Toplevel(self.master)
        self.app = HotkeyConfiguration(self.new_window)

root = tk.Tk()
app = HomePage(master=root)
app.mainloop()