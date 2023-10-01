import os
import sqlite3
import time
from tkinter import *
from tkinter import messagebox
from functools import partial


def window2():
    window1.destroy()
    global main, final 

    main = Tk()
    main.geometry("1550x750+0+0")
    main.title("Sheeshilog Billing System")

    number = StringVar()
    tapsilog = StringVar()
    tocilog = StringVar()
    cornedsilog = StringVar()
    bacsilog= StringVar()
    porksilog = StringVar()
    chicksilog = StringVar()

    coke = StringVar()
    sprite = StringVar()
    royal = StringVar()

    cost = StringVar()
    discount = StringVar()
    tax = StringVar()
    sub_total = StringVar()
    final = StringVar()

    # database
    table = sqlite3.connect("total_orders.db")
    table.execute('''CREATE TABLE IF NOT EXISTS ORDERS
    (ORDER_NUMBER,DATE TEXT,TIME TEXT,TAPSILOG TEXT,TOCILOG TEXT,CORNEDSILOG TEXT,BACSILOG TEXT,PORKSILOG TEXT,CHICKSILOG TEXT,COKE TEXT,SPRITE TEXT,ROYAL TEXT,COST TEXT,DISCOUNT TEXT,TAX TEXT,SUBTOTAL TEXT,TOTAL TEXT);''')
    table.commit()

    global order
    order = 1
    number.set(order)

    # default values to variables
    tapsilog.set(0)
    tocilog.set(0)
    cornedsilog.set(0)
    bacsilog.set(0)
    porksilog.set(0)
    chicksilog.set(0)
    coke.set(0)
    sprite.set(0)
    royal.set(0)
    discount.set(0)


    # GUI price list
    def price():
        priceWindow = Tk()
        priceWindow.geometry("620x600+0+0")
        priceWindow.title("Price List")

        priceList = LabelFrame(priceWindow,width = 400,height=800,relief=SUNKEN, text="Price List")
        priceList.pack(fill= "both", expand="yes", padx=20, pady=10)

    # label for foods
        label_Price_List = Label(priceList, font=('aria', 12, 'bold'), text="SILOG", fg="Black", bd=2, anchor ='w',justify='left')
        label_Price_List.grid(row=0, column=0,padx=25, pady=10)

        label_Price_List = Label(priceList, font=('aria', 12, 'bold'), text="PRICE", fg="Black", anchor='w',justify='left')
        label_Price_List.grid(row=0, column=3,padx=25, pady=10)

        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Tapsilog", fg="#784017", anchor='w',justify='left')
        label_Price_List.grid(row=1, column=0,padx=25, pady=5)
        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Php 120 ", fg="Black", anchor='w')
        label_Price_List.grid(row=1, column=3,padx=25, pady=5)

        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Tocilog", fg="#784017", anchor='w',justify='left')
        label_Price_List.grid(row=2, column=0,padx=25, pady=5)
        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Php 95 ", fg="Black", anchor='w')
        label_Price_List.grid(row=2, column=3,padx=25, pady=5)

        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Cornisilog", fg="#784017", anchor='w',justify='left')
        label_Price_List.grid(row=3, column=0,padx=25, pady=5)
        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Php 115 ", fg="Black", anchor='w')
        label_Price_List.grid(row=3, column=3,padx=25, pady=5)

        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Bacsilog", fg="#784017", anchor='w',justify='left')
        label_Price_List.grid(row=4, column=0,padx=25, pady=5)
        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Php 95", fg="Black", anchor='w')
        label_Price_List.grid(row=4, column=3,padx=25, pady=5)

        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Porksilog", fg="#784017", anchor='w',justify='left')
        label_Price_List.grid(row=5, column=0,padx=25, pady=5)
        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Php 120", fg="Black", anchor='w')
        label_Price_List.grid(row=5, column=3,padx=25, pady=5)

        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Chicksilog", fg="#784017", anchor='w',justify='left')
        label_Price_List.grid(row=6, column=0,padx=25, pady=5)
        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Php 115", fg="Black", anchor='w')
        label_Price_List.grid(row=6, column=3,padx=25, pady=5)

        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Adisilog", fg= "#784017", anchor='w',justify='left')
        label_Price_List.grid(row=7, column=0,padx=25, pady=5)
        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Php 120", fg="Black", anchor='w')
        label_Price_List.grid(row=7, column=3,padx=25, pady=5)

        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Longsilog", fg="#784017", anchor='w',justify='left')
        label_Price_List.grid(row=8, column=0,padx=25, pady=5)
        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Php 85", fg="Black", anchor='w')
        label_Price_List.grid(row=8, column=3,padx=25, pady=5)

     
    # label for drinks
        label_Price_List = Label(priceList, font=('aria', 12, 'bold'), text="DRINKS", fg="Black", bd=2, anchor ='w',justify='left')
        label_Price_List.grid(row=0, column=7,padx=25, pady=10)
        label_Price_List = Label(priceList, font=('aria', 12, 'bold'), text="PRICE", fg="Black", anchor='w',justify='left')
        label_Price_List.grid(row=0, column=9,padx=25, pady=10)

        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Coke", fg="#784017", anchor='w',justify='left')
        label_Price_List.grid(row=1, column=7,padx=25, pady=5)
        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Php 25", fg="Black", anchor='w')
        label_Price_List.grid(row=1, column=9,padx=25, pady=5)

        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Sprite", fg="#784017", anchor='w',justify='left')
        label_Price_List.grid(row=2, column=7,padx=25, pady=5)
        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Php 25", fg="Black", anchor='w')
        label_Price_List.grid(row=2, column=9,padx=25, pady=5)

        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Royal", fg="#784017", anchor='w',justify='left')
        label_Price_List.grid(row=3, column=7,padx=25, pady=5)
        label_Price_List = Label(priceList, font=('aria', 10, 'bold'), text="Php 25", fg="Black", anchor='w')
        label_Price_List.grid(row=3, column=9,padx=25, pady=5)




    # design
        label_Design = Label(priceList, font=('aria', 12, 'bold'), text="||", fg="Brown", bd=2, anchor ='w',justify='left')
        label_Design.grid(row=0, column=5,padx=25, pady=10)
        label_Design = Label(priceList, font=('aria', 12, 'bold'), text="||", fg="Brown", bd=2, anchor ='w',justify='left')
        label_Design.grid(row=1, column=5,padx=25, pady=10)
        label_Design = Label(priceList, font=('aria', 12, 'bold'), text="||", fg="Brown", bd=2, anchor ='w',justify='left')
        label_Design.grid(row=2, column=5,padx=25, pady=10)
        label_Design = Label(priceList, font=('aria', 12, 'bold'), text="||", fg="Brown", bd=2, anchor ='w',justify='left')
        label_Design.grid(row=3, column=5,padx=25, pady=10)
        label_Design = Label(priceList, font=('aria', 12, 'bold'), text="||", fg="Brown", bd=2, anchor ='w',justify='left')
        label_Design.grid(row=4, column=5,padx=25, pady=10)
        label_Design = Label(priceList, font=('aria', 12, 'bold'), text="||", fg="Brown", bd=2, anchor ='w',justify='left')
        label_Design.grid(row=5, column=5,padx=25, pady=10)
        label_Design = Label(priceList, font=('aria', 12, 'bold'), text="||", fg="Brown", bd=2, anchor ='w',justify='left')
        label_Design.grid(row=6, column=5,padx=25, pady=10)
        label_Design = Label(priceList, font=('aria', 12, 'bold'), text="||", fg="Brown", bd=2, anchor ='w',justify='left')
        label_Design.grid(row=7, column=5,padx=25, pady=10)
        label_Design = Label(priceList, font=('aria', 12, 'bold'), text="||", fg="Brown", bd=2, anchor ='w',justify='left')
        label_Design.grid(row=8, column=5,padx=25, pady=10)
            
        priceList.mainloop()


# computation
    class Compute:
        def price(self, m1, m2, m3, m4, m5, m6, d1, d2,d3,dt):
            try:
                global a, b, c, d, e, f, g, h,i,j
                a = int(m1.get())
                b = int(m2.get())
                c = int(m3.get())
                d = int(m4.get())
                e = int(m5.get())
                f = int(m6.get())
                g = int(d1.get())
                h = int(d2.get())
                i = int(d3.get())
                j = int(dt.get())

                global cost_tapsilog, cost_tocilog, cost_cornedsilog, cost_bacsilog, cost_porksilog, cost_chicksilog, cost_coke, cost_sprite, cost_royal, meal_cost, Discount, tax_cost, total_cost,cost_discount

                cost_tapsilog       = a * 120
                cost_tocilog        = b *  95
                cost_cornedsilog    = c * 95
                cost_bacsilog       = d * 115
                cost_porksilog      = e * 120
                cost_chicksilog     = f * 115
                cost_coke           = g * 25
                cost_sprite         = h * 25
                cost_royal          = i * 25
                cost_discount       = j * 0.10

                meal_cost = ('%.2f' % (cost_tapsilog + cost_tocilog + cost_cornedsilog + cost_bacsilog + cost_porksilog+ cost_chicksilog + cost_coke + cost_sprite + cost_royal))
                charge = ((cost_tapsilog + cost_tocilog + cost_cornedsilog + cost_bacsilog + cost_porksilog+ cost_chicksilog + cost_coke + cost_sprite+ cost_royal) * cost_discount)
                pay = (( cost_tapsilog + cost_tocilog + cost_cornedsilog + cost_bacsilog + cost_porksilog+ cost_chicksilog + cost_coke + cost_sprite+ cost_royal) * 0.12)
                subtotal = (cost_tapsilog + cost_tocilog + cost_cornedsilog + cost_bacsilog + cost_porksilog+ cost_chicksilog + cost_coke + cost_sprite+ cost_royal)
                Discount= ('%.2f' % charge)
                total_cost = ( pay + subtotal - charge)
                tax_cost = ('%.2f' % pay)

                cost.set(meal_cost)
                discount.set(Discount)
                tax.set(tax_cost)
                sub_total.set(meal_cost)
                final.set(total_cost)

                table.execute("INSERT INTO ORDERS(DATE,TIME,TAPSILOG,TOCILOG,CORNEDSILOG,BACSILOG,PORKSILOG,CHICKSILOG,COKE,SPRITE,ROYAL,COST,DISCOUNT,TAX,SUBTOTAL,TOTAL)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (str(time.strftime('%m-%d-%y')), str(time.strftime('%H:%M:%S')),str(cost_tapsilog), str(cost_tocilog), str(cost_cornedsilog), str(cost_bacsilog),
                    str(cost_porksilog), str(cost_chicksilog), str(cost_coke), str(cost_sprite), str(cost_royal),str(meal_cost), str(Discount),  
                    str(tax_cost), str(meal_cost), str(total_cost)))
                table.commit()
                messagebox.showinfo( "LOADING. . ", "[DATA SAVED]")
            except:
                messagebox.showwarning("WARNING", "Invalid Input")

                # generating bill

        def receipt(self):
            try:
                localtime = time.strftime("Date: " '%m-%d-%y  Time: %H:%M:%S')
                file = open("receipts.txt", "w")
                file.write(localtime + "\n")
                file.write("Order No. : " + str(order) + "\n\n")
                file.write("ITEM               QUANTITY                AMOUNT            TOTAL\n")
                file.write("================================================================================ \n")

                if (cost_tapsilog != 0):
                    file.write("TAPSILOG            " + str(
                        a) + "                      PHP 120" +                  "           PHP " + str(cost_tapsilog) + "\n")
                if (cost_tocilog != 0):
                    file.write("TOCILOG             " + str(
                        b) + "                      PHP 95"  +                  "            PHP " + str(cost_tocilog) +  "\n")
                if (cost_cornedsilog != 0):
                    file.write("CORNEDSILOG         " + str(
                        c) + "                      PHP 115" +                  "           PHP " + str(cost_cornedsilog) +"\n")
                if (cost_bacsilog != 0):
                    file.write("BACSILOG            " + str(
                        d) + "                      PHP 115" +                  "           PHP " + str(cost_bacsilog) + "\n")
                if (cost_porksilog != 0):
                    file.write("PORKSILOG           " + str(
                        e) + "                      PHP 120" +                  "           PHP " + str(cost_porksilog) + "\n")

                if (cost_chicksilog!= 0):
                    file.write("CHICKSILOG          " + str(
                        f) + "                      PHP 115" +                  "           PHP " + str(cost_chicksilog) + "\n")
                if (cost_coke != 0):
                    file.write("COKE                " + str(
                        g) + "                      PHP 25"  +                  "            PHP " + str(cost_coke) + "\n")
                if (cost_sprite != 0):
                    file.write("SPRITE              " + str(
                        h) + "                      PHP 25"  +                  "            PHP " + str(cost_sprite) + "\n")
                if (cost_royal != 0):
                    file.write("ROYAL               " + str(
                        i) + "                      PHP 25"  +                  "            PHP " + str(cost_royal) + "\n")
            
                file.write("================================================================================ \n\n\n")
                file.write("Cost of Meal : PHP " + str(meal_cost) + "")
                file.write("\nDiscount: PHP -" + str(Discount) + "\nTax : PHP " + str(tax_cost) + "\nTotal : PHP " + str(total_cost))
                messagebox.showinfo("RECEIPT", "BILL GENERATED SUCESSFULLY!")
            except:
                messagebox.showwarning("WARNING", "FAILED GENERATING BILL")

    def amount():
        c = Compute()
        c.price(m1, m2, m3, m4, m5, m6, d1, d2,d3,dt)

    def call_receipt():
        c = Compute()
        c.receipt()
        os.startfile("receipts.txt")



    # reset the values
    def reset():
        global order
        order = order + 1
        number.set(order)
        tapsilog.set(0)
        tocilog.set(0)
        cornedsilog.set(0)
        bacsilog.set(0)
        porksilog.set(0)
        chicksilog.set(0)
        coke.set(0)
        sprite.set(0)
        royal.set(0)
        cost.set(0)
        discount.set(0)
        tax.set(0)
        final.set(0)

    def time_display():
        localtime = time.strftime('%m-%d-%y   %H:%M:%S')
        time1.configure(text=localtime)
        TitleFrame.after(200, time_display)


    # window 2 GUI
    TitleFrame = Frame(main)
    TitleFrame.pack(side=TOP)

    MenuFrame = LabelFrame(main,width = 900,height=800,relief=SUNKEN, text="Menu")          
    MenuFrame.pack(fill= "both", expand="yes", padx=20, pady=20)

    x = Label(TitleFrame, text="SHEESHILOG RESTAURANT", font=("times", 30, "bold", "underline"), fg="#784017", bd=10, anchor=W)
    x.grid(row=0, column=0)

    y = Label(TitleFrame, text="DATE:   TIME:", font=("times", 25, ), fg="dark gray", bd=5, anchor=W)
    y.grid(row=1, column=0)

    localtime = time.strftime("Date:" '%m-%d-%y Time:  %H:%M:%S')
    time1 = Label(TitleFrame, text=localtime, font=("arial", 20, "bold"), fg="black", anchor=W)
    time1.grid(row=2, column=0)
    time_display()
 
    
    menuLabel = Label(MenuFrame, text="ORDER No: ", font=('arial', 20, 'bold','underline'), fg="black")
    menuLabel.grid(row=3)
    o1 = Entry(MenuFrame, textvariable=number, font=("arial", 20), fg="black",state='disabled', justify='center')
    o1.grid(row=3, column=1)

    menuLabel = Label(MenuFrame, text="TAPSILOG", font=('arial', 15), fg="#784017")
    menuLabel.grid(row=4)
    m1 = Entry(MenuFrame, textvariable=tapsilog, font=('arial', 15, 'bold'), fg="black", justify='center')
    m1.grid(row=4, column=1)

    menuLabel = Label(MenuFrame, text="TOCILOG", font=("arial", 15), fg="#784017")
    menuLabel.grid(row=5)
    m2 = Entry(MenuFrame, textvariable=tocilog, font=("arial", 15, 'bold'), fg="black", justify='center')
    m2.grid(row=5, column=1)

    menuLabel = Label(MenuFrame, text="CORNEDSILOG", font=("arial", 15), fg="#784017")
    menuLabel.grid(row=6)
    m3 = Entry(MenuFrame, textvariable=cornedsilog, font=("arial", 15, 'bold'), fg="black", justify='center')
    m3.grid(row=6, column=1)

    menuLabel = Label(MenuFrame, text="BACSILOG", font=("arial", 15), fg="#784017")
    menuLabel.grid(row=7)
    m4 = Entry(MenuFrame, textvariable=bacsilog, font=("arial", 15, 'bold'), fg="black", justify='center')
    m4.grid(row=7, column=1)

    menuLabel = Label(MenuFrame, text="PORKSILOG", font=("arial", 15), fg="#784017")
    menuLabel.grid(row=8)
    m5 = Entry(MenuFrame, textvariable=porksilog, font=("arial", 15, 'bold'), fg="black", justify='center')
    m5.grid(row=8, column=1)

    menuLabel = Label(MenuFrame, text="CHICKSILOG", font=("arial", 15), fg="#784017")
    menuLabel.grid(row=9)
    m6 = Entry(MenuFrame, textvariable=chicksilog, font=("arial", 15, 'bold'), fg="black", justify='center')
    m6.grid(row=9, column=1)


    menuLabel = Label(MenuFrame, text="COKE", font=("arial", 15), fg="#784017")
    menuLabel.grid(row=4, column= 4)
    d1 = Entry(MenuFrame, textvariable=coke, font=("arial", 15, 'bold'), fg="black", justify='center')
    d1.grid(row=4, column=5)

    menuLabel = Label(MenuFrame, text="SPRITE", font=("arial", 15), fg="#784017")
    menuLabel.grid(row=5, column= 4)
    d2 = Entry(MenuFrame, textvariable=sprite, font=("arial", 15, 'bold'), fg="black", justify='center')
    d2.grid(row=5, column=5)

    menuLabel = Label(MenuFrame, text="ROYAL", font=("arial", 15), fg="#784017")
    menuLabel.grid(row=6, column= 4)
    d3 = Entry(MenuFrame, textvariable=royal, font=("arial", 15, 'bold'), fg="black", justify='center')
    d3.grid(row=6, column=5)

   

    menuLabel = Label(MenuFrame, text="Cost", font=("arial", 15, 'bold'), fg="#784017")
    menuLabel.grid(row=5, column= 8)
    o6 = Entry(MenuFrame, textvariable=cost, font=("arial", 15), fg="black", state='disabled', justify='center')
    o6.grid(row=5, column=9)

    menuLabel = Label(MenuFrame, text="Discount", font=("arial", 15, 'bold'), fg="#784017")
    menuLabel.grid(row=6, column= 8)
    o2= Entry(MenuFrame, textvariable=discount, font=("arial", 15), fg="black", state='disabled', justify='center')
    o2.grid(row=6, column=9)

    menuLabel = Label(MenuFrame, text="Tax", font=("arial", 15, 'bold'), fg="#784017")
    menuLabel.grid(row=7, column= 8)
    o3 = Entry(MenuFrame, textvariable=tax, font=("arial", 15), fg="black", state='disabled', justify='center')
    o3.grid(row=7, column=9)

    menuLabel = Label(MenuFrame, text="Subtotal", font=("arial", 15, 'bold'), fg="#784017")
    menuLabel.grid(row=8, column= 8)
    o4 = Entry(MenuFrame, textvariable=cost, font=("arial", 15), fg="black", state='disabled', justify='center')
    o4.grid(row=8, column=9)

    menuLabel = Label(MenuFrame, text="Total", font=("arial", 15, 'bold'), fg="#784017")
    menuLabel.grid(row=9, column= 8)
    o5 = Entry(MenuFrame, textvariable=final, font=("arial", 15), fg="black", state='disabled', justify='center')
    o5.grid(row=9, column=9)

    menuLabel = Label(MenuFrame, text="Discount Qty ", font=("arial", 15, 'bold'), fg="#784017")
    menuLabel.grid(row=4, column= 8)
    dt = Entry(MenuFrame, textvariable=discount, font=("arial", 15), fg="black", justify= "center")
    dt.grid(row=4, column=9)


    # window 2 buttons 
    frame_control = Frame(main)
    frame_control.pack(side=BOTTOM)

    frame_control = LabelFrame(main,width = 900,height=340,relief=SUNKEN, text="Controls")          
    frame_control.pack(fill= "both", expand="yes", padx=20, pady=20)

    
    price = Button(frame_control, text="PRICE LIST", height=2, width=16, font=("arial", 15, 'bold'), fg="white",bd = 10, bg = "#784017",
                    command=price)
    price.grid(row=0, column=5, padx=7, pady=7)
    total = Button(frame_control, text="TOTAL AMOUNT", height=2, width=16, font=("arial", 15, 'bold'), fg="white", bd = 10, bg = "#784017",
                    command=amount)
    total.grid(row=0, column=10, padx=7, pady=7)
    reset = Button(frame_control, text="RESET", height=2, width=16, font=("arial", 15, 'bold'), fg="white", bd = 10, bg = "#784017",
                    command=reset)
    reset.grid(row=0, column=25, padx=7, pady=7)
    exit = Button(frame_control, text="EXIT", height=2, width=16, font=("arial", 15, 'bold'), fg="white", bd = 10, bg = "red",
                    command=quit)
    exit.grid(row=0, column=30, padx=7, pady=7)
    receipt = Button(frame_control, text="GENERATE RECEIPT", height=2, width=16, font=("arial", 15, 'bold'), fg="white", bd = 10, bg = "#784017",
                    command=call_receipt)
    receipt.grid(row=0, column=15, padx=7, pady=7)

    totalsale = Button(frame_control, text="TOTAL SALE", height=2, width=16, font=("arial", 15, 'bold'), fg="white", bd = 10,bg = "#784017",
                    command=total_sales)
    totalsale.grid(row=0, column=20, padx=7, pady=7)

    status = Label(main, text="Submitted by: Caguiat, Recana, Oreas", font=("arial", 10, 'bold'), fg="gray", relief=SUNKEN, anchor = 'w')
    status.pack(side=BOTTOM, fill = X)


    main.mainloop()


def total_sales():
    connection   = sqlite3.connect("total_orders.db")
    cursor = connection.cursor()
    Total_day_sale= "select total(TOTAL) from ORDERS"
    cursor.execute(Total_day_sale)
    messagebox.showinfo("SALES", f"TOTAL SALES : PHP {cursor.fetchone()[0]}   ")


def login(username, password):
    uname= username.get()
    pword = password.get()
    
    if (uname == "admin" and pword == "123"):
        
        window2()
        
    else:
        errorLabel = Label(logFrame, font=('aria', 8), text="Oops! Wrong Username or Password. Try again.", fg="red", bd=10, anchor='w', justify='left').grid(row=4,column=1)
        username.set("")
        password.set("")


window1 = Tk()
window1.geometry("600x520+550+50")
window1.title("")

logFrame = LabelFrame(window1,width = 580,height=500,relief=SUNKEN, text="Login")
logFrame.pack(fill= "both", expand="yes", padx=20, pady=10)

resto_name= Label(logFrame, font=( 'arial' ,15, 'bold' ), text="SHEESHILOG RESTAURANT",fg="Black",bd=10,anchor='w',justify='right').grid(row=0, column=1,padx=28, pady=19)

username = StringVar()
password = StringVar()

label_username= Label(logFrame, font=( 'arial' ,12, 'bold' ), text="Username:",fg="Black",bd=10,anchor='w',justify='right').grid(row=1, column=0,padx=28, pady=5)
username_enter = Entry(logFrame,font=( 'arial'  ,12,'bold'),bd=5,justify='center', textvariable=username).grid(row=1, column=1,padx=28, pady=5)  

label_password = Label(logFrame,text="Password:",font=( 'arial' ,12, 'bold' ),fg="Black",bd=10,anchor='w',justify='right').grid(row=2, column=0,padx=28, pady=10)  
password_enter = Entry(logFrame, textvariable=password, show='*',font=( 'arial'  ,12,'bold'), bd=5,justify='center').grid(row=2, column=1,padx=28, pady=10)  

login = partial(login, username, password)

status = Label(window1, text="Submitted by: Caguiat, Recana, Oreas", font=("arial", 10, 'bold'), fg="gray", relief=SUNKEN, anchor = 'w')
status.pack(side=BOTTOM, fill = X)

btnEnter=Button(logFrame,padx=19,pady=10, bd=10 ,fg="white",font=( 'arial'  ,12,'bold'),width=10, text="LOG IN", bg="#784017",command=login)
btnEnter.grid(row=3, column=1, padx=28, pady=20)  



window1.mainloop()
