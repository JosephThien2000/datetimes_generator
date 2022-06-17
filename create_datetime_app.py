# import necessary libraries
from tkinter import *
from tkinter import ttk
from datetimes import * # Import datetimes package


# class Main
class Main(Frame):

    # constructor
    def __init__(self, parent, *args,**kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.initUI()
        
    
    # initUI
    def initUI(self):

        # variables
        self.num_of_elements = StringVar()
        self.num_of_elements.set("0")

        # main frame
        self.pack(fill=BOTH, expand=True)
        self.frm_main = ttk.Frame(self)
        self.frm_main.pack(fill=BOTH, expand=True)

        self.label = ttk.Label(master=self.frm_main, text="Enter number of elements: ")
        self.label.pack(fill=BOTH, expand=True)

        self.entry = ttk.Entry(master=self.frm_main, textvariable=self.num_of_elements)
        self.entry.pack(fill=BOTH, expand=True)

        self.btn_create = ttk.Button(master=self.frm_main, text="Create", command=self.datetimes)
        self.btn_create.pack(expand=True)

        
        self.btn_quit = ttk.Button(master=self.frm_main, text="Quit", command=self.quit)
        self.btn_quit.pack(expand=True)

    def datetimes(self):
        self.num_of_elements = self.entry.get()
        return create_datetime(self.num_of_elements)

class Root(Tk):

    # constructor
    def __init__(self):
        super().__init__()
        self.title("Create DateTime App")
        self.resizable(True, True)
        self.geometry("500x300")

# main function
def main():
    root = Root()
    app = Main(root)
    root.mainloop()

# Run main
if __name__ == "__main__":
    main()
