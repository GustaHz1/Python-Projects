from tkinter import *

class Application:
    def __init__(self, master = None):
        self.widget1 = Frame(master)
        self.widget1.pack()

        self.result = StringVar()
        
        self.display = Entry(self.widget1, textvariable=self.result, font = ("Calibri", "20"), bd = 10, insertwidth = 2, width = 14, borderwidth = 4)
        self.display.grid(row = 0, column = 0, columnspan = 4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('=', 4, 1), ('C', 4, 2), ('+', 4, 3)
        ]
        
        for (text, row, col) in buttons:
            button = Button(self.widget1, text = text, font = ("Calibri", "20"), command = lambda t = text: self.on_button_click(t))
            button.grid(row = row, column = col, sticky = "nsew")

        for i in range(5):
            self.widget1.grid_rowconfigure(i, weight = 1)
        for i in range(4):
            self.widget1.grid_columnconfigure(i, weight = 1)
    
    def on_button_click(self, char):
        if char == '=':
            try:
                self.result.set(eval(self.result.get()))
            except Exception as e:
                self.result.set("Error")
        elif char == 'C':
            self.result.set("")
        else:
            current = self.result.get()
            new = current + char
            self.result.set(new)

root = Tk()
app = Application(root)
root.mainloop()
