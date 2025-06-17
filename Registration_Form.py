import tkinter as tk
from tkinter import ttk
from database_handler import DataBaseHandler
class RegistrationForm(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent,padx=10,pady=10)

        tk.Label(self, text='Full Name').pack(fill='x')
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        tk.Label(self, text='Email').pack(fill='x')
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        tk.Label(self, text='Age').pack(fill='x')
        self.age_entry = ttk.Spinbox(self,from_=10,to=100)
        self.age_entry.pack()

        tk.Label(self, text='Gender').pack(fill='x')
        self.gender_entry = tk.StringVar()
        tk.Radiobutton(self,text='Male',variable=self.gender_entry,value='Male').pack(anchor='w')
        tk.Radiobutton(self,text='Female',variable=self.gender_entry,value='Female').pack(anchor='w')
        
        self.submit_button = tk.Button(self, text="Submit",command=self.submit_form)
        self.submit_button.pack(fill='x')
    
    def submit_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()

        if name and email and age and gender:
            DataBaseHandler.insert_student(name,email,age,gender)
            
            self.reset_form()

    def reset_form(self):
        self.name_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.age_entry.set(10)
        self.name_entry.set(None)