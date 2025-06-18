import tkinter as tk
from tkinter import ttk
from database_handler import DataBaseHandler
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class RegistrationForm(tk.Frame):
    def __init__(self, parent,refresh_callback):
        super().__init__(parent,padx=10,pady=10)
        self.refresh_callback = refresh_callback

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

        self.visualize_button = tk.Button(self, text="Visualize Gender Distribution", command=self.visualize_gender_distribution)
        self.visualize_button.pack(fill='x', pady=(10, 0))

        self.exit_button = tk.Button(self, text="Exit", command=self.quit_app)
        self.exit_button.pack(fill='x', pady=(10, 0))
    
    def submit_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()

        if name and email and age and gender:
            DataBaseHandler.insert_student(name,email,age,gender)
            self.refresh_callback()
            self.reset_form()

    def reset_form(self):
        self.name_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.age_entry.set(10) 
        self.name_entry.set(None)

    def quit_app(self):
        self.master.destroy()

    def visualize_gender_distribution(self):
        students = DataBaseHandler.read_all_students()

        if not students:
            messagebox.showinfo("No Data", "There are no students to visualize.")  # إعلام المستخدم إذا ما في بيانات
            return

        
        male_count = sum(1 for s in students if s[4] == 'Male')
        female_count = sum(1 for s in students if s[4] == 'Female')

        
        fig, ax = plt.subplots()
        ax.pie([male_count, female_count], labels=['Male', 'Female'], autopct='%1.1f%%', startangle=90)
        ax.axis('equal') 

        chart_window = tk.Toplevel(self)
        chart_window.title("Gender Distribution")
        canvas = FigureCanvasTkAgg(fig, master=chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)