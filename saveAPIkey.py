import tkinter as tk
from tkinter import messagebox, simpledialog
import configparser
import base64

class APIKeyManager(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.api_choice = tk.StringVar(value="Azure")

        azure_button = tk.Radiobutton(self, text="Azure", variable=self.api_choice, value="Azure")
        openai_button = tk.Radiobutton(self, text="OpenAI", variable=self.api_choice, value="OpenAI")

        openai_button.pack()
        azure_button.pack()

        submit_button = tk.Button(self, text="OK", command=self.submit_choice)
        submit_button.pack()

    def submit_choice(self):
        self.service_name = self.api_choice.get()
        self.save_api_key(self.service_name)
        self.master.destroy()

    def save_api_key(self, api_key_name):
        api_key_value = simpledialog.askstring("API Key", f"Please enter your {api_key_name} API key:", show='*')
        if api_key_value is None:
            return

        endpoint_value = ''
        location_value = ''
        if api_key_name == "Azure":
            endpoint_value = simpledialog.askstring("Endpoint", "Please enter your Azure endpoint:", show='*')
            if endpoint_value is None:
                return
            location_value = simpledialog.askstring("Location", "Please enter your Azure location:", show='*')
            if location_value is None:
                return

        # Encrypt API key, endpoint, and location
        encrypted_api_key = base64.b64encode(api_key_value.encode('utf-8')).decode('utf-8')
        encrypted_endpoint = base64.b64encode(endpoint_value.encode('utf-8')).decode('utf-8')
        encrypted_location = base64.b64encode(location_value.encode('utf-8')).decode('utf-8')

        config = configparser.ConfigParser()
        config['API'] = {'choice': api_key_name}
        config[api_key_name] = {
            'api_key': encrypted_api_key,
            'endpoint': encrypted_endpoint,
            'location': encrypted_location
        }
        with open('config.ini', 'w') as configfile:
            config.write(configfile)

        messagebox.showinfo("Success", "Your API key has been saved successfully!")

    def get_api_key(self, api_key_name):
        config = configparser.ConfigParser()
        config.read('config.ini')
        encrypted_api_key = config[api_key_name]['api_key'] if config.has_option(api_key_name, 'api_key') else None
        if encrypted_api_key is None:
            return None

        # Decrypt API key
        api_key_value = base64.b64decode(encrypted_api_key.encode('utf-8')).decode('utf-8')
        return api_key_value

if __name__ == "__main__":
    root = tk.Tk()
    app = APIKeyManager(master=root)
    app.mainloop()