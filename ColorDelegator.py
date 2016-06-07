import time
import re
import keyword
import __builtin__
from idlelib.Delegator import Delegator
from idlelib.configHandler import idleConf

try:
    import regex
except ImportError:
    import re as regex


DEBUG = False

ALTERNATE_TAGS = {
    'SP_VARIABLE': None,
    'FORMAT': 'BUILTIN',
    'SPECIAL': 'BUILTIN',
    'SPECIAL_M': 'BUILTIN',
    'CONSTANT': 'BULITIN',
    'OPERATOR': 'KEYWORD',
    'CLASSDEF': 'DEFINITION',
    'FUNCDEF': 'DEFINITION',
    'STRING_PREFIX': 'KEYWORD',
    'PREPROCESSOR': 'KEYWORD',
    'SHARP': None,
    'PUNC': None,
    'RE_SGL': 'BUILTIN',
    'RE_REPEAT': 'KEYWORD',
    'RE_PAR': 'STRING',
    'RE_NAME': 'STRING',
    'RE_PAR': 'STRING',
    'RE_PARENTHESIS': 'KEYWORD',
    'RE_BRACKET': 'BUILTIN',
    'RE_CARET': 'KEYWORD',
    'RE_CHARS': 'BUILTIN',
    'RE_SPACIAL': 'STRING',
}

def any(name, alternates):
    "Return a named group pattern matching list of alternates."
    return "(?P<%s>" % name + "|".join(alternates) + ")"

def altext(ext):
    alternates = {
        '.pyw': '.py',
        '.h': '.c',
        '.hpp': '.cpp',
        '.rbw': '.rb',
        '.htm': '.html',
        '.xml': '.html',
        '.plist': '.html',
        '.svg': '.html',
    }
    return alternates.get(ext, ext)

def unify(*patterns):
    unified_pattern = ''
    for pattern in patterns:
        try:
            prog = regex.compile(pattern)
        except Exception as e:
            continue

        if prog.search(''):
            continue

        if unified_pattern:
            unified_pattern += r'|'

        unified_pattern += pattern
    return unified_pattern

def make_pat(ext):
    try:
        lang = getattr(__import__('languages'+ext), ext[1:])
    except ImportError:
        return ''
    except Exception as e:
        return ''

    try:
        keyword = lang.KEYWORD
        builtin = lang.BUILTIN
        comment = lang.COMMENT
        string = lang.STRING
        definition = lang.DEFINITION
    except AttributeError:
        return ''

    if hasattr(lang, 'MISC'):
        misc = lang.MISC
    else:
        misc = ''

    return unify(
        string,
        keyword,
        comment,
        definition,
        builtin,
        misc,
        any('SYNC', [r'\n']),
    )


class ColorDelegator(Delegator):

    def __init__(self, ext):
        Delegator.__init__(self)
        self.ext = altext(ext)
        self.prog = regex.compile(make_pat(ext), flags=regex.S)
#
        try:
            self.lang = getattr(__import__('languages'+ext), ext[1:])
            if hasattr(self.lang, 'read_twice'):
                self.read_twice = self.lang.read_twice
            else:
                self.read_twice = None
        except Exception as e:
            self.lang = None
            self.read_twice = None
        finally:
            self.LoadTagDefs()


    def setdelegate(self, delegate):
        if self.delegate is not None:
            self.unbind("<<toggle-auto-coloring>>")
        Delegator.setdelegate(self, delegate)
        if delegate is not None:
            self.config_colors()
            self.bind("<<toggle-auto-coloring>>", self.toggle_colorize_event)
            self.notify_range("1.0", "end")
        else:
            # No delegate - stop any colorizing
            self.stop_colorizing = True
            self.allow_colorizing = False

    def config_colors(self):
        for tag, cnf in self.tagdefs.items():
            if cnf:
                self.tag_configure(tag, **cnf)
        self.tag_raise('sel')

    def LoadTagDefs(self):
        theme = idleConf.CurrentTheme()
        font = idleConf.GetOption('main', 'EditorWindow', 'font')
        self.tagdefs = {
            "COMMENT": idleConf.GetHighlight(theme, "comment"),
            "KEYWORD": idleConf.GetHighlight(theme, "keyword"),
            "BUILTIN": idleConf.GetHighlight(theme, "builtin"),
            "STRING": idleConf.GetHighlight(theme, "string"),
            "DEFINITION": idleConf.GetHighlight(theme, "definition"),
            "SYNC": {'background':None,'foreground':None},
            "TODO": {'background':None,'foreground':None},
            "ERROR": idleConf.GetHighlight(theme, "error"),
            # The following is used by ReplaceDialog:
            "hit": idleConf.GetHighlight(theme, "hit"),
            }

        if DEBUG: print 'tagdefs',self.tagdefs

        try:
            lang = getattr(__import__('languages'+self.ext), self.ext[1:])
            if hasattr(lang, 'append_tags'):
                for key, value in lang.append_tags.items():
                    self.tagdefs[key] = value
        except (ImportError, AttributeError):
            pass

        def _style(string):
            list_ = []
            for c in string:
                if c == 'b':
                    list_.append('bold')
                elif c == 'i':
                    list_.append('italic')
                elif c == 'u':
                    list_.append('underline')
                elif c == 's':
                    list_.append('overstrike')

            return (font, 10, ' '.join(list_))

        try:
            alttag = getattr(__import__('languages.'+theme), theme)
            if hasattr(alttag, 'append_tags'):
                for key, value in alttag.append_tags.items():
                    if 'font' in value:
                        if isinstance(value['font'], str):
                            value['font'] = _style(value['font'])
                    else:
                        value['font'] = (font, 10, '')

                    self.tagdefs[key] = value

            for xtag, atag in ALTERNATE_TAGS.items():
                if xtag not in self.tagdefs:
                    if atag is None:
                        self.tagdefs[xtag] = {'foreground': None, 'background': None}
                    else:
                        self.tagdefs[xtag] = dict(self.tagdefs[atag])

            if hasattr(alttag, 'read_twice'):
                self.read_twice = alttag.read_twice
        except (ImportError, AttributeError) as e:
            pass

    def insert(self, index, chars, tags=None):
        index = self.index(index)
        self.delegate.insert(index, chars, tags)
        self.notify_range(index, index + "+%dc" % len(chars))

    def delete(self, index1, index2=None):
        index1 = self.index(index1)
        self.delegate.delete(index1, index2)
        self.notify_range(index1)

    after_id = None
    allow_colorizing = True
    colorizing = False

    def notify_range(self, index1, index2=None):
        self.tag_add("TODO", index1, index2)
        if self.after_id:
            if DEBUG: print "colorizing already scheduled"
            return
        if self.colorizing:
            self.stop_colorizing = True
            if DEBUG: print "stop colorizing"
        if self.allow_colorizing:
            if DEBUG: print "schedule colorizing"
            self.after_id = self.after(1, self.recolorize)

    close_when_done = None # Window to be closed when done colorizing

    def close(self, close_when_done=None):
        if self.after_id:
            after_id = self.after_id
            self.after_id = None
            if DEBUG: print "cancel scheduled recolorizer"
            self.after_cancel(after_id)
        self.allow_colorizing = False
        self.stop_colorizing = True
        if close_when_done:
            if not self.colorizing:
                close_when_done.destroy()
            else:
                self.close_when_done = close_when_done

    def toggle_colorize_event(self, event):
        if self.after_id:
            after_id = self.after_id
            self.after_id = None
            if DEBUG: print "cancel scheduled recolorizer"
            self.after_cancel(after_id)
        if self.allow_colorizing and self.colorizing:
            if DEBUG: print "stop colorizing"
            self.stop_colorizing = True
        self.allow_colorizing = not self.allow_colorizing
        if self.allow_colorizing and not self.colorizing:
            self.after_id = self.after(1, self.recolorize)
        if DEBUG:
            print "auto colorizing turned",\
                  self.allow_colorizing and "on" or "off"
        return "break"

    def recolorize(self):
        self.after_id = None
        if not self.delegate:
            if DEBUG: print "no delegate"
            return
        if not self.allow_colorizing:
            if DEBUG: print "auto colorizing is off"
            return
        if self.colorizing:
            if DEBUG: print "already colorizing"
            return
        try:
            self.stop_colorizing = False
            self.colorizing = True
            if DEBUG: print "colorizing..."
            t0 = time.clock()
            self.recolorize_main()
            t1 = time.clock()
            if DEBUG: print "%.3f seconds" % (t1-t0)
        finally:
            self.colorizing = False
        if self.allow_colorizing and self.tag_nextrange("TODO", "1.0"):
            if DEBUG: print "reschedule colorizing"
            self.after_id = self.after(1, self.recolorize)
        if self.close_when_done:
            top = self.close_when_done
            self.close_when_done = None
            top.destroy()

    def recolorize_main(self):
        next = "1.0"
        while True:
            item = self.tag_nextrange("TODO", next)
            if not item:
                break
            head, tail = item
            self.tag_remove("SYNC", head, tail)
            item = self.tag_prevrange("SYNC", head)
            if item:
                head = item[1]
            else:
                head = "1.0"

            chars = ""
            next = head
            lines_to_get = 1
            ok = False
            while not ok:
                mark = next
                next = self.index(mark + "+%d lines linestart" %
                                         lines_to_get)
                lines_to_get = min(lines_to_get * 2, 100)
                ok = "SYNC" in self.tag_names(next + "-1c")
                line = self.get(mark, next)
                ##print head, "get", mark, next, "->", repr(line)
                if not line:
                    return
                for tag in self.tagdefs.keys():
                    self.tag_remove(tag, mark, next)
                chars = chars + line
                m = self.prog.search(chars)
                p = 0
                while m:
                    for key, value in m.groupdict().items():
                        if value:
                            a, b = m.span(key)
                            self.tag_add(key,
                                         head + "+%dc" % a,
                                         head + "+%dc" % b)
                            if self.read_twice:
                                self.read_twice(
                                    self, head, key, value, chars, m
                                )

                    if m.start() == m.end():
                        p = m.start()+1
                        m = self.prog.search(chars, p)
                        if p == m.start():
                            m = None
                    else:
                        m = self.prog.search(chars, m.end())
                if "SYNC" in self.tag_names(next + "-1c"):
                    head = next
                    chars = ""
                else:
                    ok = False
                if not ok:
                    # We're in an inconsistent state, and the call to
                    # update may tell us to stop.  It may also change
                    # the correct value for "next" (since this is a
                    # line.col string, not a true mark).  So leave a
                    # crumb telling the next invocation to resume here
                    # in case update tells us to leave.
                    self.tag_add("TODO", next)
                self.update()
                if self.stop_colorizing:
                    if DEBUG: print "colorizing stopped"
                    return

    def removecolors(self):
        for tag in self.tagdefs.keys():
            self.tag_remove(tag, "1.0", "end")

def _color_delegator(parent):  # htest #
    from Tkinter import Toplevel, Text
    from idlelib.Percolator import Percolator

    top = Toplevel(parent)
    top.title("Test ColorDelegator")
    top.geometry("200x100+%d+%d" % (parent.winfo_rootx() + 200,
                  parent.winfo_rooty() + 150))
    source = "if somename: x = 'abc' # comment\nprint\n"
    text = Text(top, background="white")
    text.pack(expand=1, fill="both")
    text.insert("insert", source)
    text.focus_set()

    p = Percolator(text)
    d = ColorDelegator()
    p.insertfilter(d)

if __name__ == "__main__":
    from idlelib.idle_test.htest import run
    run(_color_delegator)
