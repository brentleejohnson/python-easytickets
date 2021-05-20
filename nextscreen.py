from tkinter import *

root = Tk()
root.title("TicketSales")
root.geometry("450x500")
root.config(bg="#DDFFF7")
root.resizable(height=False, width=False)


def nextscreen():
    root.destroy()
    import main


button1 = Button(root, text="Welcome To TicketSales", fg="black", border=4, bg="#ffd6F5", command=nextscreen)
button1.place(x=105, y=250)

root.mainloop()
