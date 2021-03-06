#!/usr/bin/env python

import regex
#from idlelib.languages.configures import *

def any(name, alternates):
    "Return a named group pattern matching list of alternates."
    return "(?P<{name}>{pattern})".format(
        name=name,
        pattern=r'|'.join(alternates),
    )

keywords = r'|'.join([
    r'(?<=(?:^|\n)[ \t]*#(?:\\\n|[^\n])*)defined',
    'auto',     'break',    'case',     'char',     'const',    'continue',
    'default',  'do',       'double',   r'(?<!#)else',
    'enum',     'extern',
    'float',    'for',      'goto',     r'(?<!#)if',
    'int',      'long',
    'register', 'return',   'short',    'signed',   'sizeof',   'static',
    'struct',   'switch',   'typedef',  'union',    'unsigned', 'void',
    'volatile', 'while',
    'nullptr',  'class',    'mutable',  'thread_local',         'friend',
    'constexpr',            'explicit', 'inline',   'virtual',  'public',
    'protected',            'private',  'operator', 'template', 'bad_cast',
    'bad_typeid',           'catch',    'const_cast',
    'dynamic_cast',         'except',   'finally',  'namespace',
    'reinterpret_cast',     'static_cast',          'throw',
    'type_info',            'typeid',   'using',
    'xalloc',   'asm',      'typename',
    r'(?<!\boperator\b\s*)(?:new|delete)',
])
types = r'|'.join([
    'char',     'const',    'double',   'enum',     'float',    'int',
    'long',     'register', 'short',    'signed',   'static',   'struct',
    'typedef',  'union',    'unsigned', 'void',     'volatile', 'bool',
])
keyword = [
    r'\b(?:{0})(?:\s+(?:{0}))*\b'.format(keywords+r'|'+types),
    r'[Rr](?=")',
]

preprocessor = [
    r'(?<=#[ \t]*){0}\b'.format(i) for i in [
        'include',  'define',   r'ifn?def', 'endif',    'if',       'elif',
        'else',     'error',    'warning',  'pragma',   'pragma once',
        'pragma comment',
    ]
]

stl_class_list = [
    'vector', 'array', 'deque',
    r'(?:forward_)?list', r'(?:unordered_)?(?:multi)?(?:set|map)',
    'stack', r'(?:priority_)?queue', 'deque',
    r'(?:Input|Output|Forward|Bidirectional|RandomAccess)Iterator',
    r'(?:BD|RA)?Iter',
    'pair', 'complex', 'bitset', 'iterator', 'string', 'tuple',

    r'[iu](?:8|16|32|64)', r'f(?:32|64)', r'[_A-Za-z]\w*_t',
]

stl_classes = [r'\b(?:' + r'|'.join(stl_class_list) + r')\b']

string = [
    r'\'(?:[^\\\n]|\\[abfnrtv\'"?\\]|\\[0-7]{1,3}|\\[Xx][0-9A-Fa-f]{1,2})\'?',
    r'(?<!\boperator\s*)[Rr]?"[^"\\\n]*(?:(?:\\.)+[^"\\\n]*)*"?',
    r'@"[^"]*(?:(?:"")+[^"]*)*"?',

    r'(?m)(?<=^[ \t]*#[ \t]*include)\s*<[^>\n]*>?',
]

number = [
    r'(?<!\w){0}'.format(i) for i in [
        r'(?:\.\d+|\d+\.\d*)(?:[Ee][+-]?\d+)?[FILQfilq]?',
        r'\d+(?:[Ee][+-]?\d+)',  # todo
        r'(?:0[Qq][0-3]+|0[Bb][01]+)',  # todo
        r'(?:0[Xx][\dA-Fa-f]+|0[0-7]+|[1-9]\d*|0)[UILuli]*',
    ]
]

operator = [
    r'(?<!\boperator\b)[-!%&+*|<^>?:=~/,.]',
    r';',
    r'##',
    r'(?<!^\s*)#',
]

definition = []

identifier = (
    r'\b[_A-Za-z]\w*',
)

comment = [
    r'(?P<COMMENT>//(?P<LINE_COMMENT>[^\n]*))',
    r'(?P<BLOCK_COMMENT>/\*[^*]*(?:\*(?:[^/*]|\*(?!/))|[^*])*(?:\*\*?/)?)',
]

freq_used_val = [
    r'\b(?:true|false)\b'
]

KEYWORD = (
    any('KEYWORD', keyword) + r'|' +
    any('STL_CLASSES', stl_classes)
)
BUILTIN = (
    any('PREPROCESSOR', preprocessor) + r'|' +
    any('BUILTIN', number+freq_used_val) + r'|' +
    any('OPERATOR', operator)
)
COMMENT = r'|'.join(comment)
STRING = any('STRING', string)
DEFINITION = (
    any('DEFINITION', definition)
)
SP_VARIABLE = r'(?P<SP_VARIABLE>\bthis\b)'

IDENTIFIER = any('IDENTIFIER', identifier)
MISC = r'|'.join(
    [
        SP_VARIABLE,
        IDENTIFIER,
        r'(?P<SHARP>#)',
        r'(?P<PUNC>[(){}[\]])',
        ur'(?P<ERROR>\u3000)',
    ]
)


DEF_POINTER_COMMA = r'(?P<SYMBOL>[*,]+)'
SPECIAL_CHAR = (
    r'(?P<SPECIAL>\\'
        r'(?:'
            r'[abtnvfr\\]|[Xx][0-9A-Fa-f]{1,2}|[0-7]{1,3}'
        r')'
    r')'
r'|'r'(?P<FORMAT>%'
        r'\*?'
        r'(?:[-+ 0#])?'
        r'(?:\d+)?'
        r'(?:\.\d+)?'
        r'(?:[LQhltz]+|I\d+)?'
        r'(?:[diuoxXcsfeEgGp%]|\[\^?[^]\\]*(?:\\.[^]\\]*)*\])'
    r')'
)

def get_parenclose_index(line, parenopen, paren):
    assert len(paren) == 2

    i = parenopen
    opened = 0
    quoted = False
    while i < len(line):
        if quoted:
            if line[i] in ('"', "'"):
                quoted = False
        elif line[i] == paren[0]:
            opened += 1
        elif line[i] == paren[1]:
            opened -= 1
        elif line[i] in ('"', "'"):
            quoted = True

        i += 1
        if not opened and i < len(line):
            return i

    return None

def get_quoteclose_index(line, quoteopen, quote):
    assert len(quote) == 1

    i = quoteopen
    opened = False
    escape = False
    while i < len(line):
        if opened:
            if escaped:
                escaped = False
            else:
                if line[i] == '\\':
                    escaped = True
                elif line[i] == quote:
                    opened = False
        else:
            if line[i] == quote:
                opened = True

        i += 1
        if not opened and i < len(line):
            return i

    return None

def eat_quote(line):
    line = list(line)
    i = 0
    quot = None
    escaped = False
    while i < len(line):
        if quot is not None:
            if escaped:
                escaped = False
            else:
                if line[i] == '\\':
                    escaped = True
                elif line[i] == quot:
                    quot = None
                else:
                    line[i] = ' '
        else:
            if line[i] in ('"', "'"):
                quot = line[i]

        i += 1

    return ''.join(line)

def get_stmt_index(line, begin, end):
    while begin > 0:
        if line[begin-1] in ";\n":
            break

        begin -= 1

    while end < len(line):
        if line[end] in ";\n":
            break

        end += 1

    return (begin, end)

QUALIFIERS = [
    # not treat as type names
    "const", "constexpr", "public", "private", "static", "typename", "virtual",
    "inline", "new", "delete", "return", "typedef", "goto", "using",
    r"(?:for|while|if)[ \t]*\(",
]

QUALS = r'(?:\b(?:' + r'|'.join(QUALIFIERS) + r')\b)'

QUA_RE = regex.compile(
    r'{0}(?:[ \t]*{0})*'.format(QUALS)
)

WS = r'(?:[ \t]+)'

ID_NS = r'(?:{0}{1}?::{1}?)*{0}'.format(
    r'(?:\b[_A-Za-z]\w*)',
    WS
)

ID_TP = r'(?:{0}(?:<(?:{0}(?:{1}?,{1}?{0})*)?{1}?>)?)'.format(ID_NS, WS)

IDENTIFIER_RE = regex.compile(
    r'(?:{0}(?:<(?:{1}(?:{2}?,{2}?{1})*)?{2}?>)?)'.format(
        ID_NS, r'(?:'+ID_TP+r'[ \t*&]*)', WS,
    )
)

PAREN_PAIRS = {
    '(': "()",
    '[': '[]',
    '<': '<>',
    '{': '{}',
}

def get_nextpos(stmt, pos):
    # get index of next initializing variable
    while pos < len(stmt) and stmt[pos] in " \t":
        # eat spaces
        pos += 1

    if len(stmt) <= pos:
        # no strings to eat
        return pos

    if stmt[pos] == '(':
        return get_parenclose_index(stmt, pos, "()")
    if stmt[pos] == '{':
        return get_parenclose_index(stmt, pos, "{}")
    if stmt[pos] == ',':
        return pos

    while pos is not None and pos < len(stmt) and stmt[pos] == '[':
        pos = get_parenclose_index(stmt, pos, "[]")

    if pos is None:
        return len(stmt)

    if stmt[pos] == '=':
        while pos < len(stmt) and stmt[pos] not in ",;\n":
            if stmt[pos] in "([{<":
                pos = get_parenclose_index(stmt, pos, PAREN_PAIRS[stmt[pos]])
            elif stmt[pos] in ("'", '"'):
                pos = get_quoteclose_index(stmt, pos, stmt[pos])
            else:
                pos += 1

            if pos is None:
                return len(stmt)
        else:
            return pos

    else:
        return len(stmt)

def is_decl(stmt, begin):
    qualifiers = QUA_RE.match(stmt)
    if qualifiers is not None:
        qlen = qualifiers.end() - qualifiers.start()

        slen = len(stmt)
        stmt = stmt[qlen:].lstrip()
        begin -= slen - len(stmt)

    if begin == 0:
        return False

    typename = IDENTIFIER_RE.match(stmt)
    if typename is None:
        # not declaration statement
        return False

    if typename.start() == begin:
        return False

    e = typename.end()
    if e >= len(stmt):
        return False

    following = stmt[e:].lstrip()
    if not following:
        return False

    if following[0] in "+-/=%([<.>|^~!":
        return False
    if following.startswith("* "):
        return False  # xxx int* a
    if following.startswith("& "):
        return False  # xxx int& a

    next_id = IDENTIFIER_RE.search(stmt, pos=typename.end())
    while next_id is not None:
        if next_id.start() == begin:
            return True
        if next_id.start() > begin:
            return False

        pos = get_nextpos(stmt, next_id.end())
        next_id = IDENTIFIER_RE.search(stmt, pos)

    return False

def specify_tag(line, begin, end):
    line = eat_quote(line)
    name = line[begin:end]
    if name.endswith("_t"):
        # type aliases, e.g. size_t
        return "BUILTIN"

    if line[:begin].rstrip().endswith('}'):
        # struct declaretions (maybe there are no conflictions)
        return "DEFINITION"

    if end < len(line) and line[end] == '(':
        i = get_parenclose_index(line, end, "()")
        if i is not None:
            nextchar = line[i:].lstrip()
            nextchar = nextchar[0] if nextchar else None

            if nextchar is not None:
                if nextchar[0] == '{':
                    # function definitions
                    si = get_stmt_index(line, begin, end)
                    if regex.search(
                            r'\)[ \t]*:', line, pos=si[0], endpos=begin
                    ) is None:
                        return "DEFINITION"
                elif nextchar[0] == ':':
                    # constructor (with initialization) definitions
                    return "DEFINITION"

    cstmt = get_stmt_index(line, begin, end)
    stmt = line.__getslice__(*cstmt)
    len_ws = len(stmt) - len(stmt.lstrip())

    if stmt.startswith("using"):
        if '=' in stmt[:begin]:
            return None
        if '=' in stmt[begin:]:
            return "DEFINITION"

        if ':' not in stmt[begin:]:
            return "DEFINITION"
        else:
            return None

    # hack
    if is_decl(stmt.lstrip(), begin-cstmt[0]-len_ws):
        # declarations
        return "DEFINITION"

    if end < len(line):
        if line[end] == '(':
            # functions declarations
            return "BUILTIN"

        if line[end] == '<':
            i = get_parenclose_index(line, end, "<>")
            if i is not None and line[i]=='(':
                # template functions declarations
                return  "BUILTIN"

    if len(name) >= 2 and name.isupper():
        return "CONSTANT"

def deco_identifier(cdelegator, head, key, lchars, m):
    # cdelegator.tag_add(tagname, head+X.Xc, head+X.Xc)
    a, b = m.span(key)
    cdelegator.tag_remove(
        'IDENTIFIER', head+"{:+}c".format(a), head+"{:+}c".format(b)
    )

    new_tag = specify_tag(lchars, a, b)
    if new_tag is None:
        return

    cdelegator.tag_add(
        new_tag, head+"{:+}c".format(a), head+"{:+}c".format(b)
    )

def deco_string(cdelegator, head, key, lchars, m):
    a, b = m.span(key)
    prog = regex.compile(SPECIAL_CHAR)
    m_ = prog.search(lchars, a)
    while m_ is not None and m_.end() <= b:
        for k, v in m_.groupdict().items():
            if v:
                a_, b_ = m_.span(k)
                cdelegator.tag_remove(
                    "STRING", head+"{:+}c".format(a_), head+"{:+}c".format(b_)
                )
                cdelegator.tag_add(
                    k, head+"{:+}c".format(a_), head+"{:+}c".format(b_)
                )

        m_ = prog.search(lchars, m_.end())

more_decorate = {
    "IDENTIFIER": deco_identifier,
    "STRING": deco_string,
}
