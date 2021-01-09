#import python module TKinter
import tkinter as tk #Let tkinker use the value tk
import tkinter.messagebox
from tkinter import *


expression = ""

main_window = tk.Tk()  # create a window

#entry widget always takes a stringvar to let tkinter know your taking a string input
inputed_text = tk.StringVar()

#configure the main window panel to be green
main_window.configure(bg = 'green')

#giving my app a title
main_window.title("Calculator")

#structuring the window length
main_window.geometry("370x295")

#making sure the window stay the same 
main_window.resizable(0,0)

#declaring our function for the argument value or input data
def update_input(value):
    global expression
    expression = expression + str(value)
    inputed_text.set(expression)

#declaring our function for the delete button which delete all value
def delete_button():
    global expression
    expression =""
    inputed_text.set("")

#declaring our function for the clear button which clear a value at a time 
def clear_button():
    global expression
    expression = expression[:len(expression) - 1]
    inputed_text.set(expression)

#declaring our function for the Equal button to result in our final answer
def equal_2_sign():
    global expression
    
    try:
        result = str(eval(expression))
        inputed_text.set(result)
    except:
        inputed_text.set("Error")
        expression = ""



#Our entry field widget that takes the number inputed

#Use a width in the grid to fill the empty space

inputed_field = Entry(main_window, textvariable= inputed_text, width=55, borderwidth= 5, bg ="grey",justify ='right')
inputed_field.grid(row=0, column=0,columnspan=5,padx=15,pady=20)


#Making use of the button widget for the button on the calculator
#FIRST ROW of the calculator button widget 
#Making use of the grid to place the button widget by rows and columns

#Button no 7,8,9 and plus(+) all grid and taking a command
button_7 = Button(main_window,padx=25,pady=10,width=5,bg = "grey",fg ="black",text=" 7 ",
        command=lambda:update_input(7))

button_7.grid(row=1,column=0)

button_8 = Button(main_window,padx=25,pady=10,width=5,bg = "grey",fg ="black",text=" 8 ",
        command=lambda:update_input(8))

button_8.grid(row=1,column=1)

button_9 = Button(main_window,padx=25,pady=10,width=5,bg = "grey",fg ="black",text=" 9 ",
        command=lambda:update_input(9))

button_9.grid(row=1,column=2)

button_plus = Button(main_window,padx=25,pady=10,width=5,bg = "grey",fg ="black",text="+",
        command=lambda:update_input("+"))

button_plus.grid(row=1,column=3)

#SECOND ROW of the calculator button widget

#Button no 4,5,6 and minus(-) all in grid and taking a command

button_4 = Button(main_window,padx=25,pady=10,width=5,bg = "grey",fg ="black",text=" 4 ",
        command=lambda:update_input(4))

button_4.grid(row=2,column=0)

button_5 = Button(main_window,padx=25,pady=10,width=5,bg = "grey",fg ="black",text=" 5 ",
        command=lambda:update_input(5))

button_5.grid(row=2,column=1)

button_6 = tk.Button(main_window,padx=25,pady=10,width=5,bg = "grey",fg ="black",text=" 6 ",
        command=lambda:update_input(6))

button_6.grid(row=2,column=2)
        
button_minus = Button(main_window,padx=25,pady=10,width=5,bg = "grey",fg ="black",text=" - ",
        command=lambda:update_input("-"))

button_minus.grid(row=2,column=3)


#THIRD ROW of the calculator button widget

#Button no 1,2,3 and multiply(*) all grid and taking a command

button_1 = Button(main_window,padx=25,pady=10,width=5,bg = "grey",fg ="black",text=" 1 ",
        command=lambda:update_input(1))

button_1.grid(row=3,column=0)

button_2 = Button(main_window,padx=25,pady=10,width=5,bg = "grey",fg ="black",text=" 2 ",
        command=lambda:update_input(2))

button_2.grid(row=3,column=1)

button_3 = Button(main_window,padx=25,pady=10,width=5,bg = "grey",fg ="black",text=" 3 ",
        command=lambda:update_input(3))

button_3.grid(row=3,column=2)


button_multi = Button(main_window,padx=25,pady=10,width=5,bg = "grey",fg ="black",text=" * ",
        command=lambda:update_input("*"))

button_multi.grid(row=3,column=3)


#FOURTH ROW of the calculator button widget

#Button point,0,equal (=) & divide(/) all grid and taking a command

button_dot = Button(main_window,padx=25,pady=10,width=5,bg = "grey",fg ="black",text=" .",
        command=lambda:update_input("."))

button_dot.grid(row=5,column=0)

button_zero = Button(main_window,padx=25,pady=10,width=5,bg = "grey",fg ="black",text="0",
        command=lambda:update_input(0))

button_zero.grid(row=5,column=1)


button_equal = Button(main_window,padx=25,pady=10,width=5,bg = "grey",fg ="black",text="=",
        command=equal_2_sign)

button_equal.grid(row=5,column=2)

button_div = Button(main_window,padx=25,pady=10,width=5,bg = "grey",fg ="black",text="/",
        command=lambda:update_input("/"))

button_div.grid(row=5,column=3)

#FIRTH ROW of the calculator button widget

#Delete Button
button_del = Button(main_window,padx=5,pady=15,width=24,bg = "red",fg ="black",text=" DELETE ",
        command=delete_button)

#making use of the grid to place the button widget by rows and columns  
button_del.grid(row=6, column=0,columnspan=2)

#Clear Button
button_clear = Button(main_window,padx=5,pady=15, width=24,bg = "blue",fg ="black",text=" CLEAR ",
        command=clear_button)

button_clear.grid(row=6,column=2,columnspan=4)




main_window.mainloop() #display window while in loop



