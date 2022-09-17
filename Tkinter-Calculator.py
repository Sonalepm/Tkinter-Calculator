import ast
from tkinter import *


root = Tk()
root.title("Calculator")

entry = Entry(root)
entry.grid(rowspan=2, columnspan=10, sticky=W + E)
i = 0


def get_variable(num):
    global i
    entry.insert(i, num)
    i += 1


def clear_all():
    entry.delete(0, END)


def undo():
    string = entry.get()
    if len(string):
        new_string = string[:-1]
        clear_all()
        entry.insert(0, new_string)
    else:
        clear_all()
        entry.insert(0, "Error")


def get_operator(op):
    global i
    op_len = len(op)
    entry.insert(i,op)
    i += op_len


def calculate():
    string = entry.get()
    try:
        inp = compile(ast.parse(string,mode='eval'),'',mode='eval')
        #inp= parser.exp(string).compile()
        result = eval(inp)
        clear_all()
        entry.insert(0, result)
    except:
         clear_all()
         entry.insert(0, "ERROR")


# Adding button to calculator
Button(root, text="1", command=lambda: get_variable(1)).grid(row=2, column=0)
Button(root, text="2", command=lambda: get_variable(2)).grid(row=2, column=1)
Button(root, text="3", command=lambda: get_variable(3)).grid(row=2, column=2)
Button(root, text="4", command=lambda: get_variable(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda: get_variable(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda: get_variable(6)).grid(row=3, column=2)
Button(root, text="7", command=lambda: get_variable(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda: get_variable(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda: get_variable(9)).grid(row=4, column=2)
Button(root, text="0", command=lambda: get_variable(0)).grid(row=5, column=0)
Button(root, text="AC", command=lambda: clear_all()).grid(row=5, column=1)
Button(root, text="=", command=lambda: calculate()).grid(row=5, column=2)
Button(root, text="+", command=lambda: get_operator('+')).grid(row=2, column=4)
Button(root, text="-", command=lambda: get_operator('-')).grid(row=3, column=4)
Button(root, text="*", command=lambda: get_operator('*')).grid(row=4, column=4)
Button(root, text="/", command=lambda: get_operator('/')).grid(row=5, column=4)
Button(root, text="pi", command=lambda: get_operator('*3.14')).grid(row=2, column=5)
Button(root, text="%", command=lambda: get_operator('%')).grid(row=3, column=5)
Button(root, text="(", command=lambda: get_operator('(')).grid(row=4, column=5)
Button(root, text=")", command=lambda: get_operator(')')).grid(row=5, column=5)
Button(root, text="exp", command=lambda: get_operator('^')).grid(row=3, column=6)
Button(root, text="x!", command=lambda: get_operator('!')).grid(row=4, column=6)
Button(root, text="x^2", command=lambda: get_operator('^2')).grid(row=5, column=6)
Button(root, text="<---", command=lambda: undo()).grid(row=2, column=6)

root.mainloop()
