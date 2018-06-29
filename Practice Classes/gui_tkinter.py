import tkinter

class Pymodoro:
    def __init__(self, master):
        self.master = master
        self.mainframe = tkinter.frame(self.master, bg= 'white')
        self.mainframe.pack(fill = tkinter.BOTH, expand = True)

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight = 1)
        self.mainframe.rowconfigure(0, weight = 0)
        self.mainframe.rowconfigure(1, weight = 1)
        self.mainframe.rowconfigure(2, weight = 0)

    def build_banner(self):
        banner = tkintet.Label(
            self.mainframe,
            background = 'black',
            text = 'Pomodoro',
            fg = 'white',
            font = ('Helvetica', 24)
            )

if __name__ == '__main__':
    root = tkinter.Tk()
    Pymodoro(root)
    root.mainloop()
