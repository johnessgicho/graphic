import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("simple calc app by ness")
        self.master.resizable(False, False)
        
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        self.display = tk.Label(self.master, textvariable=self.display_var, width=32, height=6, anchor="e", background="green")
        self.display.grid(row=0, column=0, columnspan=4)
        
        button_list = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]
        
        row = 1
        col = 0
        
        for button_text in button_list:
            button = tk.Button(self.master, text=button_text, width=6, height=3, command=lambda text=button_text:self.button_click(text))
            button.grid(row=row, column=col)
            
            col += 1
            
            if col > 3:
                col = 0
                row += 1
                
    def button_click(self, text):
        if text == "=":
            try:
                result = str(eval(self.display_var.get()))
                self.display_var.set(result)
            except:
                self.display_var.set("Error")
        else:
            if self.display_var.get() == "0":
                self.display_var.set(text)
            else:
                self.display_var.set(self.display_var.get() + text)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
