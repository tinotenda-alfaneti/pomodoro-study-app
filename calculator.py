from tkinter import Label, Button, Entry, Tk, END

class Calculator:
    
    '''Calculator class'''
    
    def __init__(self):
        
        self.current_num = ""
        self.math = ""
        self.first_num = 0
        self.fib_data = {}
        self.font_name = "Courier"

    def calc_ui(self):
        
        '''Calculator user interface'''
        
        self.root = Tk()
        self.root.title("Ashesi Student Calculator")

        self.entry_box = Entry(self.root, width = 40, borderwidth=10)
        self.entry_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        #creating the buttons
        self.btn_1 =Button(self.root, bg="yellow", fg="green", text="1", font=(self.font_name, 10, "bold"), padx=40, pady=20, command=lambda: self.btn_press(1))
        self.btn_2 =Button(self.root, bg="yellow", fg="green", text="2", font=(self.font_name, 10, "bold"), padx=40, pady=20, command=lambda: self.btn_press(2))
        self.btn_3 =Button(self.root, bg="yellow", fg="green", text="3", font=(self.font_name, 10, "bold"), padx=40, pady=20, command=lambda: self.btn_press(3))
        self.btn_4 =Button(self.root, bg="yellow", fg="green", text="4", font=(self.font_name, 10, "bold"), padx=40, pady=20, command=lambda: self.btn_press(4))
        self.btn_5 =Button(self.root, bg="yellow", fg="green", text="5", font=(self.font_name, 10, "bold"), padx=40, pady=20, command=lambda: self.btn_press(5))
        self.btn_6 =Button(self.root, bg="yellow", fg="green", text="6", font=(self.font_name, 10, "bold"), padx=40, pady=20, command=lambda: self.btn_press(6))
        self.btn_7 =Button(self.root, bg="yellow", fg="green", text="7", font=(self.font_name, 10, "bold"), padx=40, pady=20, command=lambda: self.btn_press(7))
        self.btn_8 =Button(self.root, bg="yellow", fg="green", text="8", font=(self.font_name, 10, "bold"), padx=40, pady=20, command=lambda: self.btn_press(8))
        self.btn_9 =Button(self.root, bg="yellow", fg="green", text="9", font=(self.font_name, 10, "bold"), padx=40, pady=20, command=lambda: self.btn_press(9))
        self.btn_0 =Button(self.root, bg="yellow", fg="green", text="0", font=(self.font_name, 10, "bold"), padx=40, pady=20, command=lambda: self.btn_press(0))
        
        self.btn_add =Button(self.root, bg="yellow", fg="green", font=(self.font_name, 10, "bold"), text="+", padx=39, pady=20, command= self.btn_add)
        self.btn_equal =Button(self.root, text="=", bg="yellow", fg="green", font=(self.font_name, 10, "bold"), padx=91, pady=20, command=self.btn_equal)
        self.btn_clear =Button(self.root, text="clear", bg="yellow", fg="green", font=(self.font_name, 10, "bold"), padx=79, pady=20, command=self.btn_clear)
        self.btn_subtract =Button(self.root, bg="yellow", fg="green", font=(self.font_name, 10, "bold"), text="-", padx=41, pady=20, command= self.subtract_btn)
        self.btn_multiply =Button(self.root, text="X", bg="yellow", fg="green", font=(self.font_name, 10, "bold"), padx=40, pady=20, command= self.multiplication_btn)
        self.btn_divide =Button(self.root, text="/", bg="yellow", fg="green", font=(self.font_name, 10, "bold"), padx=41, pady=20, command= self.division_btn)
        self.btn_fibonacci =Button(self.root, text="Fibonacci", bg="yellow", fg="green", font=(self.font_name, 10, "bold"), padx=90, pady=20, command= self.fibonacci_btn)
        # put btns on the screen
        self.btn_1.grid(row=3, column=0)
        self.btn_2.grid(row=3, column=1)
        self.btn_3.grid(row=3, column=2)

        self.btn_4.grid(row=2, column=0)
        self.btn_5.grid(row=2, column=1)
        self.btn_6.grid(row=2, column=2)

        self.btn_7.grid(row=1, column=0)
        self.btn_8.grid(row=1, column=1)
        self.btn_9.grid(row=1, column=2)

        self.btn_0.grid(row=4, column=0)
        self.btn_clear.grid(row=4, column=1, columnspan=2)
        self.btn_add.grid(row=5, column=0)
        self.btn_equal.grid(row=5, column=1, columnspan=2)

        self.btn_subtract.grid(row=6, column=0)
        self.btn_multiply.grid(row=6, column=1)
        self.btn_divide.grid(row=6, column=2)
        self.btn_fibonacci.grid(row=7, column=0, columnspan=3)
        
        
        self.root.mainloop()
        
    # functionalities of the buttons
    def btn_press(self, number):
        self.number = number
        self.current_num = self.entry_box.get()
        self.entry_box.delete(0, END)
        self.entry_box.insert(0, str(self.current_num) + str(self.number))

    def btn_clear(self):
        self.entry_box.delete(0, END)

    def btn_add(self):
        if self.entry_box.get() != "":
            self.first_number=self.entry_box.get()
            self.math = "addition"
            self.first_num = int(self.first_number)
            self.entry_box.delete(0, END)
        

    def btn_equal(self):
        if self.entry_box.get() != "":
            self.second_number = self.entry_box.get()
            self.entry_box.delete(0, END)
            if self.math == "addition":
                self.entry_box.insert(0, self.first_num + int(self.second_number))
            elif self.math == "subtraction":
                self.entry_box.insert(0, self.first_num - int(self.second_number))
            elif self.math == "multiplication":
                self.entry_box.insert(0, self.first_num * int(self.second_number))
            elif self.math == "division":
                self.entry_box.insert(0, self.first_num / int(self.second_number))


    def subtract_btn(self):
        if self.entry_box.get() != "":
            self.first_number=self.entry_box.get()
            self.math = "subtraction"
            self.first_num = int(self.first_number)
            self.entry_box.delete(0, END)


    def division_btn(self):
        if self.entry_box.get() != "":
            self.first_number=self.entry_box.get()
            self.math = "division"
            self.first_num = int(self.first_number)
            self.entry_box.delete(0, END)
        
    def multiplication_btn(self):
        if self.entry_box.get() != "":
            self.first_number=self.entry_box.get()
            self.math = "multiplication"
            self.first_num = int(self.first_number)
            self.entry_box.delete(0, END)
     
     # fibonacci calculation
    def fibonacci_btn(self):
        if self.entry_box.get() != "":
            self.first_number=self.entry_box.get()
            self.math = "fibonacci"
            self.first_num = int(self.first_number)
            self.entry_box.delete(0, END)
            self.number = self.fibonacci_number(int(self.first_number))
            self.entry_box.insert(0, self.number)

        
    def fibonacci_number(self, number):
        if number in (0, 1):
            return number
        elif number in self.fib_data:
            return self.fib_data[number]
        else:
            self.fib_data[number] = self.fibonacci_number(number - 1) + self.fibonacci_number(number - 2) # saving the values to avoid repetition on next run # memoization
            return self.fib_data[number]



        
        
        

    




