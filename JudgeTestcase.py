import cookielib
import os
import re
import subprocess
import threading
import urllib2
from ScrolledText import ScrolledText
from Tkinter import *

class JudgeWindow(ScrolledText):
    def __init__(self, name, close_func, parent=None, **kwargs):
        self.parent = parent
        frame = LabelFrame(parent, text=name)
        ScrolledText.__init__(self, frame, **kwargs)
        self.bind('<Escape>', lambda e: close_func(e))

        self.pack(fill='both', expand=True)
        frame.pack(fill='both', expand=True)

class JudgeTestcase(object):
    IO_PROG = (
        r'<h\d[^>]*>'
        r'{}\s*'
        r'(?P<INDEX>\d+)'
        r'</h\d>\s*(?:<section[^>]*>\s*)?<pre[^>]*>\s*'
        r'(?P<IO>[^<]*)'
        r'</pre>'
    )
    IN_PROG = re.compile(
        IO_PROG.format(r'.*\xe5\x85\xa5\xe5\x8a\x9b\xe4\xbe\x8b')
    )
    OUT_PROG = re.compile(
        IO_PROG.format(r'.*\xe5\x87\xba\xe5\x8a\x9b\xe4\xbe\x8b')
    )
    TL_PROG = re.compile(
        r'(?P<TL>\d+(?:\.\d+)?)\s*sec'
    )

    GRAY = '#999999'
    GREEN = '#468847'
    ORANGE = '#f89406'

    menudefs = [
        ('run', [
            ('Judge testcase', '<<judge-testcase>>'),
        ])
    ]

    def __init__(self, editwin=None):
        self.editwin = editwin

        self.subwin = self.judgewindow = None
        self.cpp14 = IntVar()
        self.cpp14.set(1)
        self.tl = StringVar()
        self.tl.set('')
        self.status = StringVar()
        self.status.set('')

        self.url = StringVar()

        self.cin = ''
        self.cout = ''
        self.cerr = ''
        self.timelimit = 2

        if editwin is None:
            self.url.set('')
            return

        self.io = self.editwin.io
        self.text = self.editwin.text
        self.text.bind('<<judge-testcase>>', self.open_window)

        self.opener = urllib2.build_opener()
        self.username = StringVar()
        self.passwd = StringVar()
        self.logged_in = False

    def login(self, name, passwd):
        self.opener.add_handler(
            urllib2.HTTPCookieProcessor(cookielib.CookieJar())
        )
        url = 'https://practice.contest.atcoder.jp/login'
        req = urllib2.Request(
            url, 'name={}&password={}'.format(name, passwd)
        )
        self.opener.add_handler(
            urllib2.HTTPCookieProcessor(cookielib.CookieJar())
        )
##        print (name, passwd)
        html = self.opener.open(req).read()
        if 'practice contest\n - practice contest | AtCoder' in html:
            print 'Signed in successfully'
            self.logged_in = True
        elif 'Sign in - practice contest | AtCoder' in html:
            print 'Failed to sign in'
            self.logged_in = False

    def get_timelimit(self, url):
        html = self.opener.open(url).read()
        tl = JudgeTestcase.TL_PROG.search(html)
        if tl:
            self.tl.set(tl.group('TL'))
            self.text.update_idletasks()
            self.timelimit = float(self.tl.get())

    def get_testcases(self, url):
        name = self.name_entry.get()
        passwd = self.passwd_entry.get()

        if (not self.logged_in) and (name and passwd):
            self.login(name, passwd)

        html = self.opener.open(url).read()
##        print html.decode('utf-8').encode('cp932', 'ignore')
        input_ = dict(JudgeTestcase.IN_PROG.findall(html))
        output = dict(JudgeTestcase.OUT_PROG.findall(html))

        print url
        print input_, output

        testcases = [
            (input_.get(str(i), None), output.get(str(i), None))
            for i in range(1, 1+min(map(len, [input_, output])))
            if (str(i) in input_) and (str(i) in output)
        ]

        return testcases

    def run_code(self, input_='', expected_output='', exe_name=None):
        expected_output = expected_output.replace('\r\n', '\n')
        expected_output = expected_output.replace('\r', '\n')
        expected_output = re.sub(
            r'^\s+', '', expected_output, flags=re.M
        ).rstrip('\n') + '\n'
        if exe_name is None:
            exe_name = os.path.splitext(self.io.filename)[0]+'.exe'

        def run_exe():
            p = subprocess.Popen(
                exe_name, shell=True,
                stdin = subprocess.PIPE,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
            )
            self.cout, self.cerr = p.communicate(input_)

        d = threading.Thread(name='judge', target=run_exe)
        d.start()
        d.join(self.timelimit)

        if d.is_alive():
            p = subprocess.Popen(
                'taskkill /im {} /f /t'.format(
                    os.path.basename(exe_name)
                ),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
            )
            p.communicate()
            return 'TLE'

        self.cout = self.cout.replace('\r\n', '\n')
        self.cout = self.cout.replace('\r', '\n')

        print `self.cout`, `expected_output`
        if self.cout == expected_output:
            return 'AC'
        elif self.cout + '\n' == expected_output:
            return 'PE'
        elif 'float_error_check':
            s = self.check_float_error(expected_output)
            if s == 1:
                return 'AC'
            elif s == -1:
                return 'PE'

        return 'WA'

    def check_float_error(self, expected_output):
        print 'started checking float error'
        cout = self.cout.split()
        xout = expected_output.split()

        if len(cout) != len(xout):
            return 0

        for cf, xf in zip(cout, xout):
            try:
                cf, xf = map(float, (cf, xf))
            except (TypeError, ValueError) as e:
                print e, cf, xf
                if cf != xf:
                    print 'WAed'
                    return 0
                else:
                    print 'str'
                    continue

            if not (abs(cf-xf)<1e-6 or (xf and abs((cf-xf)/xf)<1e-6)):
                return 0

        if self.cout.endswith('\n'):
            return 1
        else:
            return -1

    def judge_testcase(self, event=None):
        if self.subwin is None:
            self.open_window()
            return

        try:
            self.judgewindow.focus_set()
        except TclError:
            self.open_window()
            return

        self.judgewindow.delete('1.0', 'end')
        self.status.set('WJ')
        self.result.config(background=JudgeTestcase.GRAY)
        self.judgewindow.update_idletasks()

        url = self.url.get()
##        print url
        if not url:
            return

        self.get_timelimit(url)
        testcases = self.get_testcases(url)
##        print testcases
        status = {'AC': 0, 'WA': 0, 'TLE': 0, 'PE': 0}
        for idx, (in_, out) in enumerate(testcases):
            result = self.run_code(in_, out)
            status[result] += 1
            judgestr = 'Case {}: {}'.format(idx+1, result)
            self.judgewindow.insert('end', judgestr+'\n')
            self.judgewindow.update_idletasks()

        for s in ('TLE', 'WA', 'PE'):
            if status[s]:
                self.status.set(s)
                self.result.config(background=JudgeTestcase.ORANGE)
                return

        self.status.set('AC')
        self.result.config(background=JudgeTestcase.GREEN)
        self.judgewindow.focus_set()

    def guess_url(self):
        name = self.io.filename
        if name is None:
            return ''

        m = re.search(
            r'(?P<CONT>a[a-z]c)(?P<IDX>\d+)_(?P<PROB>[a-z])',
            os.path.basename(name)
        )
        if m:
            cont = cont_ = m.group('CONT')
            idx = idx_ = int(m.group('IDX'))
            prob = m.group('PROB')

            if (cont=='abc' and idx<=19 or cont=='arc' and idx<=34):
                prob = chr(ord(prob)-ord('a')+ord('1'))
            elif (cont=='abc' and idx>=42 and ord(prob)>=ord('c')):
                cont_ = 'arc'
                idx_ += 16
                prob = chr(ord(prob)-2)

            return (
                'http://{}{:0>3}.contest.atcoder.jp/tasks/{}{:0>3}_{}'
            ).format(cont, idx, cont_, idx_, prob)
        else:
            return ''

    def open_window(self, event=None):
        try:
            if self.subwin:
                self.subwin.focus_set()
                return
        except TclError:
            pass

        self.subwin = Toplevel(self.text)
        self.subwin.title('Judge testcase')
        self.url.set(self.guess_url())

        frame = Frame(self.subwin, width=20, height=10)

        cframe = LabelFrame(frame, text='Compilation', width=19)
        cbutton = Button(cframe, text='Compile', command=self.compile_)
        cbutton.pack(expand=True, side='left', anchor='sw')
        ccheckb = Checkbutton(cframe, text='C++14', variable=self.cpp14)
        ccheckb.pack(side='left', anchor='se')

        eframe = LabelFrame(frame, text='Judgment', width=19)
        ebutton = Button(eframe, text='Judge', command=self.judge_testcase)
        ebutton.pack(expand=True, side='left', anchor='sw')
        eeframe = LabelFrame(eframe, text='Time Limit', width=3)
        fstr = str(self.timelimit).replace('.0', '')
        self.tl.set(fstr)

        eentry = Entry(eeframe, textvariable=self.tl, width=8)
        eentry.pack(side='left')
        elabel = Label(eeframe, text='sec', width=3)
        elabel.pack(side='right')
        eeframe.pack(fill='both', expand=True, side='right')

        eframe.pack(fill='both', expand=True, side='right')
        cframe.pack(fill='both', expand=True, side='right')
        frame.pack(fill='both', expand=True, side='top')

        taskframe = LabelFrame(
            self.subwin, text='Task URL', width=38,
        )
        self.task_url = Entry(
            taskframe, textvariable=self.url,
            fg='white', bg='black', insertbackground='white',
            width=38, font='Consolas 10',
        )
        self.task_url.pack(fill='both', expand=True, side='top')
        taskframe.pack(fill='both', expand=True, side='top')

        authframe = LabelFrame(
            self.subwin, text='Authentication (optional)',
        )
        nameframe = LabelFrame(authframe, text='Username')
        self.name_entry = Entry(
            nameframe, textvariable=self.username,
            fg='white', bg='black', insertbackground='white',
            width=18, font='Consolas 10',
        )
        self.name_entry.pack(expand=True, fill='both')

        passwdframe = LabelFrame(authframe, text='Password')
        self.passwd_entry = Entry(
            passwdframe, textvariable=self.passwd,
            fg='white', bg='black', insertbackground='white',
            width=18, font='Consolas 10', show='*',
        )
        self.passwd_entry.pack(expand=True, fill='both')

        nameframe.pack(expand=True, fill='both', side='left')
        passwdframe.pack(expand=True, fill='both', side='right')
        authframe.pack(expand=True, fill='both', side='top')


        self.judgewindow = JudgeWindow(
            'Judge status', self.close_window, self.subwin,
            fg='white', bg='black', insertbackground='white',
            width=20, height=6, font='Consolas 10',
        )
        self.judgewindow.bind('<Control-Key-Return>', self.judge_testcase)
        self.judgewindow.pack(fill='x', expand=True, side='top')

        resultframe = LabelFrame(
            self.subwin, text='Result', width=3, height=1,
        )
        self.result = Entry(
            resultframe, textvariable=self.status,
            fg='white', bg='black', insertbackground='white',
            width=6, font='Consolas 10',
        )
        self.result.pack(expand=True, side='top')
        resultframe.pack(expand=True, side='top')

        self.judgewindow.focus_set()

    def close_window(self, event=None):
        def _close(window, event):
            window.grab_release()
            window.withdraw()

        if self.subwin is not None:
            _close(self.subwin, event)

        self.subwin = None

    def compile_(self, event=None):
        if self.io.filename is None:
            return

        exe_name = os.path.splitext(self.io.filename)[0]+'.exe'

        def run_compiler():
            if not hasattr(self.editwin, 'ext'):
                return

            try:
                f = self.editwin.ftype.get()
            except (AttributeError,):
                return

            if f not in ('C++/l',):
                return

            cc = 'g++ -Wall -o {} {} -O2'.format(
                exe_name, self.io.filename,
            )
            if self.cpp14.get():
                cc += ' --std=c++14'
            else:
                cc += ' --std=c++98'

            p = subprocess.Popen(
                cc,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
            )
            compile_failed = p.wait()
            self.judgewindow.delete('1.0', 'end')
            if compile_failed:
                self.status.set('CE')
                self.result.config(background=JudgeTestcase.ORANGE)
            else:
                self.status.set('')
                self.result.config(background='black')

        d = threading.Thread(name='compile', target=run_compiler)
        d.start()
        d.join(6)
        if d.is_alive():
            p = subprocess.Popen(
                'taskkill /im g++ /f /t',
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
            )
            p.communicate()


if __name__ == '__main__':
    judge = JudgeTestcase()
    tc = judge.get_testcases('http://abc042.contest.atcoder.jp/tasks/abc042_a')
    print tc
