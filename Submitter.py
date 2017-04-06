import os
import subprocess
import tkSimpleDialog
import threading
import ttk
import urllib
import urllib2
from idlelib.configHandler import idleConf
from Tkinter import *
from ScrolledText import ScrolledText

import mechanize
import regex

class tkPulldown(ttk.Combobox):
    def __init__(self, parent, values, init=0, **kwargs):
        ttk.Combobox.__init__(self, parent, **kwargs)
        self['values'] = values
        self.current(init)
##        self.grid(row=0, column=0, columnspan=10)
        self.configure(
            state='readonly',
        )

class Submitter(object):
    menudefs = [
        ('run', [
            ('Test and submit', '<<test-and-submit>>'),
        ])
    ]

    def __init__(self, editwin=None):
        self.editwin = editwin
        if editwin is None:
            return

        self.text = editwin.text
        self.io = editwin.io
        self.text.bind('<<test-and-submit>>', self.open_tester)
        self.subwin = None

        try:
            f = self.editwin.ftype.get()
        except:
            f = 'xxx'

    def open_tester(self, event=None):
        if self.subwin is not None:
            self.username_entry.focus_set()
            return

        self.subwin = Toplevel(self.text)
        self.subwin.title('AtCoder submitter')

        self.subwin.bind('<Escape>', self.close_tester)
        self.subwin.bind('<Key-F9>', lambda e: self.text.focus_set())

        self.browser = mechanize.Browser()
        self.browser.set_handle_robots(False)
        self.logged_in = False

        self.username = StringVar()
        self.password = StringVar()
        self.contesturl = StringVar(value='https://')
        self.taskname = StringVar()
        self.language = StringVar()
        self.status = StringVar()
        self.init_tester()

    def init_tester(self):
        if self.subwin is None:
            return

        self.pack_loginform()
        self.pack_submitform()
        self.pack_actions()
        self.pack_details()

    def pack_loginform(self):
        login_info = Frame(self.subwin)

        # Username
        username_frame = LabelFrame(login_info, text='Username')
        self.username_entry = Entry(
            username_frame, textvariable=self.username,
        )
        self.username_entry.pack(side='left')
        username_frame.pack(side='left')

        # Password
        password_frame = LabelFrame(login_info, text='Password')
        self.password_entry = Entry(
            password_frame, textvariable=self.password, show='*',
        )
        self.password_entry.pack(side='left')
        password_frame.pack(side='left')

        login_info.pack(side='top')
        self.username_entry.focus_set()

    def pack_submitform(self):
        submit_info = Frame(self.subwin)

        # Contest URL
        url_frame = LabelFrame(
            submit_info, text='Contest page (https://***.contest.atcoder.jp/)',
        )
        self.url_entry = Entry(
            url_frame, textvariable=self.contesturl, width=42,
        )
        self.url_entry.pack(side='left')
        url_frame.pack(side='top')

        # Task
        task_frame = LabelFrame(submit_info, text='Task name')
        self.task_pdown = tkPulldown(
            task_frame, [''], init=0, width=31,
        )
        self.task_pdown.pack(side='left', fill='x')
        task_reload = Button(
            task_frame, text='Reload', command=self.reload_task
        )
        task_reload.pack(side='left', anchor='ne')
        task_frame.pack(side='top')

        # Language
        lang_frame = LabelFrame(submit_info, text='Language')
        self.lang_pdown = tkPulldown(
            lang_frame, [''], init=0, width=31,
        )
        self.lang_pdown.pack(side='left', fill='x')
        lang_reload = Button(
            lang_frame, text='Reload', command=self.reload_lang
        )
        lang_reload.pack(side='left', anchor='ne')
        lang_frame.pack(side='top')

        submit_info.pack(side='top')

    def pack_actions(self):
        actions_frame = Frame(self.subwin)

        buttons_frame = LabelFrame(actions_frame, text='Actions')
        Button(buttons_frame, text='Compile').pack(side='left')
        Button(buttons_frame, text='Sample').pack(side='left')
        Button(buttons_frame, text='Submit', command=self.submit).pack(side='left')
        buttons_frame.pack(side='left', fill='x')

        status_frame = LabelFrame(actions_frame, text='Status')
        Entry(status_frame, textvariable=self.status, width=14).pack(side='right')
        status_frame.pack(side='right', fill='x')

        actions_frame.pack(side='top', fill='x')

    def pack_details(self):
        detail_frame = LabelFrame(self.subwin, text='Test/Judge detail')

        self.detail = ScrolledText(
            detail_frame, width=39, height=16,
            font=('Segoe UI', 9),
        )
        self.detail.pack()
        detail_frame.pack(side='top')

    def reload_task(self):
        self.contesturl.set('https://practice.contest.atcoder.jp/')
        self.subwin.update_idletasks()

        self.login()

        url = urllib.basejoin(self.contesturl.get(), '/submit')
        self.browser.open(url)
        self.browser.select_form(nr=0)

        ctrl = self.browser.controls[1]
        if ctrl.id != 'submit-task-selector' or ctrl.name != 'task_id':
            return

##        self.task_dict = dict(
##            (ctrl.get_item_attrs(i.name)['contents'], i.name)
##            for i in ctrl.items
##        )

        tasks = [ctrl.get_item_attrs(i.name)['contents'] for i in ctrl.items]

        self.task_pdown['values'] = tasks
        self.task_pdown.current(0)  # todo guess from filename

    def reload_lang(self):
        self.reload_task()
        self.subwin.update_idletasks()

##        task_id = self.task_dict.get(self.task_pdown.get(), None)
##        if task_id is None:
##            return
        index = self.task_pdown.current()
        task_id = self.browser.controls[1].items[index].name
        print index

        ctrl = self.browser.controls[2+index]
        if (ctrl.id != 'submit-language-selector-'+task_id or
                ctrl.name != 'language_id_'+task_id):
            return

##        self.lang_dict = dict([
##            (ctrl.get_item_attrs(i.name)['contents'], i.name)
##            for i in ctrl.items
##        ])

        langs = [ctrl.get_item_attrs(i.name)['contents'] for i in ctrl.items]

        self.lang_pdown['values'] = langs
        self.lang_pdown.current(0)  # todo guess from filename

    def close_tester(self, event=None):
        if self.subwin is not None:
            self.subwin.grab_release()
            self.subwin.withdraw()

            self.subwin = None
            self.logout()

    # AtCoder agent
    def login(self):
        if self.logged_in:
            return

        self.browser.open('https://practice.contest.atcoder.jp/login')
        self.browser.select_form(nr=0)
        self.browser['name'] = self.username.get()
        self.browser['password'] = self.password.get()

        self.browser.submit()
        self.logged_in = True  # todo more check

    def submit(self):
        url = urllib.basejoin(self.contesturl.get(), '/submit')
        try:
            self.browser.open(url)
            self.browser.select_form(nr=0)
        except mechanize._mechanize.FormNotFoundError:
            print 'not found error'
            return

        self.select_task()
        self.select_lang()

        src = self.text.get('1.0', 'end')
        if not src.strip():
            return

        self.browser.form.set_value(src, 'source_code')

##        return
        response = self.browser.submit()

        url = response.geturl()
        detail_link = self.find_latest_submit(url)
        request = self.browser.click_link(detail_link)
        response = self.browser.open(request)
        self.wait(response.geturl())

    def select_task(self):
        ctrl = self.browser.controls[1]
        ctrl.set(ctrl.name, ctrl.items[self.task_pdown.current()].name)

    def select_lang(self):
        ctrl = self.browser.controls[2+self.lang_pdown.current()]
        ctrl.set(ctrl.name, ctrl.items[self.lang_pdown.current()].name)

    def find_latest_submit(url):
        self.browser.open(url)
        for link in self.browser.links():
            if 'Details' in link.text:
                return link

    def wait(url):
        # waits for judge finishing and shows the result
        pass
