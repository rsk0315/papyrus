import os
import regex
import subprocess
import tkSimpleDialog
import threading
import ttk
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

class ExitStatus(Entry):
    def __init__(self, tvar, parent=None, **kwargs):
        if parent is None: return

        Entry.__init__(self, parent, width=11, **kwargs)
        tvar.set('')
        self.tvar = tvar

    def update(self, p):
        if p is None:
            self.tvar.set('')
        else:
            if hasattr(p, 'returncode'):
                r = p.returncode
                if r < 0:
                    r += 2147483648

                if r < 10:
                    self.tvar.set(str(r))
                else:
                    self.tvar.set('0x{:X}'.format(r))
            else:
                self.tvar.set('-')

        status = self.tvar.get().strip()

        if not status:
            self.configure(bg='black')
        elif status == '0':
            self.configure(bg='#00c000', fg='#d2fadc')
        else:
            self.configure(bg='#c00000', fg='#fad2dc')

class tkPulldown(ttk.Combobox):
    def __init__(self, parent, values, **kwargs):
        ttk.Combobox.__init__(self, parent, **kwargs)
        self['values'] = values
        self.current(0)
        self.grid(row=0, column=0, columnspan=10)
        self.configure(
            state='readonly',
        )

class RunCode(object):
    menudefs = [
        ('run', [
            ('Run Code', '<<run-code>>'),
        ])
    ]

    COMPILE_CMDS = {
        'C89':
            'gcc --std=c89 -O2 -o {out} {in_}',
##        'C99':
##            'gcc --std=c99 -O2 -o {out} {in_}',
        'C11':
            'gcc --std=c11 -O2 -o {out} {in_}',
        'C++03':
            'g++ --std=c++03 -O2 -o {out} {in_}',
##        'C++11':
##            'g++ --std=c++11 -O2 -o {out} {in_}',
        'C++14':
            'g++ --std=c++14 -O2 -o {out} {in_}',
        'C#':
            'mcs {in_}',
        'Java':
            'javac {in_}',
        'Haskell':
            'ghc -o {out} {in_}',
    }

    EXECUTE_CMDS = {
        'Java':
            'java -classpath {cpath} {root}',
        'Python2':
            'py -2 {in_}',
        'Python3':
            'py -3 {in_}',
    }

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

        self.wall = BooleanVar(value=True)
        self.wextra = BooleanVar()
        self.addopts = StringVar()
        self.argv = StringVar()
        self.cargv = BooleanVar()

        self.tl = StringVar(value=2)
        self.es = StringVar(value='')

    def _open_window(self, event=None):
        self.subwin = Toplevel(self.text)
        self.subwin.title('Standard Streams')

        kwargs = {
            'width': 40, 'height': 8,
            'bg': 'black',
            'insertbackground': 'white',
        }

        frame = Frame(self.subwin, width=40)
        exlf = LabelFrame(frame, text='Execution')
        colf = LabelFrame(frame, text='Compilation')

        # --- Execution ---
        self.exec_button = Button(
            exlf, text='Execute', command=self.execute,
        )

        self.exec_button.pack(side='right', anchor='s', padx=6, pady=8)

        tllf = LabelFrame(exlf, text='Time Limit')
        unit = Label(tllf, text='sec')
        unit.pack(side='right')

        self.time_limit = Spinbox(
            tllf, from_=1, to=60, increment=1, width=8, textvariable=self.tl,
        )
        self.time_limit.pack(anchor='w')

        cargvlf = LabelFrame(exlf, text="Pass arguments")
        self.cuses_argv = Checkbutton(
            cargvlf, variable=self.cargv, text="also to compiler",
        )
        self.cuses_argv.pack()
        cargvlf.pack(side='left', padx=4)

        tllf.pack(side='left', padx=9, pady=6)

        # --- Compilation ---
        coptframe = Frame(colf)
        optionbuttons = Frame(coptframe)

        ## * Warning  options
        wlf = LabelFrame(optionbuttons, text='Warnings')

        wacb = Checkbutton(wlf, text='all', variable=self.wall)
        wecb = Checkbutton(wlf, text='extra', variable=self.wextra)

        wacb.pack(side='left')
        wecb.pack(side='left')

        wlf.pack(side='left', padx=4, pady=2, fill='x', anchor='n')

        ## * Standard options
        langlf = LabelFrame(optionbuttons, text='Languages')
        available_langs = [
            'C89', 'C11', 'C++03', 'C++14', 'C#',
            'Java', 'Haskell',
            'Python2', 'Python3',
        ]

        self.lang = tkPulldown(langlf, available_langs, width=8)
        self.lang.pack(side='right', anchor='w')
        optionbuttons.pack(side='top')

        langlf.pack(side='right', padx=4, pady=2, fill='x')

        ## * Button
        bframe = Frame(colf)
        self.comp_button = Button(
            bframe, text='Compile', command=self.compile_,
        )

        self.comp_button.pack(side='right', anchor='s', padx=6, pady=8)

        coptframe.pack(side='left')
        bframe.pack(side='top', fill='both', expand=True)

        exlf.pack(side='top', fill='both', expand=True)
        colf.pack(side='top', fill='both', expand=True)

        # --- Streams ---
        shframe = Frame(frame)
        ## * Argv
        argvlf = LabelFrame(shframe, text='Command line arguments')
        self.argve = Entry(
            argvlf, textvariable=self.argv,
            width=20,  font='Consolas 10',
            foreground='white', background='black', insertbackground='white',
        )

        self.argve.bind('<Control-Key-Return>', self.execute)
        self.argve.bind('<Control-Shift-Key-Return>', self.compile_)
        self.argve.bind('<Escape>', self._close_window)

        self.argve.pack(side='top', fill='both', expand=True)

        argvlf.pack(side='left', padx=2, pady=2, fill='both', expand=True)

        # --- Exit status ---
        esframe = LabelFrame(shframe, text='Exit status')
        self.estatus = ExitStatus(
            self.es, esframe, textvariable=self.es, font='Consolas 10',
            fg='#b7b7b7', bg='black', justify='right',
        )
        self.estatus.pack()
        esframe.pack(side='right')

        shframe.pack(fill='x', expand=True)

        self.stdin = StdIO(
            'Standard Input', self._close_window, frame, fg='white',
            font='Consolas 10', **kwargs
        )
        self.stdin.bind('<Control-Key-Return>', self.execute)
        self.stdin.bind('<Control-Shift-Key-Return>', self.compile_)

        self.stdout = StdIO(
            'Standard Output', self._close_window, frame, fg='white',
            font='Consolas 10 bold', **kwargs
        )
        self.stderr = StdIO(
            'Standard Error', self._close_window, frame, fg='#b7b7b7',
            font='Consolas 10', **kwargs
        )

        # ---
        frame.pack(side='top', fill='both', expand=True)
        self.stdin.focus_set()

        if self.io.filename:
            os.chdir(os.path.dirname(self.io.filename))

    def _close_window(self, event=None):
        def _close(window, event=None):
            window.grab_release()
            window.withdraw()

        if self.subwin is not None:
            _close(self.subwin, event)

        self.subwin = None

    def write_error(self, level, msg, pos='1.0'):
        msg = '{}: {}\n'.format(level, msg)
        self.stderr.insert(pos, msg)

    def run_code(self, event=None):
        try:
            self.subwin.focus_set()
            self.stdin.focus_set()
        except (TclError, AttributeError):
            self._open_window()

    def compile_(self, event=None):
        if self.io.filename is None:
            self.write_error(
                'Error',
                'Source must to be named; please save'
            )
            return

        self.stdout.delete('1.0', 'end')
        self.stderr.delete('1.0', 'end')
        self.stderr.insert('1.0', 'Compiling...\n')
        self.estatus.update(None)

        self.stdout.update_idletasks()
        self.stderr.update_idletasks()

        def run_compile():
            self.stderr.delete('1.0', 'end')
            self.stdout.delete('1.0', 'end')

            source_name = self.io.filename
            if source_name is None:
                return

            lang = self.lang.get()
            cc = self.COMPILE_CMDS.get(lang, None)
            if cc is None:
                self.write_error(
                    'Note',
                    'Selected language does not need compiling\n'
                )
                return

            if lang in ('C89', 'C11', 'C++03', 'C++14', 'Haskell'):
                cc += ' -Wall'

            # todo configureable extension
            out_name = os.path.splitext(source_name)[0] + '.exe'

            if self.cargv.get():
                m = regex.search(r'\B--\B', self.argv.get())
                endpos = m and m.end()

                if regex.search(
                        r'\B-[A-Z]*[ES]', self.argv.get(), endpos=endpos
                ):
                    out_name = '-'

                cc = cc.format(out=out_name, in_=source_name)
                cc += ' ' + self.argv.get()

            else:
                if self.argv.get().strip() != '':
                    self.write_error(
                        'Note',
                        'Command line arguments are not passed to the compiler'
                    )

                cc = cc.format(out=out_name, in_=source_name)

            p = subprocess.Popen(
                cc, shell=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            crlf = lambda s: s.replace('\r\n', '\n').replace('\r', '\n')
            stdout, stderr = map(crlf, p.communicate())
            self.estatus.update(p)

            fullpath_win = self.io.filename.replace('\\', r'\\')
            fullpath_unix = self.io.filename.replace('\\', '/')
            basename = os.path.basename(self.io.filename)

            stderr = re.sub(fullpath_win, basename, stderr)
            stderr = re.sub(fullpath_unix, basename, stderr)

            self.stdout.insert('1.0', stdout)
            self.stderr.insert('1.0', stderr)

        d = threading.Thread(name='compile', target=run_compile)
        d.start()
        d.join(15)
        self.stdin.focus_set()
        if d.isAlive():
            self.stderr.insert('1.0', '[Time Limit Exceeded]\n')
            p2 = subprocess.Popen(
                'taskkill /im {} /f /t'.format(cc.split()[0]),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
            )
            stdout, stderr = p2.communicate()
            self.stderr.insert('end', '[TERMINATED]')

            self.stdin.focus_set()

    def execute(self, event=None):
        if self.io.filename is None:
            return

        exec_name = os.path.splitext(self.io.filename)[0]+'.exe'
        if not os.path.isfile(exec_name):
            lang = self.lang.get()
            ec = self.EXECUTE_CMDS.get(lang, '{out}')
            if '{out}' in ec:
                self.write_error(
                    'Error',
                    'Selected language needs compiling'
                )
                return

        self.estatus.update(None)
        self.stdout.delete('1.0', 'end')
        self.stderr.delete('1.0', 'end')
        self.stderr.insert('1.0', 'Executing...\n')
        self.stdout.update_idletasks()
        self.stderr.update_idletasks()

        def run_exe():
            lang = self.lang.get()
            exec_cmd = self.EXECUTE_CMDS.get(lang, '{out}').format(
                in_=self.io.filename,
                out=exec_name,
                cpath=os.path.dirname(self.io.filename),
                root=os.path.basename(os.path.splitext(self.io.filename)[0]),
            )
            p = subprocess.Popen(
                exec_cmd+' '+self.argv.get(), shell=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            stdin = self.stdin.get('1.0', 'end')
            if not stdin.endswith('\n'):
                stdin += '\n'

            crlf = lambda s: s.replace('\r\n', '\n').replace('\r', '\n')
            stdout, stderr = map(crlf, p.communicate(stdin))
            self.stderr.delete('1.0', 'end')
            self.stdout.insert('1.0', stdout)
            self.stderr.insert('1.0', stderr)

            self.estatus.update(p)

        d = threading.Thread(name='exe', target=run_exe)
        self.stdin.focus_set()
        d.start()
        self.stdin.focus_set()
        d.join(int(self.time_limit.get()))
        self.stdin.focus_set()
        if d.isAlive():
            self.stderr.insert('1.0', '[Time Limit Exceeded]\n')
            p2 = subprocess.Popen(
                'taskkill /im {} /f /t'.format(os.path.basename(exec_name)),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
            )
            stdout, stderr = p2.communicate()
            self.stderr.insert('end', '[TERMINATED]')
            self.stdin.focus_set()

        self.stdin.focus_set()
