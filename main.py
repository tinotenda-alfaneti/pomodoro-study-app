from tkinter import Tk, Label, Button  
from user_register import *
from calculator import *

# initialising the graphical user interface window 
window = Tk()
# screen title
window.title("Ashesi Study App")
window.config(padx=100, pady=100)

# Tracking App users
font_name = "Courier"
calcu = Calculator()


#checking the user
def checking_user(user, name):
    
    '''function to check if the user is registered. If not, it takes the student to the registration class'''
    
    # creating an instance of the Register class
    student_register = Register(window, user, name, welcome_label)
    
    registered_students = open("students.txt", "r")
    for record in registered_students:
        if user == record.split("|")[0].strip():
            student_register.success_registration()
            return None

    student_register.registering()



# Welcoming user
def welcome():
    
    '''Function that welcomes the user'''
    
    user = username.get()  # Taking the input from the entry widget 
    name = user.split("@")[0]
    
    # checking if the entry box is not empty
    if user != "":
        username_label.destroy()
        welcome_label.config(text="Hello, " + name)
        username.destroy()
        welcome_label.grid(row=0, column=0, columnspan=2)
        login_button.destroy()
        checking_user(user, name)



# Logging in page

welcome_label = Label(window, text="Welcome to studentApp", font=(font_name, 20, "bold"), fg="green", bg="yellow")
welcome_label.grid(row=0, column=0, columnspan=2, pady=20)


username_label = Label(window, text="Enter Username(Name@studentID, e.g. Joe@1234): ")
username_label.grid(row=1, column=0)

username = Entry(window, width = 50)
username.grid(row=1, column=1)

login_button = Button(window, text="Log in", command = welcome, font=(font_name, 10, "bold"), fg="green", bg="yellow")
login_button.grid(row=2, column=1, padx=10, pady=10)


window.mainloop()