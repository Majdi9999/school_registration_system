import tkinter as tk
from Registration_Form import RegistrationForm


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Managment System")
        self.geometry("900x600")
        self.create_widgets()

    def create_widgets(self):
        title_lable = tk.Label(self, text="Students Management System", font=('Helvetica',16))
        title_lable.pack(side='top',fill='x')
        self.registeration_form = RegistrationForm(self)
        self.registeration_form.pack(side='left', fill='y',padx=10,pady=10)
        



if __name__ == '__main__':
    app = MainApp()
    app.mainloop()