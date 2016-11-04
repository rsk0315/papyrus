import os
import tkSimpleDialog
from idlelib.configHandler import idleConf
from ScrolledText import ScrolledText
from Tkinter import *
from tkMessageBox import *

class EditSnippet(object):
    def __init__(self, editwin=None):
        self.editwin = editwin
        if editwin is None:
            return

        self.text = editwin.text
        self.io = editwin.io
        self.text.bind('<<edit-snippet>>', self.edit_snippet)
        self.n = IntVar()
        self.n.set(0)

    def edit_snippet(self, event=None):
        try:
            name = self.text.get('self.first', 'sel.last')
        except TclError:
            name = ''
        else:
            name = name.strip()

        name = tkSimpleDialog.askstring(
            'Snippet',
            'Enter the name of a snippet file\n'
            'to search on idlelib/snippets and open:',
            parent=self.text, initialvalue=name
        )

        if name:
            name = name.strip()
        if not name:
            return

        path = self.complete_name(name)
        idlelib_path = os.path.dirname(__file__)
        snippet_path = os.path.join(idlelib_path, 'snippets')
        if path is True:
            path = os.path.join(snippet_path, name)
            with open(path, 'w'):
                # just make file
                pass
        elif path is False:
            return None

        if self.editwin.flist:
            self.editwin.flist.open(path)
        else:
            self.io.loadfile(path)

        return path

    def complete_name(self, name):
        idlelib_path = os.path.dirname(__file__)
        snippet_path = os.path.join(idlelib_path, 'snippets')
        self.files = files = [
            f for f in os.listdir(snippet_path)
            if (
                os.path.isfile(os.path.join(snippet_path, f))
                and f.startswith(name)
            )
        ]
        self.path = ''

        if not files:
##            showerror(
##                title='Cannot open snippet',
##                message='Please specify the file name.'
##            )
            q = askyesno(
                title='Cannot specify the name',
                message='Create the new file?'
            )
            if q:
                return True
            else:
                self.text.focus_set()
                return False

        self.path = files[0]
        return os.path.join(snippet_path, self.path)

    def _complete(self, clist, event=None):
        self.path = path = self.files[self.n.get()]
        if self.editwin.flist:
            self.editwin.flist.open(path)
        else:
            self.io.loadfile(path)

        self._close(clist)

    def _close(self, window, event=None):
        def _c(window_, event):
            window_.grab_release()
            window_.withdraw()

        if window is not None:
            _c(window, event)

        window = None

