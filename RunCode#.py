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

        try:
            f = self.editwin.ftype.get()
        except:
            f = 'xxx'

        self.cpp14opt = BooleanVar()
        self.cppstd = StringVar(value=" --std=c++11")

        self.wall = BooleanVar(value=True)
        self.wextra = BooleanVar()

        self.tl = StringVar(value=2)
        self.t_cmp_c = StringVar(value='gcc -Wall -O2 -o %s.exe %s.c')
        self.t_cmp_cpp = StringVar(value='g++ -Wall -O2 -o %s.exe %s.cpp')
        self.t_exec = StringVar(value='%s.exe < stdin > stdout 2> stderr')

##    def exec_from_key(self, event=None):
##        self.stdin.config(state='disabled')
##        self.execute(event)
####        self.stdin.delete('insert', 'insert+1c')
##        string = self.stdin.get('1.0', 'end')
####        self.stdin.delete('1.0', 'end')
####        self.stdin.insert('1.0', string.rstrip())
####        self.stdin.delete('end-1c', 'end')
##        self.stdin.config(state='normal')
##        self.stdin.focus_set()

    def _open_window(self, event=None):
        self.subwin = Toplevel(self.text)
        self.subwin.title('Standard Streams')

        kwargs = {
            'width': 40, 'height': 8,
            'bg': 'black',
            'insertbackground': 'white',
        }

##        self.stdin = StdIO(
##            'Standard Input', self._close_window, self.subwin, fg='white',
##            font='Consolas 10', **kwargs
##        )
##        self.stdin.bind('<Control-Key-Return>', self.execute)

        frame = Frame(self.subwin, width=40, height=3)
        exlf = LabelFrame(frame, text='Execution')
        colf = LabelFrame(frame, text='Compilation')

        self.exec_button = Button(
            exlf, text='Execute', command=self.execute,
        )
        self.comp_button = Button(
            colf, text='Compile', command=self.compile_,
        )

        self.comp_button.pack(side='right', anchor='s', padx=2, pady=8)
        self.exec_button.pack(side='right', anchor='s', padx=2, pady=8)

        tllf = LabelFrame(exlf, text='Time Limit')
        unit = Label(tllf, text='sec')
        unit.pack(side='right')
##        tl = StringVar(value=2)
        self.time_limit = Spinbox(
            tllf, from_=1, to=60, increment=1, width=8, textvariable=self.tl,
        )
        self.time_limit.pack(anchor='w')

        tllf.pack(side='right', padx=2)

        stdlf = LabelFrame(colf, text='C++ Standards')

##        vcb = Checkbutton(colf, text='verbosely', variable=self.cpp14opt)
##        vcb = Checkbutton(oplf, text='C++14', variable=self.cpp14opt)

##        vcb = Checkbutton(oplf, text='std=c++14', variable=self.cpp14opt)
##        vcb.pack(side='right', anchor='se')

        available_stds = [
            ('98', ' --std=c++98'),
            ('11', ' --std=c++11'),
            ('14', ' --std=c++14'),
##            ('17', ' --std=c++17'),
        ]
        for text, value in available_stds:
            vrb = Radiobutton(
                stdlf, text=text, variable=self.cppstd, value=value,
            )
            vrb.pack(side='left', anchor='w')

        stdlf.pack(side='right', padx=2, pady=2, fill='both')

        wlf = LabelFrame(colf, text='Warnings')

        wacb = Checkbutton(wlf, text='all', variable=self.wall)
        wecb = Checkbutton(wlf, text='extra', variable=self.wextra)

        wacb.pack(side='left')
        wecb.pack(side='left')
##        wlf.pack(side='top', anchor='e')
        wlf.pack(side='right', padx=2, pady=2, fill='both')

##        self.comp_button.pack(side='left', anchor='w')
##        self.exec_button.pack(side='left', anchor='w')
##        exlf.pack(side='right', fill='both', expand=True)
##        colf.pack(side='left', fill='both', expand=True)
##
##        frame.pack(side='top', fill='both')

        colf.pack(side='top', fill='both', expand=True)
        exlf.pack(side='top', fill='both', expand=True)

        frame.pack(side='top', fill='both')

##        cmds = LabelFrame(self.subwin, text='Commands')
##        ccmd_c = Entry(
##            cmds, textvariable=self.t_cmp_c, state='readonly',
##            fg='white', bg='black',
##            readonlybackground='black',
##            font='Consolas 10', width=40,
##        )
##        ccmd_cpp = Entry(
##            cmds, textvariable=self.t_cmp_cpp, state='readonly',
##            fg='white', bg='black',
##            readonlybackground='black',
##            font='Consolas 10', width=40,
##        )
##        ecmd = Entry(
##            cmds, textvariable=self.t_exec, state='readonly',
##            fg='white', bg='black',
##            readonlybackground='black',
##            font='Consolas 10', width=40,
##        )
##        ccmd_c.pack(side='top', anchor='nw')
##        ccmd_cpp.pack(side='top', anchor='nw')
##        ecmd.pack(side='top', anchor='nw')
##        #cmds.pack(side='top', fill='both')

        self.stdin = StdIO(
            'Standard Input', self._close_window, self.subwin, fg='white',
            font='Consolas 10', **kwargs
        )
        self.stdin.bind('<Control-Key-Return>', self.execute)

        self.stdout = StdIO(
            'Standard Output', self._close_window, self.subwin, fg='white',
            font='Consolas 10 bold', **kwargs
        )
        self.stderr = StdIO(
            'Standard Error', self._close_window, self.subwin, fg='#b7b7b7',
            font='Consolas 10', **kwargs
        )

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

    def compile_(self, event=None):
        if self.io.filename is None:
            return

##        self.stdout.delete('1.0', 'end')
##        self.stderr.delete('1.0', 'end')
##
        def run_compile():
            if not hasattr(self.editwin, 'ext'):
                return

            try:
                f = self.editwin.ftype.get()
            except (AttributeError,):
                return

            if f in ('C/l',):
                cc = idleConf.GetOption('extensions', 'CompileCode', 'compile_c')
            elif f in ('C++/l',):
                cc = idleConf.GetOption('extensions', 'CompileCode', 'compile_cpp')

            raw_name = os.path.splitext(self.io.filename)[0]
            cc = cc.format(raw_name)
##            if self.cpp14opt.get():
####                cc += ' -v'
##                cc += ' --std=c++14'

            cc += self.cppstd.get()

            if self.wall:
                cc += ' -Wall'
            if self.wextra:
                cc += ' -Wextra'

            options = (
##                '-lquadmath',
            )
            for o in options:
                cc += ' ' + o

            self.stdout.delete('1.0', 'end')
            self.stderr.delete('1.0', 'end')

##            self.stderr.insert('1.0', 'Compilation in progress')  # does not appear?
            p = subprocess.Popen(
                cc, shell=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            crlf = lambda s: s.replace('\r\n', '\n').replace('\r', '\n')
            stdout, stderr = map(crlf, p.communicate())

            fullpath_win = self.io.filename.replace('\\', r'\\')
            fullpath_unix = self.io.filename.replace('\\', '/')
            basename = os.path.basename(self.io.filename)

            stderr = re.sub(fullpath_win, basename, stderr)
            stderr = re.sub(fullpath_unix, basename, stderr)

##            stdout, stderr = p.communicate()
            self.stdout.insert('1.0', stdout)
##            self.stderr.delete('1.0', 'end')
            self.stderr.insert('1.0', stderr)

##        self.stderr.insert('1.0', 'Compilation in progress')
        d = threading.Thread(name='compile', target=run_compile)
        d.start()
        d.join(15)
        self.stdin.focus_set()

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

            crlf = lambda s: s.replace('\r\n', '\n').replace('\r', '\n')
            stdout, stderr = map(crlf, p.communicate(stdin))
##            stdout, stderr = p.communicate(stdin)
            self.stdout.insert('1.0', stdout)
            self.stderr.insert('1.0', stderr)

        d = threading.Thread(name='exe', target=run_exe)
        self.stdin.focus_set()
        d.start()
        self.stdin.focus_set()
        d.join(int(self.time_limit.get()))
        self.stdin.focus_set()
        if d.isAlive():
            self.stderr.insert('1.0', '[Time Limit Exceeded]\n')
            p = subprocess.Popen(
                'taskkill /im {} /f /t'.format(os.path.basename(exec_name)),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
            )
            stdout, stderr = p.communicate()
            self.stderr.insert('end', '[TERMINATED]')
##            self.stderr.insert('end', stdout)
##            self.stderr.insert('end', stderr)
            self.stdin.focus_set()

        self.stdin.focus_set()
