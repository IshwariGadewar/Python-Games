import tkinter

FONT = ("Arial",15,"normal")

window = tkinter.Tk()
window.title("Mile to Km Converter")
# window.minsize(width=300,height=300)
window.config(padx=20,pady=20)

#entry
mile_input = tkinter.Entry(width=10)
mile_input.grid(row=0,column=1)
mile_lable = tkinter.Label(text="Miles",font=FONT)
mile_lable.grid(row=0,column=2)

text = tkinter.Label(text="is equal to",font=FONT)
text.grid(row=1,column=0)
outout = tkinter.Label(font=FONT)
outout.grid(row=1,column=1)
km_lable = tkinter.Label(text="Km",font=FONT)
km_lable.grid(row=1,column=2)

def calcu():
    miles = float(mile_input.get())
    outout["text"] = miles*1.609

cal = tkinter.Button(width=10,text="Calculate",font=FONT,command=calcu)
cal.grid(row=2,column=1)

window.mainloop()