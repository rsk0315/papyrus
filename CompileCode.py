import os
import subprocess
import tkMessageBox
from ScrolledText import ScrolledText
from Tkinter import *

class CompileCode(object):
    menudefs = [
        ('run', [
            ('Compile Code', '<<compile-code>>'),
        ])
    ]

    def __init__(self, editwin=None):
        self.editwin = editwin
        if editwin is None:
            return

        self.text = editwin.text
        self.text.bind('<<compile-code>>', self.compile_code)

    def compile_code(self, event=None):
        if not hasattr(self.editwin.io, 'filename') or self.editwin.io.filename is None:
            return

        filename = self.editwin.io.filename
        try:
            f = self.editwin.ftype.get()
        except:
            return

        if f in ('C/l Abbrev',):
            compiler = 'gcc'
        elif f in ('C++/l Abbrev',):
            compiler = 'g++'
        else:
            return

        exe_name = os.path.splitext(filename)[0]+'.exe'
        basename = os.path.basename(filename)
        args = [compiler, '-O2', '-Wall', '-o', exe_name, filename]
        if compiler == 'gcc':
            args += ['-lm']  # todo

        sp = subprocess.Popen(
            args, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        compile_failed = sp.wait()
        compile_message = sp.communicate()[1]
        compile_message = re.sub(
            r'^{}:'.format(filename.replace('\\', r'\\')),
            basename+':',
            compile_message,
            flags=re.M,
        )

        if not compile_message:
            tkMessageBox.showinfo(
                parent=self.text,
                title=compiler,
                message='Compilation succeeded.',
            )
            return

        sub_win = Toplevel(self.text)

        if compile_failed:
            title = 'Compilation failed'
        else:
            title = 'Compilation succeeded (with warning)'

        sub_win.title(title)

        ce = ScrolledText(
            sub_win, width=80, height=24,
            fg='white', bg='black', font='Consolas 10',
            insertbackground='white',
        )
        def close_(w, event=None):
            w.grab_release()
            w.withdraw()

        ce.bind('<Escape>', lambda event: close_(sub_win, event))
        ce.pack(fill='both', expand=True)
        ce.insert('1.0', compile_message)
        ce.focus_set()
