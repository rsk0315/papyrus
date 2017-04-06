import re

class CppParser(object):
    def __init__(self, editwin):
        self.editwin = editwin
        if editwin is None:
            return

        self.text = self.editwin.text

    @classmethod
    def parenclose_index(cls, line, pos, pair):
        i = pos
        opened = 0
        while i < len(line):
            if line[i] == pair[0]:
                opened += 1
            elif line[i] == pair[1]:
                opened -= 1

            i += 1
            if not opened:
                break

        return i

    @classmethod
    def eat_modifier(cls, line):
        modifiers = [
            'static', r'const(?:expr)?', 'volatile',
        ]
        return re.sub(r'\b'+r'|'.join(modifiers)+r'\b', ' ', line)

    def get_type(self, index, what):
        # todo find variables in function parameters
        if what is None: return None
        if '.' in what: return None  # todo

        line = self.text.get(index+' linestart', index+' lineend')

        leading_ws = re.compile(r'[ \t]*')
        indent_length = lambda s: len(leading_ws.match(s).group())

        ilen = indent_length(line)

        id_re = re.compile(r'[ \t]*([_A-Za-z]\w*)[ \t]*')
        ns_re = re.compile(r'[ \t]*::[ \t]*([_A-Za-z]\w*)[ \t]*')
        paren_re = re.compile(r'[ \t]*(\()')

        ln = int(self.text.index(index).split('.')[0])
        typename = None
        while ln >= 1:
            line = self.text.get('%d.0 linestart'%ln, '%d.0 lineend'%ln)

            ln -= 1
            is_template = False

            tn = ''

            if indent_length(line) > ilen: continue
            if line.lstrip().startswith('//'): continue
            if not line.strip(): continue
            if indent_length(line) < ilen:
                ilen = indent_length(line)

            line = self.eat_modifier(line)
            m = re.match(r'[ \t]*([_A-Za-z]\w*)', line)
            if m is None:
                continue

            tn = m.group(1)
            pos = m.end()

            # find typename
            while m is not None and m.end() < len(line):
                if line[m.end()] == '<':
                    endpos = self.parenclose_index(line, m.end(), '<>')

                    if (
                            tn.endswith('vector') and
                            re.sub(r'\s+', '', line[pos:endpos]) == '<bool>'
                    ):
                        tn += '_bool'
                    else:
                        tn += '<>'

                    pos = endpos

                m = ns_re.match(line, pos=pos)
                if m is not None:
                    tn += '::'+m.group(1)
                    pos = m.end()

            following = line[pos:].lstrip()
            if not following: continue
            if following[0] in ('(',):
                if tn not in ('for', 'if', 'case', 'while'):
                    continue
            elif not (following[0].isalpha() or following[0] in '_*&'):
                continue

            if self.search_var(line, pos, what):
                typename = tn
                break

            if tn in ('for', 'if', 'case', 'while'):
                endpos = pos
            else:
                # function declaration; function name
                m2 = id_re.match(line, pos=pos)
                if m2 is None: continue

                endpos = m2.end()
                if line[endpos:].startswith('<'):
                    # eat function template specialization
                    endpos = self.parenclose_index(line, endpos, '<>')
                elif line[endpos:].startswith('='):
                    lambda_re = re.compile(r'=[ \t]*(?=\[)')
                    m3 = lambda_re.match(line, pos=endpos)
                    if m3 is not None:
                        endpos = self.parenclose_index(line, m3.end(), '[]')

            m2 = paren_re.match(line, pos=endpos)
            if m2 is None: continue
            if m2.group(1):
                tn = self.get_funcparams(line, m2.end(), what)
                if tn:
                    typename = tn
                    break

        return typename

##    @classmethod
##    def get_funcparams(cls, line, pos, what):
##        id_re = re.compile(r'[ \t]*([_A-Za-z]\w*)[ \t]*')
##        ns_re = re.compile(r'[ \t]*::[ \t]*([_A-Za-z]\w*)[ \t]*')
##        param_re = re.compile(r'([*&]*)([_A-Za-z]\w*)')
##
##        m = id_re.match(line, pos=pos)
##        while m is not None:
##            # todo default arguments
##            pos = m.end()
##            tn = m.group(1)
##            if pos < len(line) and line[pos] == '<':
##                pos = cls.parenclose_index(line, pos, '<>')
##                if pos >= len(line): return None
##
##            m2 = param_re.match(line, pos=pos)
##            if m2 is None: return None
##
##            if m2.group(2) == what:
##                return None if m2.group(1) else m.group(1)
##
##            m = id_re.match(line, pos=pos)
##
##        return None

    @classmethod
    def remove_cv(cls, line):
        return re.sub(
            r'(?:const(?:expr)|volatile|static)',
            lambda m: ' '*len(m.group()),
            line
        )

    @classmethod
    def get_funcparams(cls, line, pos, what):
        id_re = re.compile(r'[ \t]*(?P<PTR_REF>[*&]*)[ \t]*(?P<NAME>[_A-Za-z]\w*)[ \t]*')

        line = cls.remove_cv(line)

        endpos, entity = cls.get_fulltypename(line, pos)
        while entity:
            param = id_re.match(line, pos=endpos)
            if param is None:
                return None

            if param.group('NAME') == what:
                return None if '*' in param.group('PTR_REF') else entity

            endpos = param.end()
            if endpos < len(line):
                punct = line[endpos]
                if punct == ',':
                    endpos += 1
                elif punct == ')':
                    break

            endpos, entity = cls.get_fulltypename(line, endpos)

        return None

    @classmethod
    def get_fulltypename(cls, line, pos):
        id_re = re.compile(r'[ \t]*([_A-Za-z]\w*)[ \t]*')
        ns_re = re.compile(r'[ \t]*::[ \t]*([_A-Za-z]\w*)[ \t]*')

        m = id_re.match(line, pos=pos)
        if m is None: return -1, ''

        entity = m.group(1)
        endpos = m.end()

        if endpos < len(line) and line[endpos] == '<':
            endpos = cls.parenclose_index(line, endpos, '<>')
            entity += '<>'

        if endpos >= len(line): return endpos, entity

        m = ns_re.match(line, pos=endpos)
        while m is not None:
            endpos = m.end()
            entity += '::' + m.group(1)

            if endpos < len(line) and line[endpos] == '<':
                endpos = cls.parenclose_index(line, endpos, '<>')
                entity += '<>'

            if endpos >= len(line): break

            m = ns_re.match(line, pos=endpos)

        return endpos, entity

    @classmethod
    def eat_item(cls, line, pos):
        # (...()? ... : ...) + ()[]
        # identifiers
        # function calls
        # operators
        # parentheses
        pass

    def search_var(self, line, pos, target):
        id_re = re.compile(r'[ \t]*([*&]*)[ \t]*([_A-Za-z]\w*)[ \t]*')
        eq_re = re.compile(r'[ \t]*=[ \t]*')
        eat_re = re.compile(r'[ \t]*\w+[ \t]*')

        m = id_re.match(line, pos=pos)
        while m is not None:
            if m.group(2) == target: return not m.group(1).startswith('*')

            pos = m.end()

            if pos >= len(line): return False
            if line[pos] == '[':
                pos = self.parenclose_index(line, pos, '[]')
                if pos >= len(line): return False
            if line[pos] == '(':
                pos = self.parenclose_index(line, pos, '()')
                if pos >= len(line): return False

            m_eq = eq_re.match(line, pos=pos)
            if m_eq:
                if m.end() >= len(line): return False

                if line[m.end()] == '{':
                    pos = self.parenclose_index(line, pos, '{}')
                elif line[m.end()] == '(':
                    pos = self.parenclose_index(line, pos, '()')

                m_eat = eat_re.match(line, pos=pos)
                if m_eat: pos = m_eat.end()
                if pos >= len(line): return False

            if line[pos] == ',': pos += 1
            m = id_re.match(line, pos=pos)

        return False

    @classmethod
    def remove_templateargs(cls, typename):
        id_re = re.compile(r'[ \t]*([_A-Za-z]\w*)[ \t]*')
        ns_re = re.compile(r'[ \t]*::[ \t]*([_A-Za-z]\w*)[ \t]*')
        s = ''
        m = id_re.match(typename)
        while m is not None:
            s += m.group(1)
            pos = m.end()
            if pos < len(typename) and typename[pos] == '<':
                endpos = cls.parenclose_index(typename, pos, '<>')

##                print `s`, `typename[pos:endpos]`, (pos, endpos)

                if (
                        s.endswith('vector') and
                        re.sub(r'\s+', '', typename[pos:endpos]) == '<bool>'
                ):
                    s += '_bool'
                else:
                    s += '<>'

                pos = endpos

            m = ns_re.match(typename, pos)
            if m is not None:
                s += '::'

        return s

'''
foo<>::bar<baz::hoge>::piyo d;
a::b<>::c<> d;
'''
