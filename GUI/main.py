import customtkinter 
from serials import *

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1344x768")
        self.title("Serial Data Plotting - Bagas, Faiz, Ade")
        self.grid_rowconfigure(0, weight=8) 
        self.grid_rowconfigure(1, weight=2) 
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=8)

        self.serialFrame = SerialFrame(master=self)
        self.serialFrame.grid(row=0, column=0, padx=20, pady=20, rowspan=2, sticky="nsew")
        

if __name__ == '__main__':
    app = App()
    app.mainloop()