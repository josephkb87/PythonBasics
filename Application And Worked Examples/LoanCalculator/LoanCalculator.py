# import Tkinter Module - used to create GUI- standard interface to Tk Gui Toolkit
from tkinter import *  # (*) imports whole module


# create a user defined class named: Loan calculator which holds its own
# data members and member functions

def getMonthlyPayment(loanAmount, monthlyInterestRate, numberofYears):
    monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberofYears * 12))
    return monthlyPayment


class LoanCalculator:
    def __init__(self):  # This is a special method in python class-constructor of a python_class
        window = Tk()  # creates a window to house the calculator bits
        window.title("Loan Calculator")  # sets the title
        window.configure(background="light green")  # sets bg colour for window

        # Create input boxes: Label function creates a display box to take input
        # The grid method gives it a table like structure
        # Widgets are centered by default. Use sticky arguments to change:N.S.E.W
        Label(window, font='Helvetica 12 bold', bg="light green", text="Annual Interest Rate").grid(row=1, column=1,
                                                                                                    sticky=W)
        Label(window, font='Helvetica 12 bold', bg="light green", text="Number of Years").grid(row=2, column=1,
                                                                                               sticky=W)
        Label(window, font='Helvetica 12 bold', bg="light green", text="Loan Amount").grid(row=3, column=1, sticky=W)
        Label(window, font='Helvetica 12 bold', bg="light green", text="Monthly Payment").grid(row=4, column=1,
                                                                                               sticky=W)
        Label(window, font='Helvetica 12 bold', bg="light green", text="Total Payment").grid(row=5, column=1, sticky=W)

        # Create objects: first 3 objects to take inputs using entry() function

        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar, justify=RIGHT).grid(row=1, column=2)

        self.numberofYearsVar = StringVar()
        Entry(window, textvariable=self.numberofYearsVar, justify=RIGHT).grid(row=2, column=2)

        self.loanAmountVar = StringVar()
        Entry(window, textvariable=self.loanAmountVar, justify=RIGHT).grid(row=3, column=2)

        self.monthlyPaymentVar = StringVar()
        Label(window, font='Helvetica 12 bold', bg="light green",
              textvariable=self.monthlyPaymentVar).grid(row=4, column=2, sticky=E)

        self.totalPaymentVar = StringVar()
        Label(window, font='Helvetica 12 bold', bg="light green",
              textvariable=self.totalPaymentVar).grid(row=5, column=2, sticky=E)

        # Create button to calculate payment. When button is clicked it will call the compute payment function

        Button(window, text="Compute Payment", bg="red", fg="white", font='Helvetica 14 bold',
               command=self.computePayment).grid(row=6, column=2, sticky=E)
        Button(window, text="Clear", bg="blue", fg="white", font='Helvetica 14 bold',
               command=self.delete_all).grid(row=6, column=8, padx=20, pady=20, sticky=E)

        window.mainloop()  # The mainloop () function is used to run the application program.

        # Create function to compute total payment

    def computePayment(self):
        monthlyPayment = getMonthlyPayment(
            float(self.loanAmountVar.get()),
            float(self.annualInterestRateVar.get()) / 1200,
            int(self.numberofYearsVar.get()))

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
                       * int(self.numberofYearsVar.get())

        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    def delete_all(self):
        self.monthlyPaymentVar.set("")
        self.loanAmountVar.set("")
        self.annualInterestRateVar.set("")
        self.numberofYearsVar.set("")
        self.totalPaymentVar.set("")

    # Call the class to run the program
