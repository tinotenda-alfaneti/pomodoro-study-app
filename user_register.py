from tkinter import Label, Entry, Button
from calculator import Calculator
import time
import studying

class Register:
    '''Class for registeration and registration window'''
    
    def __init__(self, window, user, name, welcome_label):
        
        self.window = window
        self.user = user
        self.name  = name
        self.welcome_label = welcome_label
        self.font_name = "Courier"
        self.calc = Calculator()
        

    def registering(self):
        
        '''Function for registration user interface'''

        self.register_button = Button(self.window, text="Register", command = self.capturing_info, font=(self.font_name, 10, "bold"), fg="green", bg="yellow")
        self.register_button.grid(row=5, column=1, padx=10, pady=10)

        self.subjects_label = Label(self.window, text="Enter subjects(comma seperated): ")
        self.subjects_label.grid(row=1, column=0)

        self.subjects_entry = Entry(self.window, width = 50)
        self.subjects_entry.grid(row=1, column=1)

        self.sessions_label = Label(self.window, text="Enter number of sessions you study: ")
        self.sessions_label.grid(row=2, column=0)

        self.sessions_entry = Entry(self.window, width = 10)
        self.sessions_entry.grid(row=2, column=1)

        self.sessiontime_label = Label(self.window, text="Enter time per session(min): ")
        self.sessiontime_label.grid(row=3, column=0)

        self.sessiontime_entry = Entry(self.window, width = 30)
        self.sessiontime_entry.grid(row=3, column=1)

        self.sessionbreak_label = Label(self.window, text="Enter time for resting(min): ")
        self.sessionbreak_label.grid(row=4, column=0)

        self.sessionbreak_entry = Entry(self.window, width = 30)
        self.sessionbreak_entry.grid(row=4, column=1)

    #saving the information to a file after the button to register has been clicked.
    def capturing_info(self):
        
        '''function for capturing the information'''

        self.my_subjects = self.subjects_entry.get()
        self.my_number_sessions = self.sessions_entry.get()
        self.my_session = self.sessiontime_entry.get()
        self.my_break_time = self.sessionbreak_entry.get()

        if "" not in (self.my_subjects, self.my_number_sessions, self.my_session, self.my_break_time):

            self.students_register = open("students.txt", "a")
            self.students_register.write("{:^15}  |  {:^15}  |  {:^15}  |  {:^15}  |  {:^15}\n".format(self.user, self.my_subjects, self.my_number_sessions, self.my_session, self.my_break_time))
            self.students_register.close()
            
            # clearing the screen
            self.subjects_label.destroy()
            self.subjects_entry.destroy()
            self.sessions_label.destroy()
            self.sessions_entry.destroy()
            self.sessiontime_label.destroy()
            self.sessiontime_entry.destroy()
            self.sessionbreak_label.destroy()
            self.sessionbreak_entry.destroy()
            self.register_button.destroy()


            self.welcome_label.config(text="Registration Successful, " + self.name)
            self.success_registration()
            
    # successful registration screen
    def success_registration(self):
        
        '''function for the successful registration screen'''
        
        self.welcome_label.config(text="Let's get started " + self.name)

        self.calculator_button = Button(self.window, text="Calculator", command = self.calc.calc_ui, font=(self.font_name, 10, "bold"), fg="green", bg="yellow")
        self.calculator_button.grid(row=1, column=0, padx=10, pady=10)

        self.study_button = Button(self.window, text="Study", command =lambda: studying.main(self.user), font=(self.font_name, 10, "bold"), fg="green", bg="yellow")
        self.study_button.grid(row=1, column=1, padx=10, pady=10)

        


