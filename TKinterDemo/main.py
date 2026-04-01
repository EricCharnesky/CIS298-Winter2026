# bing tkinter tutorial

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np


age = 0
desired_retirement_age = 0
mattress_money = 0
bank_money = 0
bonds_money = 0
stocks_money = 0
year = 0

balances = []


rate_of_returns_bonds = []
rate_of_returns_stocks = []

with open("BondsAndStocksAnnualReturn.csv") as data:
    lines = data.readlines()
    for index in range(1, len(lines)):
        tokens = lines[index].split(',')
        rate_of_returns_stocks.append(float(tokens[1][:-1])/100)
        rate_of_returns_bonds.append(float(tokens[2].strip()[:-1])/100)


# Create a button widget
def on_start_click():
    global age
    global desired_retirement_age
    global mattress_money
    global bank_money
    global bonds_money
    global stocks_money


    age_text_box.config(state='disabled')
    retirement_age_text_box.config(state='disabled')


    age = int(age_text_box.get("1.0", "end-1c"))
    age_text_box.delete("1.0", "end")

    desired_retirement_age = int(retirement_age_text_box.get("1.0", "end-1c"))
    retirement_age_text_box.delete("1.0", "end")

    mattress_money += float(mattress_text_box.get("1.0", "end-1c"))
    mattress_text_box.delete("1.0", "end")
    mattress_label.config(text="Enter how much you are adding to your mattress this year")

    bank_money += float(bank_text_box.get("1.0", "end-1c"))
    bank_text_box.delete("1.0", "end")
    bank_label.config(text="Enter how much you are adding to the bank this year")

    bonds_money += float(bonds_text_box.get("1.0", "end-1c"))
    bonds_text_box.delete("1.0", "end")
    bonds_label.config(text="Enter how much you are adding to bonds this year")

    stocks_money += float(stocks_text_box.get("1.0", "end-1c"))
    stocks_text_box.delete("1.0", "end")
    stocks_label.config(text="Enter how much you are adding to stocks this year")

    button.config(text="Move to next year")
    button.config(command=on_next_year_click)

    global balances
    balances.append(sum([mattress_money, bank_money, bonds_money, stocks_money]))

    display_label.config(text=f"Current Age:{age}\nMattress: ${mattress_money:.2f}\nBank: ${bank_money:.2f}\nBonds: ${bonds_money:.2f}\nStocks: ${stocks_money:.2f}\n")

def on_next_year_click():
    global year
    global age
    global desired_retirement_age
    global mattress_money
    global bank_money
    global bonds_money
    global stocks_money

    year += 1

    mattress = mattress_text_box.get("1.0", "end-1c")
    if mattress:
        mattress_money += float(mattress)
        mattress_text_box.delete("1.0", "end")

    bank = bank_text_box.get("1.0", "end-1c")
    if bank:
        bank_money += float(bank)
        bank_text_box.delete("1.0", "end")

    bonds = bonds_text_box.get("1.0", "end-1c")
    if bonds:
        bonds_money += float(bonds)
        bonds_text_box.delete("1.0", "end")

    stocks = stocks_text_box.get("1.0", "end-1c")
    if stocks:
        stocks_money += float(stocks)
        stocks_text_box.delete("1.0", "end")

    bank_money *= 1.02
    bonds_money *= (1 + rate_of_returns_bonds[year])
    stocks_money *= (1 + rate_of_returns_stocks[year])

    global balances
    balances.append(sum([mattress_money, bank_money, bonds_money, stocks_money]))

    if age+year == desired_retirement_age:
        button.config(state='disabled')
        button.config(text="all done")

        fig = Figure(figsize=(8, 4), dpi=100)
        ax = fig.add_subplot(111)

        # Simulate long X-axis data
        x = range(age, desired_retirement_age+1)
        y = balances

        ax.plot(x, y)
        ax.set_xlabel("Age")
        ax.set_ylabel("Retirement Savings")

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    display_label.config(text=f"Current Age:{age+year}\nMattress: ${mattress_money:.2f}\nBank: ${bank_money:.2f}\nBonds: ${bonds_money:.2f}\nStocks: ${stocks_money:.2f}\n")


# Create the main window
window = tk.Tk()
window.title("Retirement Calculator App")


display_label = tk.Label(window, text="")
display_label.pack()

# Create a label widget
label = tk.Label(window, text="Enter your age")
label.pack()

age_text_box = tk.Text(window, height=1, width=10)
age_text_box.pack()

label2 = tk.Label(window, text="Enter your desired retirement age")
label2.pack()

retirement_age_text_box = tk.Text(window, height=1, width=10)
retirement_age_text_box.pack()

mattress_label = tk.Label(window, text="Enter the money you have saved under your mattress")
mattress_label.pack()

mattress_text_box = tk.Text(window, height=1, width=10)
mattress_text_box.pack()

bank_label = tk.Label(window, text="Enter the money you have saved in your bank")
bank_label.pack()

bank_text_box = tk.Text(window, height=1, width=10)
bank_text_box.pack()

bonds_label = tk.Label(window, text="Enter the money you have saved in bonds")
bonds_label.pack()

bonds_text_box = tk.Text(window, height=1, width=10)
bonds_text_box.pack()

stocks_label = tk.Label(window, text="Enter the money you have saved in stocks")
stocks_label.pack()

stocks_text_box = tk.Text(window, height=1, width=10)
stocks_text_box.pack()


button = tk.Button(window, text="Start", command=on_start_click)
button.pack()


# Run the application
window.mainloop()