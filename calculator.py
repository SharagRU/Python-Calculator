import tkinter as tk

# -------------------------
# Calculator Window
# -------------------------
root = tk.Tk()
root.title("Calculator")
root.geometry("360x560")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

expression = ""


# -------------------------
# Functions
# -------------------------
def press(value):
    global expression
    expression += str(value)
    display_var.set(expression)


def clear():
    global expression
    expression = ""
    display_var.set("0")


def backspace():
    global expression
    expression = expression[:-1]
    if expression == "":
        display_var.set("0")
    else:
        display_var.set(expression)


def equal():
    global expression
    try:
        result = str(eval(expression))
        display_var.set(result)
        expression = result
    except:
        display_var.set("0")
        expression = ""


def plus_minus():
    global expression
    try:
        if expression:
            expression = str(eval(f"-({expression})"))
            display_var.set(expression)
    except:
        pass


def percentage():
    global expression
    try:
        expression = str(eval(expression) / 100)
        display_var.set(expression)
    except:
        pass


# -------------------------
# Keyboard Support
# -------------------------
def key_press(event):
    key = event.keysym

    if key in "0123456789":
        press(key)

    elif key in ["plus", "KP_Add"]:
        press("+")

    elif key in ["minus", "KP_Subtract"]:
        press("-")

    elif key in ["asterisk", "KP_Multiply"]:
        press("*")

    elif key in ["slash", "KP_Divide"]:
        press("/")

    elif key == "period":
        press(".")

    elif key in ["Return", "KP_Enter"]:
        equal()

    elif key == "BackSpace":
        backspace()

    elif key == "Escape":
        clear()


root.bind("<Key>", key_press)


# -------------------------
# Display
# -------------------------
display_var = tk.StringVar()
display_var.set("0")

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Segoe UI", 28),
    justify="right",
    bd=0,
    bg="#1e1e1e",
    fg="white",
    insertbackground="white"
)

display.pack(fill="both", ipadx=8, ipady=30, padx=12, pady=12)


# -------------------------
# Button Style
# -------------------------
button_font = ("Segoe UI", 18)

number_bg = "#2d2d2d"
operator_bg = "#ff9500"
special_bg = "#444444"

number_fg = "white"
operator_fg = "white"

active_num = "#3b3b3b"
active_op = "#ffb347"

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(expand=True, fill="both")


def create_button(text, row, col, command,
                  bg=number_bg,
                  fg=number_fg):

    btn = tk.Button(
        frame,
        text=text,
        command=command,
        font=button_font,
        bg=bg,
        fg=fg,
        bd=0,
        activebackground=active_op if bg == operator_bg else active_num,
        activeforeground="white",
        relief="flat",
        cursor="hand2"
    )

    btn.grid(row=row,
             column=col,
             sticky="nsew",
             padx=4,
             pady=4)

    return btn


# -------------------------
# Layout
# -------------------------
buttons = [

    ("%", percentage, special_bg),
    ("/",  press("/"), special_bg),
    ("C", clear, special_bg),
    ("⌫",  backspace, operator_bg),

    ("7", lambda: press("7"), number_bg),
    ("8", lambda: press("8"), number_bg),
    ("9", lambda: press("9"), number_bg),
    ("*", lambda: press("*"), operator_bg),

    ("4", lambda: press("4"), number_bg),
    ("5", lambda: press("5"), number_bg),
    ("6", lambda: press("6"), number_bg),
    ("-", lambda: press("-"), operator_bg),

    ("1", lambda: press("1"), number_bg),
    ("2", lambda: press("2"), number_bg),
    ("3", lambda: press("3"), number_bg),
    ("+", lambda: press("+"), operator_bg),

    ("+/-", plus_minus, special_bg),
    ("0", lambda: press("0"), number_bg),
    (".", lambda: press("."), number_bg),
    ("=", equal, operator_bg),

]

row = 0
col = 0

for text, command, color in buttons:
    create_button(text, row, col, command, color)

    col += 1

    if col > 3:
        col = 0
        row += 1


# -------------------------
# Grid Configuration
# -------------------------
for i in range(5):
    frame.rowconfigure(i, weight=1)

for i in range(4):
    frame.columnconfigure(i, weight=1)


# -------------------------
# Run
# -------------------------
root.mainloop()