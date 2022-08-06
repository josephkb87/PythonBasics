from tkinter import * #imports whole design module from tkinter#

class CurrencyConverter:  # this creates our class#
    def __init__(self):   #This is a special method in python#
        window = Tk()       #Creates application window#
        window.title("CurrencyConverter")       #Adds title  to application window#
        window.configure(bg = "blue")           #Adds background to application window#

        #This adds label widgets to application window#
        Label(window, font = "Helvetica 12 bold", bg = "yellow", text = "Amount to convert").grid(row =1, column = 1, sticky = W)
        Label(window, font = "Helvetica 12 bold", bg = "white", text = "Conversion Rate").grid(row=2, column=1, sticky=W)
        Label(window, font = "Helvetica 12 bold", bg = "white", text = "Converted Amount").grid(row=3, column=1, sticky=W)

        #This creates and adds entry functions to our app#
        self.amounttoConvertVar = StringVar()
        Entry(window, textvariable = self.amounttoConvertVar, justify = RIGHT).grid(row = 1, column = 2)
        self.conversionRateVar = StringVar()
        Entry(window, textvariable = self.conversionRateVar, justify = RIGHT).grid(row = 2, column = 2)
        self.convertedAmountVar = StringVar()
        lblConvertedAmount = Label(window, font = "Helvetica 12 bold", bg ="red", textvariable = self.convertedAmountVar). grid(row = 3, column = 2, sticky = E)

        #create convert and clear buttons.When clicked they will call their respective functions.
        btConvertedAmount = Button(window, text = "Convert", font = "Helvetica 12 bold", bg = "green", fg = "white", command = self.ConvertedAmount).grid(row = 4, column = 2, sticky = E)
        btdelete_all = Button(window, text = "Clear", font = "Helvetica 12 bold", bg = "yellow", fg = "white", command = self.delete_all).grid(row = 4, column = 6, padx = 25, pady = 25, sticky = E)

        window.mainloop() #Runs the application program#

      #Function to do conversion.Stores inputs and performs conversion#
    def ConvertedAmount(self):
        amt = float(self.conversionRateVar.get())
        convertedAmountVar = float(self.amounttoConvertVar.get())*amt
        self.convertedAmountVar.set(format(convertedAmountVar, '10.2f'))

      #Function to clear inputs
    def delete_all(self):
        self.amounttoConvertVar.set("")
        self.conversionRateVar.set("")
        self.convertedAmountVar.set("")

CurrencyConverter()
