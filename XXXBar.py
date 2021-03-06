from Tkinter import *
import re
import string

UPDATEINTERVAL = 50 # ms

class XXXBar(Frame):

    def __init__(self, master=None, editwin=None, **kw):
        if master is None:
            master = Tk()
        Frame.__init__(self, master, **kw)
        self.labels = {}

        if editwin is None:
            return

        self.editwin = editwin
        self.text = self.editwin.text
##        self.text.after(UPDATEINTERVAL, self.timer_event)

##        al = string.ascii_lowercase
##        #for c in al:
##        bind_ctrl = lambda k: self.text.bind(
##            '<Control-Key-{}>'.format(k),
##            lambda e: self.write_key(e, 'C-{}'.format(k))
##        )
##        bind_alt = lambda k: self.text.bind(
##            '<Alt-Key-{}>'.format(k),
##            lambda e: self.write_key(e, 'M-{}'.format(k))
##        )
##        bind_raw = lambda k: self.text.bind(
##            '<Key-{}>'.format(k),
##            lambda e: self.write_key(e, None)
##        )
##        for c in al:
##            bind_ctrl(c)
##            bind_alt(c)
##            bind_raw(c)

##        for i in range(len(al)):
##            c = str(al[i])
##            self.text.bind(
##                '<Control-Key-{}>'.format(c),
##                lambda e: self.write_key(e, 'C-{}'.format(c))
##            )
##            self.text.bind(
##                '<Alt-Key-{}>'.format(c),
##                lambda e: self.write_key(e, 'M-{}'.format(c))
##            )
##            self.text.bind(
##                '<Key-{}>'.format(c),
##                lambda e: self.write_key(e, None)
##            )

##        self.t = StringVar()
##        print master, editwin
        self.set_label('xxx', text=' Lorem ipsum dolor sit amet', font='Consolas 10', bg='white')

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

##    def timer_event(self):
##        if self.labels:
##            self.update_xxxbar()
##        self.text.after(UPDATEINTERVAL, self.timer_event)

##    def write_key(self, event=None, key=''):
##        if key is None:
##            self.t.set('')
##        elif len(self.t.get()) > 20:
##            self.t.set(' '+key)
##        else:
##            self.t.set(self.t.get()+' '+key)
##
##        self.labels['xxx'].config(text=self.t.get())

##    def update_xxxbar(self, event=None):
####        t = self.text.get('insert linestart', 'insert')
####        self.labels['xxx'].config(text=' '+re.search(r'\w*$', t).group())
##        self.labels['xxx'].config(text=repr(event))

    
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
