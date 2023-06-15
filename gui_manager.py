import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

class GuiManager:

    def __init__(self, chat_app):
        self.chat_app = chat_app

        self.root = tk.Tk()
        self.root.title('Secure Chat App')

        self.frame = ttk.Frame(self.root, padding='10')
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.text_field = ttk.Entry(self.frame, width=50)
        self.text_field.grid(row=0, column=0, padx=(0, 10))

        self.send_button = ttk.Button(self.frame, text='Send', command=self.send_message)
        self.send_button.grid(row=0, column=1)

        self.file_button = ttk.Button(self.frame, text='Send File', command=self.send_file)
        self.file_button.grid(row=0, column=2, padx=(10, 0))

        self.text_area = tk.Text(self.frame, width=50, height=15)
        self.text_area.grid(row=1, column=0, columnspan=3, pady=(10, 0))

        self.status_label = ttk.Label(self.frame, text='Disconnected')
        self.status_label.grid(row=2, column=0, columnspan=3, pady=(10, 0))

        self.progress = ttk.Progressbar(self.frame, mode='indeterminate')
        self.progress.grid(row=3, column=0, columnspan=3, pady=(10, 0))

    def run(self):
        self.root.mainloop()

    def send_message(self):
        message = self.text_field.get()
        if message:
            self.chat_app.send_message(message)

    def send_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.chat_app.send_file(file_path)

    def update_status(self, status):
        self.status_label['text'] = status

    def update_progress(self, value):
        self.progress['value'] = value

    def display_message(self, message):
        self.text_area.insert(tk.END, message + '\n')

    def display_error(self, error):
        messagebox.showerror('Error', error)

    def ask_password(self):
        password = tk.simpledialog.askstring("Password", "Enter password:", show='*')
        return password
