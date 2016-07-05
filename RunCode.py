import os
import subprocess
import tkSimpleDialog
import threading
from idlelib.configHandler import idleConf
from Tkinter import *
from ScrolledText import ScrolledText

class StdIO(ScrolledText):
    def __init__(self, name, close_func, parent=None, **kwargs):
        frame = LabelFrame(parent, text=name)
        self.parent = parent
        ScrolledText.__init__(self, frame, **kwargs)
        self.bind('<Escape>', lambda event: close_func(event))

        self.pack(fill='both', expand=True)
        frame.pack(fill='both', expand=True)


class RunCode(object):
    menudefs = [
        ('run', [
            ('Run Code', '<<run-code>>'),
        ])
    ]

    def __init__(self, editwin=None):
        self.editwin = editwin
        if editwin is None:
            return

        self.text = editwin.text
        self.io = editwin.io
        self.text.bind('<<run-code>>', self.run_code)
        self.subwin = None

    def exec_from_key(self, event=None):
        self.stdin.config(state='disabled')
        self.execute(event)
##        self.stdin.delete('insert', 'insert+1c')
        string = self.stdin.get('1.0', 'end')
##        self.stdin.delete('1.0', 'end')
##        self.stdin.insert('1.0', string.rstrip())
##        self.stdin.delete('end-1c', 'end')
        self.stdin.config(state='normal')
        self.stdin.focus_set()

    def _open_window(self, event=None):
        self.subwin = Toplevel(self.text)
        self.subwin.title('Standard Streams')

        kwargs = {
            'width': 40, 'height': 8,
            'fg': 'white', 'bg': 'black', 'font': 'Consolas 10',
            'insertbackground': 'white',
        }

        self.stdin = StdIO('Standard Input', self._close_window, self.subwin, **kwargs)
##        self.stdin.unbind('<Control-Key-Return>')
        self.stdin.bind('<Control-Key-Return>', self.execute)

        frame = Frame(self.subwin, width=40, height=3)
        self.exec_button = Button(
            frame, text='Execute', command=self.execute,
        )

        labelframe = LabelFrame(frame, text='Time Limit')
        unit = Label(labelframe, text='sec')
        unit.pack(side='right')
        tl = StringVar(value=2)
        self.time_limit = Spinbox(
            labelframe, from_=1, to=60, increment=1, width=8, textvariable=tl,
        )
        self.time_limit.pack(anchor='w')

        labelframe.pack(side='top', anchor='e')
##        space = Label(frame, text=' '*12)  # todo
##        space.pack(side='right', anchor='s')
        self.exec_button.pack(side='bottom', anchor='s')

        frame.pack(side='top', fill='both')

        self.stdout = StdIO('Standard Output', self._close_window, self.subwin, **kwargs)
        self.stderr = StdIO('Standard Error', self._close_window, self.subwin, **kwargs)

        self.stdin.focus_set()

    def _close_window(self, event=None):
        def _close(window, event=None):
            window.grab_release()
            window.withdraw()

        if self.subwin is not None:
            _close(self.subwin, event)

        self.subwin = None

    def run_code(self, event=None):
        try:
            self.subwin.focus_set()
        except (TclError, AttributeError):
            self._open_window()
##        if self.subwin is None:
##            self._open_window()
##        else:
##            #print `self.subwin`
##            self.subwin.focus_set()

    def execute(self, event=None):
        if self.io.filename is None:
            return

        exec_name = os.path.splitext(self.io.filename)[0]+'.exe'
        if not os.path.isfile(exec_name):
            return

        self.stdout.delete('1.0', 'end')
        self.stderr.delete('1.0', 'end')

        def run_exe():
            p = subprocess.Popen(
                exec_name, shell=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            stdin = self.stdin.get('1.0', 'end')
            if not stdin.endswith('\n'):
                stdin += '\n'

            stdout, stderr = p.communicate(stdin)
            self.stdout.insert('1.0', stdout)
            self.stderr.insert('1.0', stderr)

        d = threading.Thread(name='exe', target=run_exe)
        self.stdin.focus_set()
        d.start()
        self.stdin.focus_set()
        d.join(int(self.time_limit.get()))
        self.stdin.focus_set()
        if d.isAlive():
            self.stderr.insert('1.0', 'Time Limit Exceeded')
            self.stdin.focus_set()

        self.stdin.focus_set()
