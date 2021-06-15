from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

 #определяем калькулятор
root = Tk()
root.title("Калькулятор")

#функция калькулятора
def add_digit(var):
    value = calc.get()
    if value[0] == "0" and len(value) == 1: #если в начале стоит 0, то она обрезается, len нужен, чтобы нолик не удалялся в начале какой либо операции
        value = value[1:]
    calc.delete(0, tk.END)
    calc.insert(0, value + var)

def add_oper(oper):
    value = calc.get()
    if value[-1] in "-+/*": #замена операции, если водят другую операцию последней
        value = value[:-1]
    elif "+" in value or "-" in value or "/" in value or "*" in value: #условие для сложения значений, если мы добавляем еще одну оперпцию
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + oper)

def calculate():
    value = calc.get()
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except ZeroDivisionError:
        messagebox.showinfo("Ошибка!", "Нельзя делить на ноль!")
        calc.insert(0, "0")

def add_del(del1):
    calc.delete(0, tk.END)
    calc.insert(0, "0")


#функция для кнопок
def type_digit(var):
    return ttk.Button(text=var, command=lambda : add_digit(var))

def type_oper(oper):
    return ttk.Button(text=oper, command=lambda : add_oper(oper))

def type_del(del1):
    return ttk.Button(text=del1, command=lambda : add_del(del1))

def type_equal(eql):
    return ttk.Button(text=eql, command=calculate)

#окно ввода
calc = ttk.Entry(root, justify=tk.RIGHT, font="Arial 18")
calc.insert(0, "0")
calc.grid(row=0, column=0, columnspan=4, stick="we")


#кнопки ввода
type_digit("1").grid(row=1, column=0, stick="wens")
type_digit("2").grid(row=1, column=1, stick="wens")
type_digit("3").grid(row=1, column=2, stick="wens")
type_digit("4").grid(row=2, column=0, stick="wens")
type_digit("5").grid(row=2, column=1, stick="wens")
type_digit("6").grid(row=2, column=2, stick="wens")
type_digit("7").grid(row=3, column=0, stick="wens")
type_digit("8").grid(row=3, column=1, stick="wens")
type_digit("9").grid(row=3, column=2, stick="wens")
type_digit("0").grid(row=4, column=0, stick="wens")
type_oper("+").grid(row=1, column=3, stick="wens")
type_oper("-").grid(row=2, column=3, stick="wens")
type_oper("/").grid(row=3, column=3, stick="wens")
type_oper("*").grid(row=4, column=3, stick="wens")
type_equal("=").grid(row=4, column=2, stick="wens")
type_del("C").grid(row=4, column=1, stick="wens")

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)

root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)

root.mainloop()