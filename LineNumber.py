"""LineNumber - Extension to display the number of line leftward the edit window

"""
import Tkinter
from Tkconstants import TOP, LEFT, X, W, SUNKEN, N, Y, RIGHT
import re
import math
from sys import maxint as INFINITY
from idlelib.configHandler import idleConf

UPDATEINTERVAL = 50 # ms
FONTUPDATEINTERVAL = 1000 # ms

class LineNumber:
    menudefs = [('options', [('!Line _Number', '<<toggle-line-number>>')])]
    digit = 4
    bgcolor = idleConf.GetOption('extensions', 'LineNumber',
                                 'bgcolor', type='str', default='White')
    fgcolor = idleConf.GetOption('extensions', 'LineNumber',
                                 'fgcolor', type='str', default='Black')

    def __init__(self, editwin):
        self.editwin = editwin
        self.text = editwin.text
        self.textfont = self.text['font']
        self.label = None
        self.info = [(0, -1, '', False)]

        self.topvisible = 1
        self.bottomvisible = 1
        visible = idleConf.GetOption('extensions', 'LineNumber',
                                     'visible', type='bool', default=False)
        if visible:
            self.toggle_line_number_event()
            self.editwin.setvar('<<toggle-line-number>>', True)
        self.text.after(UPDATEINTERVAL, self.timer_event)
        self.text.after(FONTUPDATEINTERVAL, self.font_timer_event)

    def toggle_line_number_event(self, event=None):
        if not self.label:
            widgets = self.editwin.text, self.editwin.text_frame
            pady = 0
            for widget in widgets:
                pady += int(str( widget.pack_info()['pady'] ))
                pady += int(str( widget.cget('pady') ))

            border = 0
            for widget in widgets:
                border += int(str( widget.cget('border') ))
            self.label = Tkinter.Label(self.editwin.top,
##                                       text='\n'.join(['%d'%(i+1) for i in range(50)]),
                                       text='1',
                                       anchor=N, justify=RIGHT,
                                       font=self.textfont,
                                       bg=self.bgcolor, fg=self.fgcolor,
                                       width=self.digit,
                                       pady=pady, border=border,
                                       relief=SUNKEN)
            self.label.pack(side=LEFT, fill=Y, expand=False,
                            before=self.editwin.text_frame)
            
        else:
            self.label.destroy()
            self.label = None
        idleConf.SetOption('extensions', 'LineNumber', 'visible',
                           str(self.label is not None))
        idleConf.SaveUserCfgFiles()

    def timer_event(self):
        if self.label:
            self.update_line_number()
        self.text.after(UPDATEINTERVAL, self.timer_event)

    def font_timer_event(self):
        newtextfont = self.text["font"]
        if self.label and newtextfont != self.textfont:
            self.textfont = newtextfont
            self.label["font"] = self.textfont
        self.text.after(FONTUPDATEINTERVAL, self.font_timer_event)

    def update_line_number(self):
        topvisible = int(self.text.index('@0,0').split('.')[0])
        bottomvisible = int(self.text.index('@0,%s'%INFINITY).split('.')[0])
##        print bottomvisible - topvisible,
##        print self.bottomvisible - self.topvisible,
##        topvisible = int(math.ceil(float(self.text.index('@0,0'))))
##        bottomvisible = int(math.ceil(float(self.text.index('@0,16383'))))
##        print self.text.index('@0,0'),
##        print bottomvisible,
        if self.bottomvisible == bottomvisible:
            return

        self.label['text'] = '\n'.join(
            ['%d'%i for i in range(topvisible,
##                                   min(topvisible+39, bottomvisible)+1)]
                                   bottomvisible+1)]
        )

##        if min(topvisible+50, bottomvisible) >= 999:
####            self.label['width'] = len(str(min(topvisible+39, bottomvisible)+1))+1
##            self.label['width'] = len(str(bottomvisible))+1

        self.label['height'] = 1
        self.label['width'] = max(len(str(bottomvisible))+1, 4)

        self.topvisible = topvisible
        self.bottomvisible = bottomvisible
