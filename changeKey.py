import json, os, time, sys
import os
import tkinter as tk
from tkinter import messagebox

class HotkeyConfiguration(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.modifier_var = tk.StringVar(self)
        self.key_var = tk.StringVar(self)

        modifier_options = ["ctrl", "alt", "shift", "win"]
        key_options = [chr(i) for i in range(ord('A'), ord('Z')+1)]

        # Load the configuration file
        config = self.load_config()

        # Extract the hotkey from the configuration
        hotkey = config["hotkey"]
        modifier, key = hotkey.split('+') # '+'で分割

        # Set the initial values of the OptionMenus
        self.modifier_var.set(modifier)
        self.key_var.set(key)

        modifier_menu = tk.OptionMenu(self, self.modifier_var, *modifier_options)
        key_menu = tk.OptionMenu(self, self.key_var, *key_options)

        tk.Label(self, text="Modifier").grid(row=0, column=0)
        modifier_menu.grid(row=0, column=1)

        tk.Label(self, text="Key").grid(row=1, column=0)
        key_menu.grid(row=1, column=1)

        # Create a label to display the current hotkey setting
        current_hotkey_label = tk.Label(self, text=f"Current: {modifier} {hotkey[1]}")
        current_hotkey_label.grid(row=2, column=0)

        tk.Button(self, text="Save", command=self.save).grid(row=3, column=1)

    def load_config(self):
        config_file_path = 'config.json'
        
        if os.path.exists(config_file_path):
            with open(config_file_path, 'r') as config_file:
                config = json.load(config_file)
        else:
            # Create the config file with default hotkey
            default_hotkey = "alt+C"
            config = {"hotkey": default_hotkey}
            with open(config_file_path, 'w') as config_file:
                json.dump(config, config_file)
        
        return config
    
    def save(self):
        modifier = self.modifier_var.get()
        key = self.key_var.get()
        if not modifier or not key:
            messagebox.showinfo("Error", "Both modifier and key must be selected")
            return

        config = {"hotkey": f"{modifier}+{key}"} # '+'でつなぐ
        with open("config.json", "w") as f:
            json.dump(config, f)

        messagebox.showinfo("Saved", "OK!")

        self.master.destroy()