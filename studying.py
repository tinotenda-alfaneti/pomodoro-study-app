from tkinter import Tk, Label, Button, HORIZONTAL 
from tkinter import ttk
import time
from tkinter import messagebox
import sys

def main(name):
    
    '''main function for studying'''
    
    # instantiating a class object for the tkinter GUI
    study_window = Tk()
    study_window.title("Studying App")
    study_window.geometry("600x400")
    
    def study():
        
        '''Studying function'''
        
        # reading and getting the saved information about how an individual wants to study
        students_register = open("students.txt", "r")
        for line in students_register:
            if  line.split("|")[0].strip() == name:
                subjects = line.split("|")[1].strip().split(",")
                num_sessions = int(line.split("|")[2].strip())
                session = int(line.split("|")[3].strip())
                break_time  = int(line.split("|")[4].strip())
        name_label.config(text=f"Go, Go, {name.split('@')[0]}",font=("courier", 10, "bold"), fg="green", bg="yellow")
        
        
        # session and time tracker function
        def session_counter(num_sessions, subjects, session, break_time):
        
            subjects_list = subjects*num_sessions # multiplying the subjects list by number of sessions so that we won't fall into the index out of range error
            count_1 = session
            count_2 = break_time

            # Base case
            if num_sessions == 0:
                messagebox.showinfo("done", "Study is Over")
                return None

            # Sessions
            messagebox.showinfo("study", "Session {}: You are studying {}".format(num_sessions, subjects_list[num_sessions])) # popup messagebox
            while count_1 > 0:
                count_1 -= 1
                progress["value"] += ((1/session)*100) # updating the value of the progress widget
                study_window.update_idletasks() # updating the screen before it reaches to the mainloop so that the student can see the time left
                time.sleep(0.5) #time in seconds 
            progress["value"] = 100

            # Breaks
            while count_2 > 0:
                if count_2 == break_time:
                    messagebox.showinfo("break", "On break...!")
                count_2 -= 1
                progress["value"] -= ((1/break_time)*100)
                study_window.update_idletasks()
                time.sleep(0.5)
            
            # terminating window
            option = messagebox.askquestion("option", "Continue studying")
            if option == "no":
                sys.exit()
                
            # recursive statement
            session_counter(num_sessions - 1 , subjects, session, break_time)
            
            
        session_counter(num_sessions, subjects, session, break_time)

    
    # progress widget that updates with time in this case
    progress = ttk.Progressbar(study_window, orient=HORIZONTAL, length=300, mode='determinate')
    progress.grid(row=1, column=0, pady=20, padx=150, columnspan=3)

    start_button = Button(study_window, text="Start", command = study, font=("courier", 10, "bold"), fg="green", bg="yellow")
    start_button.grid(row=2, column=1, padx=150, pady=10)

    name_label = Label(study_window, text="")
    name_label.grid(row=0, column=1, padx=150, pady=10)


    study_window.mainloop()
