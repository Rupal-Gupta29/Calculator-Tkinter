import tkinter
from tkinter import messagebox
import tkinter.font as tk_font


class Calculator:

    def __init__(self, root):
        self.operation_str = tkinter.StringVar()
        self.result_str = tkinter.StringVar()
        self.my_font = tk_font.Font(weight="bold")
        self.root = root
        self.root.title("Calculator")
        self.root['bg'] = '#0F0F0F'
        self.img = tkinter.PhotoImage(file="calculator.png")
        self.root.iconphoto(self.root, self.img)
        self.root.resizable(False,False)

        # display label
        self.display_operation = tkinter.Label(self.root, textvariable=self.operation_str, font=self.my_font, bg=
                                  "#0F0F0F", fg="#fff", pady=10)
        self.display_result = tkinter.Label(self.root, textvariable=self.result_str, font=self.my_font, bg="#0F0F0F",
                              fg="#fff", pady=10)

        # buttons
        self.btn_zero = tkinter.Button(text="0", command=lambda: self.get_value("0"), width=5, font=self.my_font,
                                       relief="flat", bg="#3F3F3F", fg="#fff")
        self.btn_one = tkinter.Button(text="1", command=lambda: self.get_value("1"), width=5, font=self.my_font,
                                      relief="flat", bg="#3F3F3F", fg="#fff")
        self.btn_two = tkinter.Button(text="2", command=lambda: self.get_value("2"), width=5, font=self.my_font,
                                      relief="flat", bg="#3F3F3F", fg="#fff")
        self.btn_three = tkinter.Button(text="3", command=lambda: self.get_value("3"), width=5, font=self.my_font,
                                      relief="flat", bg="#3F3F3F", fg="#fff")
        self.btn_four = tkinter.Button(text="4", command=lambda: self.get_value("4"), width=5, font=self.my_font,
                                       relief="flat", bg="#3F3F3F", fg="#fff")
        self.btn_five = tkinter.Button(text="5", command=lambda: self.get_value("5"), width=5, font=self.my_font,
                                       relief="flat", bg="#3F3F3F", fg="#fff")
        self.btn_six = tkinter.Button(text="6", command=lambda: self.get_value("6"), width=5, font=self.my_font,
                                       relief="flat", bg="#3F3F3F", fg="#fff")
        self.btn_seven = tkinter.Button(text="7", command=lambda: self.get_value("7"), width=5, font=self.my_font,
                                       relief="flat", bg="#3F3F3F", fg="#fff")
        self.btn_eight = tkinter.Button(text="8", command=lambda: self.get_value("8"), width=5, font=self.my_font,
                                       relief="flat", bg="#3F3F3F", fg="#fff")
        self.btn_nine = tkinter.Button(text="9", command=lambda: self.get_value("9"), width=5, font=self.my_font,
                                       relief="flat", bg="#3F3F3F", fg="#fff")

        self.btn_plus = tkinter.Button(text="+", command=lambda: self.get_value("+"), width=5, font=self.my_font,
                                       relief="flat", bg="#1C5FBA", fg="#fff")
        self.btn_minus = tkinter.Button(text="-", command=lambda: self.get_value("-"), width=5, font=self.my_font,
                                       relief="flat", bg="#1C5FBA", fg="#fff")
        self.btn_multiply = tkinter.Button(text="*", command=lambda: self.get_value("*"), width=5, font=self.my_font,
                                       relief="flat", bg="#1C5FBA", fg="#fff")
        self.btn_divide = tkinter.Button(text="/", command=lambda: self.get_value("/"), width=5, font=self.my_font,
                                       relief="flat", bg="#1C5FBA", fg="#fff")
        self.btn_modulo = tkinter.Button(text="%", command=lambda: self.get_value("%"), width=5, font=self.my_font,
                                       relief="flat", bg="#1C5FBA", fg="#fff")
        self.btn_power = tkinter.Button(text="**", command=lambda: self.get_value("**"), width=5, font=self.my_font,
                                       relief="flat", bg="#1C5FBA", fg="#fff")
        self.btn_equal_to = tkinter.Button(text="=", command=self.get_result, width=5, font=self.my_font,
                                       relief="flat", bg="#379237", fg="#fff")

        self.btn_decimal = tkinter.Button(text=".", command=lambda: self.get_value("."), width=5, font=self.my_font,
                                       relief="flat", bg="#3F3F3F", fg="#fff")

        self.btn_clear = tkinter.Button(text="C", command=self.clear, width=5, font=self.my_font,
                                       relief="flat", bg="#3F3F3F", fg="#fff")
        self.btn_all_clear = tkinter.Button(text="AC", command=self.set_all_clear, width=5, font=self.my_font,
                                       relief="flat", bg="#FFBF00", fg="#000")

        # displaying labels
        self.display_operation.grid(row=0, column=0, columnspan=4, sticky="e", ipady=5)
        self.display_result.grid(row=1, column=0, columnspan=4, sticky="e", ipady=5)

        # displaying buttons
        self.btn_all_clear.grid(row=2, column=0)
        self.btn_power.grid(row=2, column=1)
        self.btn_modulo.grid(row=2, column=2)
        self.btn_divide.grid(row=2, column=3)

        self.btn_seven.grid(row=3, column=0)
        self.btn_eight.grid(row=3, column=1)
        self.btn_nine.grid(row=3, column=2)
        self.btn_multiply.grid(row=3, column=3)

        self.btn_four.grid(row=4, column=0)
        self.btn_five.grid(row=4, column=1)
        self.btn_six.grid(row=4, column=2)
        self.btn_minus.grid(row=4, column=3)

        self.btn_one.grid(row=5, column=0)
        self.btn_two.grid(row=5, column=1)
        self.btn_three.grid(row=5, column=2)
        self.btn_plus.grid(row=5, column=3)

        self.btn_zero.grid(row=6, column=0)
        self.btn_decimal.grid(row=6, column=1)
        self.btn_clear.grid(row=6, column=2)
        self.btn_equal_to.grid(row=6, column=3)

    def get_value(self, val):
        old_value = self.result_str.get()
        new_value = self.result_str.get() + val
        self.result_str.set(new_value)
        self.operation_str.set('')

    def get_result(self):
        try:
            data = self.result_str.get()
            result = eval(data)
            self.operation_str.set(data)
            self.result_str.set(result)
        except ZeroDivisionError:
            messagebox.showerror("Division Error!", "Cannot be divided by zero.")
        except:
            messagebox.showerror("Wrong Input", "Please provide the correct input!")

    def set_all_clear(self):
        self.operation_str.set('')
        self.result_str.set('')

    def clear(self):
        old_value = self.result_str.get()
        new_value = old_value[0:len(old_value)-1]
        self.result_str.set(new_value)
        self.operation_str.set('')


root_window = tkinter.Tk()
my_calc = Calculator(root_window)
root_window.mainloop()


