import tkinter as tk

def button_click(value):
    entry.insert(tk.END, value)

def clear_entry():
    entry.delete("1.0", tk.END)

def calculate():
    try:
        expression = entry.get("1.0", tk.END).strip().replace("\n", "")
        result = eval(expression)
        if isinstance(result, float):
            result = round(result, 6)
            result = int(result) if result.is_integer() else result
        clear_entry()
        entry.insert(tk.END, str(result))
    except Exception:
        clear_entry()
        entry.insert(tk.END, "ERROR")

window = tk.Tk()
window.geometry("420x420")
window.title("Calculator Tkinter")
window.config(background="black")
entry = tk.Text(window,height=3, selectbackground="grey", selectforeground="blue", font=("Arial", 20))
entry.pack(padx=20, pady=20)

buttonFrame = tk.Frame(window, background="black")
buttonFrame.columnconfigure(0, weight=1)
buttonFrame.columnconfigure(1, weight=1)
buttonFrame.columnconfigure(2, weight=1)
buttonFrame.columnconfigure(3, weight=1)
buttonFrame.config(background="black")

btnbg = "#2a2b2b"
btnfg1 = "white"
btnfg2 = "orange"

btn7 = tk.Button(buttonFrame, text="7", font=("Arial", 16), background=btnbg, foreground=btnfg1, command=lambda: button_click("7"))
btn7.grid(row=0, column=0, sticky=tk.W+tk.E)

btn8 = tk.Button(buttonFrame, text="8", font=("arial", 16), background=btnbg, foreground=btnfg1, command=lambda: button_click("8"))
btn8.grid(row=0, column=1, sticky=tk.W+tk.E)

btn9 = tk.Button(buttonFrame, text="9", font=("Arial", 16), background=btnbg, foreground=btnfg1, command=lambda: button_click("9"))
btn9.grid(row=0, column=2, sticky=tk.W+tk.E)

btnd = tk.Button(buttonFrame, text="/", font=("Arial", 16), background=btnbg, foreground=btnfg2, command=lambda: button_click("/"))
btnd.grid(row=0, column=3, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonFrame, text="4", font=("Arial", 16), background=btnbg, foreground=btnfg1, command=lambda: button_click("4"))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonFrame, text="5", font=("Arial", 16), background=btnbg, foreground=btnfg1, command=lambda: button_click("5"))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonFrame, text="6", font=("Arial", 16), background=btnbg, foreground=btnfg1, command=lambda: button_click("6"))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

btns = tk.Button(buttonFrame, text="-", font=("Arial", 16), background=btnbg, foreground=btnfg2, command=lambda: button_click("-"))
btns.grid(row=1, column=3, sticky=tk.W+tk.E)

btn1 = tk.Button(buttonFrame, text="1", font=("Arial", 16), background=btnbg, foreground=btnfg1, command=lambda: button_click("1"))
btn1.grid(row=2, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonFrame, text="2", font=("Arial", 16), background=btnbg, foreground=btnfg1, command=lambda: button_click("2"))
btn2.grid(row=2, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonFrame, text="3", font=("Arial", 16), background=btnbg, foreground=btnfg1, command=lambda: button_click("3"))
btn3.grid(row=2, column=2, sticky=tk.W+tk.E)

btnm = tk.Button(buttonFrame, text="x", font=("Arial", 16), background=btnbg, foreground=btnfg2, command=lambda: button_click("*"))
btnm.grid(row=2, column=3, sticky=tk.W+tk.E)

btnc = tk.Button(buttonFrame, text="C" ,font=("Arial", 16), background=btnbg, foreground=btnfg1, command=clear_entry)
btnc.grid(row=3, column=0, sticky=tk.W+ tk.E)

btn0 = tk.Button(buttonFrame, text="0" ,font=("Arial", 16), background=btnbg, foreground=btnfg1, command=lambda: button_click("0"))
btn0.grid(row=3, column=1, sticky=tk.W+ tk.E)

btnp = tk.Button(buttonFrame, text="." ,font=("Arial", 16), background=btnbg, foreground=btnfg1, command=lambda: button_click("."))
btnp.grid(row=3, column=2, sticky=tk.W+ tk.E)

btna = tk.Button(buttonFrame, text="+", font=("Arial", 16), background=btnbg, foreground=btnfg2, command=lambda: button_click("+"))
btna.grid(row=3, column=3, sticky=tk.W+tk.E)

buttonFrame.pack(fill="x")

btneq = tk.Button(window, text="=", font=("Arial", 22), background="orange", foreground="white", command=calculate)
btneq.pack(padx=10, pady=10)

window.bind("<Return>", lambda event: calculate())

window.mainloop()