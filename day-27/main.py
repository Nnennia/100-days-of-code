import tkinter

window = tkinter.Tk()

window.title("My First GUI")

window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"

my_label.config(text="New Text")
my_label.place(x=0, y=0) # so specific
# my_label.grid(column=0, row=0)
# button


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

# Entry
input = tkinter.Entry(width=10)
input.pack()

# # entries
# entry = tkinter.Entry(width=30)
# entry.insert(END, string="Some text to begin with.")

window.mainloop()
