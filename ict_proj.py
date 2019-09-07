from tkinter import Tk , StringVar , ttk
from tkinter import *
import time
import datetime

val = Tk()
val.title("Real Time Currency Converter")
val.geometry('1000x300+0+0')
val.configure(background = 'black')

LeftMainFrame = Frame(val, width=660, height=400, bd=8, relief='raise')
LeftMainFrame.pack(side=LEFT)
RightMainFrame = Frame(val, width=200, height=400, bd=8, relief='raise')
RightMainFrame.pack(side=RIGHT)

DateofOrder = StringVar()
value0 = StringVar()
convert = DoubleVar()
currency = DoubleVar()

EntCurrency = Entry(LeftMainFrame,font=('arial',20,'bold'), textvariable = convert, bd=2,width=28, justify = 'center')
EntCurrency.grid(row=0,column=1)
'''
lblRupees = Label(LeftMainFrame,font=('arial',20,'bold'), text='Rupees equals', padx=2 , pady=2, bd=2, fg="black", width=18)
lblRupees.grid(row=0, coloumn=2, sticky=W)

box = ttk.Combobox(LeftMainFrame, textvariable=value0, state='readonly', font=('arial',20,'bold'),width=20)
box['values'] = ('','USA', 'Nepali', 'Australian', 'Canadian', 'Indian') 
box.current(0)
box.grid(row=4, column=2)

lblCurrency = Label(LeftMainFrame,font=('arial',20,'bold'), textvariable=currency, bd=2, width=25,bg='white',pady=2,padx=2, relief='sunkeen')
lblCurrency.grid(row=4,column=1)

lblDateofOrder= Label(RightMainFrame,font=('arial',20,'bold'), textvariable=DateofOrder, bd=2, width=12, fg='black',pady=2,padx=2, justify='center')
lblDateofOrder.grid(row=0,coloum=0, sticky=W)



'''


val.mainloop()