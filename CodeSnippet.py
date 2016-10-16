import os
import re

from idlelib.configHandler import idleConf

import __main__

class CodeSnippet(object):
    menudefs = [
        ('edit', [
            ('Insert Code Snippet', '<<code-snippet>>'),
        ])
    ]

    def __init__(self, editwin=None):
        self.editwin = editwin
        if editwin is None:
            return

        self.text = editwin.text
        self.text.bind('<<code-snippet>>', self.complete_event)

    def complete_event(self, event=None):
        curline = self.text.get('insert linestart', 'insert')
        query = curline.strip()
        if re.search(r'[ \t]|^$', query):
            return

        sdir, sbase = os.path.split(query)

        indent = re.search(r'[ \t]*', curline).group()

        idlelib_path = os.path.dirname(__file__)
        snippet_path = os.path.join(idlelib_path, 'snippets', sdir)
        snippet_files = [
            f for f in os.listdir(snippet_path)
            if os.path.isfile(os.path.join(snippet_path, f))
        ]
        if hasattr(self.editwin, 'ext'):
            ext = self.editwin.ext or ''
        else:
            ext = ''

        snippet = ''
        if sbase+ext in snippet_files:
            snippet_file = os.path.join(snippet_path, sbase+ext)
        else:
            candidate = [s for s in snippet_files if s.startswith(sbase)]
            # todo for auto-completion
            if len(candidate) == 1:
                snippet_file = os.path.join(snippet_path, candidate[0])
            else:
                return

        snippet = open(snippet_file).read().rstrip()
        if indent:
            snippet = ('\n'+indent).join(re.split(r'[\r\n]', snippet))

        if not snippet.endswith('\n'):
            snippet += '\n'

        snippet += indent
                

        self.text.delete('insert linestart', 'insert lineend')
        self.text.insert('insert linestart', indent+snippet)
