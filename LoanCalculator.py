# import Tkinter Module - used to create GUI- standard interface to Tk Gui Toolkit
from tkinter import * #(*) imports whole module

#create a user defined class named: Loan calculator which holds it's own
# data memebers and member functions

class LoanCalculator:
    def __init__(self):  #This is a special method in python class-constroctor of a python_class
        window = Tk() #creates a window to house the calculator bits
        window.title("Loan Calculator") #sets the title
        window.configure(background= "light green") #sets bg colour for window

        # Create input boxes:Label function creates a diplay box to take input
        # The grid method gives it a table like structure
        #Widgets are centred by default.Use sticky arguments to change: N.S.E.W
        Label(window, font = 'Helvetica 12 bold',bg ='light green', text= "Annual Interest Rate", column = 1, sticky = W)

