from tkinter import *

root = Tk()
root.title("Adressenbuch")
root.geometry("600x600")

root.iconbitmap("book1.ico")
root.configure(background="lightgrey")

bg = PhotoImage(file="book2.png")
label1 = Label(root, image=bg, width=200, height=200)
label1.pack(pady=10)

l1 = Label(root, text="Den Namen eingeben", bg="Lightgrey", font=("Arial", 16), fg="red")
l1.pack()

t1 = Text(root, height=2, width=15)
t1.pack(pady=10)

f1 = Frame(root, bg="lightgrey")
b1 = Button(f1, text="OK", height=2, width=10, command=lambda: input())
b1.grid(row=1, column=1)
b2 = Button(f1, text="show text", height=2, width=10, command=lambda: output())
b2.grid(row=1, column=2, padx=10)
f1.pack()

t2 = Text(root, height=50, width=40)
t2.pack(pady=10, side="bottom")

a = ""
def input():
    a = t1.get(1.0, "end-1c") + "\n"
    t1.delete(1.0, "end-1c")
    f = open("Adressen.txt", "a")
    f.write(a)
    f.close()

b = ""
def output():
    f = open("Adressen.txt", "r")
    b = f.read().strip()

    t2.delete(1.0, "end-1c")
    t2.insert(1.0, b)

root.mainloop()