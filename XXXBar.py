from Tkinter import *

class XXXBar(Frame):

    def __init__(self, master=None, **kw):
        if master is None:
            master = Tk()
        Frame.__init__(self, master, **kw)
        self.labels = {}

    def set_label(self, name, text='', side=LEFT, width=0, **kw):
        if name not in self.labels:
            label = Label(self, borderwidth=0, anchor=W)
            label.pack(side=side, pady=0, padx=4)
            self.labels[name] = label
        else:
            label = self.labels[name]
        if width != 0:
            label.config(width=width)
        label.config(text=text, **kw)

def _xxx_bar(parent):
    root = Tk()
    width, height, x, y = list(map(int, re.split('[x+]', parent.geometry())))
    root.geometry("+%d+%d" % (x, y+150))
    root.title("Test xxx bar")
    frame = Frame(root)
    text = Text(frame)
    text.pack()
    mb = XXXBar(frame)
    mb.set_label("one", "hello")
    mb.set_label("two", "world")
    mb.pack(side=BOTTOM, fill=X)

    def change():
        mb.set_label("one", "foo")
        mb.set_label("two", "bar")

    button = Button(root, text="Update status", command=change)
    button.pack(side=BOTTOM)
    frame.pack()
    frame.mainloop()
    root.mainloop()

if __name__ == '__main__':
    from idlelib.idle_test.htest import run
    run(_xxx_bar)
