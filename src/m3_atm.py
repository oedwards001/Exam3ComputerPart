import tkinter as tk

###############################################################################
# Done: 1. (2 pts)
#
#   The todos in this module are in one comment because you will be modifying
#   the same bit of code each time. Here you will create a basic ATM
#   application that allows a user to withdraw funds and deposit funds
#
#   For this _todo_, you will create a window with the title "ATM" and call its
#   mainloop() method so it runs.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# Done: 2. (3 pts)
#
#   For this _todo_, you will create an area where the user's current balance
#   is displayed. There should be a label that says "Current Balance ($):" and
#   below it another label that has the dollar amount of their current balance
#   displayed. For the purposes of this problem, we will assume that all users
#   start out with 1000 dollars in their account. So, this label should start
#   out with "1000" as its text.
#
#   All of the elements on this window should be centered.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# Done: 3 (3 pts)
#
#   For this _todo_, create two more labels: one that says "Amount ($):" and
#   another that starts out empty beneath it. This is where the user's amount
#   that they will either withdraw or deposit will display.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# Done: 4. (7 pts)
#
#   For this _todo_, you will create all the buttons that the user needs:
#
#       - One for each digit 0-9
#       - A withdrawal button
#       - A deposit button
#
#   They should be in the standard configuration for a numberpad (see the
#   images in the README file on GitHub). Each button is 75px by 75px.
#
#   HINT: I used a frame to surround the buttons and grid for this.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# Done: 5. (10 pts)
#
#   For this _todo_, using the command keyword on each button to have each
#   number button type that digit in the amount label above (just like you
#   would if you were typing in an amount). Pressing each button should add
#   that number to end of the text in the label.
#
#   HINT: I found that the easiest way to accomplish this was to use a
#   different handler for each button.
#
#   You also need a handler for the withdrawal and deposit buttons.
#
#   The withdrawal button should subtract the amount typed into the amount box
#   from the user's current balance. It should clear the amount label and
#   update the current balance label.
#
#   The deposit button should add the amount typed into the amount box to the
#   user's current balance. It should also clear the amount label and update
#   the current balance label.
#
#   Remember that, for these handlers, you will need to convert the strings in
#   the label's to floats before you do your calculations.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# Done: 5. (3 pts)
#
#   For this _todo_, bind the window to any keypress so that if the user types
#   a number, it also types that number into the amount label. Remember, you
#   can use isdigit() to check if the key pressed is a digit.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
window = tk.Tk()

window.title("ATM")

CurrentBalanceLabel = tk.Label(master = window, text = "Current Balance ($):")
CurrentBalanceLabel.pack()

DollarLabel = tk.Label(master = window, text = float(1000))
DollarLabel.pack()

DollarAmountLabel = tk.Label(master = window, text = "Amount($):")
DollarAmountLabel.pack()

ChangeableAmountLabel = tk.Label(master = window, text = "")
ChangeableAmountLabel.pack()

frame = tk.Frame(master = window)
frame.pack()

frame.rowconfigure([0, 1, 2, 3], weight = 1, minsize = 75)
frame.columnconfigure([0, 1, 2], weight = 1, minsize = 75)

def button1_handler():
    ChangeableAmountLabel["text"] = ChangeableAmountLabel["text"] + "1"

button1 = tk.Button(master = frame, command = button1_handler, text = "1")
button1.grid(row = 0, column = 0, sticky = "nsew")

def button2_handler():
    ChangeableAmountLabel["text"] = ChangeableAmountLabel["text"] + "2"

button2 = tk.Button(master = frame, command = button2_handler, text = "2")
button2.grid(row = 0, column = 1, sticky = "nsew")

def button3_handler():
    ChangeableAmountLabel["text"] = ChangeableAmountLabel["text"] + "3"

button3 = tk.Button(master = frame, command = button3_handler, text = "3")
button3.grid(row = 0, column = 2, sticky = "nsew")

def button4_handler():
    ChangeableAmountLabel["text"] = ChangeableAmountLabel["text"] + "4"

button4 = tk.Button(master = frame, command = button4_handler, text = "4")
button4.grid(row = 1, column = 0, sticky = "nsew")

def button5_handler():
    ChangeableAmountLabel["text"] = ChangeableAmountLabel["text"] + "5"

button5 = tk.Button(master = frame, command = button5_handler, text = "5")
button5.grid(row = 1, column = 1, sticky = "nsew")

def button6_handler():
    ChangeableAmountLabel["text"] = ChangeableAmountLabel["text"] + "6"

button6 = tk.Button(master = frame, command = button6_handler, text = "6")
button6.grid(row = 1, column = 2, sticky = "nsew")

def button7_handler():
    ChangeableAmountLabel["text"] = ChangeableAmountLabel["text"] + "7"

button7 = tk.Button(master = frame, command = button7_handler, text = "7")
button7.grid(row = 2, column = 0, sticky = "nsew")

def button8_handler():
   ChangeableAmountLabel ["text"] = ChangeableAmountLabel["text"] + "8"

button8 = tk.Button(master = frame, command = button8_handler, text = "8")
button8.grid(row = 2, column = 1, sticky = "nsew")

def button9_handler():
    ChangeableAmountLabel["text"] = ChangeableAmountLabel["text"] + "9"

button9 = tk.Button(master = frame, command = button9_handler, text = "9")
button9.grid(row = 2, column = 2, sticky = "nsew")

def button0_handler():
    ChangeableAmountLabel["text"] = ChangeableAmountLabel["text"] + "0"

button0 = tk.Button(master = frame, command = button0_handler, text = "0")
button0.grid(row = 3, column = 1, sticky = "nsew")

def withdrawalbutton_handler():
    DollarLabel = 0
    DollarLabel["text"] = DollarLabel["text"] - ChangeableAmountLabel["text"]
    ChangeableAmountLabel["text"] = ""

Withdrawbutton = tk.Button(master = frame, command = withdrawalbutton_handler, text = "Withdraw")
Withdrawbutton.grid(row = 3, column = 0, sticky = "nsew")

def depositbutton_handler():
    DollarLabel = 0
    DollarLabel = DollarLabel + ChangeableAmountLabel
    ChangeableAmountLabel["text"] = ""

depositbutton = tk.Button(master = frame, command = depositbutton_handler, text = "Deposit")
depositbutton.grid(row = 3, column = 2, sticky = "nsew")

def key_handler(event):
    if event.char.isdigit():
        ChangeableAmountLabel["text"] = ChangeableAmountLabel["text"] + event.char

window.bind("<Key>", key_handler)

window.mainloop()