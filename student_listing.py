import tkinter as tk
from tkinter import ttk
from database_handler import DataBaseHandler

class StudentListing(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.create_widgets()

    def create_widgets(self):
        self.tree = ttk.Treeview(self, columns=('ID', 'Name','Email','Age','Gender'), show = 'headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Email', text='Email')
        self.tree.heading('Age', text='Age')
        self.tree.heading('Gender', text='Gender')
        self.tree.pack(fill= tk.BOTH,expand=True)
        self.load_students()
    
    def load_students(self):
        self.tree.delete(*self.tree.get_children())
        for x in DataBaseHandler.read_all_students():
            self.tree.insert('',tk.END,values=x)
        