import os
import subprocess
import tkMessageBox
import threading
from ScrolledText import ScrolledText
from Tkinter import *
from idlelib.configHandler import idleConf

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

        if f in ('C/l',):
            compiler = 'gcc'
            command = idleConf.GetOption('extensions', 'CompileCode', 'compile_c')
        elif f in ('C++/l',):
            compiler = 'g++'
            command = idleConf.GetOption('extensions', 'CompileCode', 'compile_cpp')
        else:
            return

        def close_(w, event=None):
            w.grab_release()
            w.withdraw()

        raw_name = os.path.splitext(filename)[0]
        exe_name = raw_name+'.exe'
        basename = os.path.basename(filename)

        args = command.format(raw_name)

        sub_win = Toplevel(self.text)
        sub_win.title('In compilation')

        ce = ScrolledText(
            sub_win, width=80, height=24,
            fg='#b7b7b7', bg='black', font='Consolas 10',
            insertbackground='white',
        )

        ce.bind('<Escape>', lambda event: close_(sub_win, event))
        ce.pack(fill='both', expand=True)
        ce.focus_set()
        
        def compile_():
            sp = subprocess.Popen(
                args, stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
            )
            self.compile_failed = compile_failed = sp.wait()
            compile_message = sp.communicate()[1]
            compile_message = re.sub(
                r'^{}:'.format(filename.replace('\\', r'\\')),
                basename+':',
                compile_message,
                flags=re.M,
            )
            self.compile_message = compile_message

            if not compile_message:
                return

            if compile_failed:
                title = 'Compilation failed'
            else:
                title = 'Compilation succeeded (with warning)'

            sub_win.title(title)

##            ce.insert('1.0', compile_message)
##            ce.focus_set()

        d = threading.Thread(name='comp', target=compile_)
        d.start()
        d.join(6)
        if d.is_alive():
            p = subprocess.Popen(
                'taskkill /im {} /f /t'.format(compiler),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
            )
            stdout, stderr = p.communicate()

        if not self.compile_message:
            close_(sub_win, None)
            tkMessageBox.showinfo(
                parent=self.text,
                title=compiler,
                message='Compilation succeeded.',
            )
        else:
            ce.insert('end', self.compile_message)

        ce.focus_set()
