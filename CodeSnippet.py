import os
import re

from idlelib.configHandler import idleConf

import __main__

class CodeSnippet(object):
    menudefs = [
        ('edit', [
            ('Complete Code Snippet', '<<code-snippet>>'),
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

        indent = re.search(r'[ \t]*', curline).group()

        idlelib_path = os.path.dirname(__file__)
        snippet_path = os.path.join(idlelib_path, 'snippets')
        snippet_files = os.listdir(snippet_path)
        if hasattr(self.editwin, 'ext'):
            ext = self.editwin.ext or ''
        else:
            ext = ''

        snippet = ''
        if query+ext in snippet_files:
            snippet = open(os.path.join(snippet_path, query+ext)).read()
            if indent:
                snippet = ('\n'+indent).join(re.split(r'[\r\n]', snippet))

            if not snippet.endswith('\n'):
                snippet += '\n'

            snippet += indent
                
        elif any([s for s in snippet_files if s.startswith(query)]):
            # todo for auto-completion
            return
        else:
            return

        self.text.delete('insert linestart', 'insert lineend')
        self.text.insert('insert linestart', indent+snippet)
