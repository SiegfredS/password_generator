import tkinter as tk
from tkinter import messagebox
import pyperclip

FONT = ("Courier", 12, "normal")


class Screen:

    def __init__(self,
                 gen_password_func):
        self.gen_password_func = gen_password_func
        self.window = tk.Tk()
        # Initiate with a value of None
        self.mypass_canvas = None
        self.logo_img = None
        self.website_label = None
        self.website_entry = None
        self.email_label = None
        self.email_entry = None
        self.password_label = None
        self.password_entry = None
        self.generate_password_button = None
        self.add_button = None
        self.setup()

    def setup(self):
        self.window_setup()
        self.canvas_setup()
        self.label_entries_setup()
        self.button_setup()

    def window_setup(self):
        self.window.title("Password Manager")
        self.window.config(padx=30, pady=30)

    def canvas_setup(self):
        self.mypass_canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
        self.logo_img = tk.PhotoImage(file="logo.png")
        self.mypass_canvas.create_image(100, 100, image=self.logo_img)  # kung saan sya sa canvas, so sa gitna
        self.mypass_canvas.grid(column=1, row=0)

    def label_entries_setup(self):
        self.website_label = tk.Label(text="Website: ", font=FONT)
        self.website_label.grid(column=0, row=1)
        self.website_entry = tk.Entry()
        self.website_entry.config(width=45)
        self.website_entry.grid(column=1, row=1, columnspan=2)
        self.email_label = tk.Label(text="Email/Username", font=FONT)
        self.email_label.grid(column=0, row=2)
        self.email_entry = tk.Entry()
        self.email_entry.config(width=45)
        self.email_entry.grid(column=1, row=2, columnspan=2)
        self.email_entry.insert(tk.END, "@gmail.com")  # emails and/or usernames end with @gmail.com
        self.password_label = tk.Label(text="Password", font=FONT)
        self.password_label.grid(column=0, row=3)
        self.password_entry = tk.Entry()
        self.password_entry.config(width=27)
        self.password_entry.grid(column=1, row=3)

    def button_setup(self):
        self.generate_password_button = tk.Button(text="Generate Password", command=self.password_to_entry)
        self.generate_password_button.grid(column=2, row=3)
        self.add_button = tk.Button(text="Add", command=self.add_password)
        self.add_button.config(width=36)
        self.add_button.grid(column=1, row=4, columnspan=2)

    def add_password(self):
        saved_website = self.website_entry.get()
        saved_email = self.email_entry.get()
        saved_password = self.password_entry.get()
        is_there_empty = len(saved_password) == 0 or len(saved_email) == 0 or len(saved_website) == 0

        if is_there_empty:
            messagebox.showinfo(title="Oopsie", message="Please don't leave any empty lines")

        else:

            is_okay = messagebox.askokcancel(title=saved_website,
                                             message=f"Save:\n{saved_website} | {saved_email} | {saved_password}\n in the database?")
            if is_okay:

                with open(file="data.txt", mode="a") as saved_data:  # append lang, not write
                    saved_data.writelines(f"{saved_website} | {saved_email} | {saved_password}\n")
                    self.website_entry.delete(0, tk.END)  # delete everything
                    self.password_entry.delete(0, tk.END)
                    self.email_entry.delete(0, tk.END)
                    self.email_entry.insert(tk.END, "@gmail.com")

            else:
                pass

    def password_to_entry(self):
        self.password_entry.delete(0, tk.END)
        generated_password = self.gen_password_func()
        self.password_entry.insert(tk.END, generated_password)
        pyperclip.copy(generated_password)

    def run(self):
        self.window.mainloop()
