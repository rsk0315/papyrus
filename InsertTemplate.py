import os

class InsertTemplate(object):
    menudefs = [
        ('edit', [
            ('Insert Template', '<<insert-template>>'),
        ])
    ]

    def __init__(self, editwin=None):
        self.editwin = editwin
        if editwin is None:
            return

        self.text = editwin.text
        self.text.bind('<<insert-template>>', self.insert_template)

    def insert_template(self, event=None):
        if hasattr(self.editwin, 'ext'):
            ext = self.editwin.ext
        else:
            return

        template_text = ''
        idlelib_path = os.path.dirname(__file__)
        template_path = os.path.join(idlelib_path, 'templates')
        template_file = os.path.join(template_path, ext[1:]+'.tpl')
        try:
            with open(template_file) as fin:
                template_text = fin.read()
        except:
            return

        self.text.insert('1.0', template_text)
