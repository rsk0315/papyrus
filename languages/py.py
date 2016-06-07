#!/usr/bin/env python

import keyword
import __builtin__
from idlelib.configHandler import idleConf

try:
    import regex
except ImportError:
    import re as regex


def any(name, alternates):
    "Return a named group pattern matching list of alternates."
    return "(?P<{name}>{pattern})".format(
        name=name,
        pattern=r'|'.join(alternates),
    )

keyword_list = [
    r'(?<!\w)' + w + r'(?!\w)' for w in keyword.kwlist if (
        not str(w) == 'print'
    )
] + [r'(?<!\w)print(?![\w(])']
operator_list = [
    r'!=',
    r'[-+*/%<>&|^~=`]',
    r'[;:@]',
    r'\.\.\.',
]
builtin_list = [
    name for name in dir(__builtin__) if (
        not str(name) == 'print' and
        True  # not regex.search(r'__\w+__', name)
    )
] + [
    '__name__',     '__file__',     '__loader__',   '__package',
    r'__builtins?__',               r'print(?=\()',
]

builtins = (
    r'(?:'
        r'(?<![.\w])'
        r'(?:' +
            r'|'.join(builtin_list) +
        r')'
        r'(?!\w)'
    r')'
)

number_list = [
    r'(?:{pointfloat})(?:{exponent})?[Jj]?'.format(
        pointfloat=r'[0-9]*\.[0-9]+|[0-9]+\.',
        exponent=r'[Ee][+-]?[0-9]+',
    ), # imagnumber
    r'(?:[0-9]+)(?:{exponent})?[Jj]'.format(
        pointfloat=r'[0-9]*\.[0-9]+|[0-9]+\.',
        exponent=r'[Ee][+-]?[0-9]+',
    ), # imagnumber
    r'(?:[0-9]+)(?:[Ee][+-]?[0-9]+)', # todo exponent
    r'(?:{decint}|{octint}|{hexint}|{binint})[Ll]?'.format(
        decint=r'[1-9][0-9]*',
        octint=r'0[Oo]?[0-7]+',
        hexint=r'0[Xx][0-9A-Fa-f]+',
        binint=r'0[Bb][01]+',
    ), # longinteger
    r'0[Ll]?', # zero
]

numbers = r'(?<!\w)(?:' + r'|'.join(number_list) + r')'

special_method_list = [
    name for name in (
        'new',      'init',     'del',      'repr',     'str',      'lt',
        'le',       'eq',       'ne',       'gt',       'ge',       'cmp',
        'rcmp',     'hash',     'nonzero',  'unicode',  'getattr',  'setattr',
        'delattr',  'getattribute',         'get',      'set',      'delete',
        'call',     'len',      'getitem',  'setitem',  'delitem',  'iter',
        'reversed', 'contains', 'getslice', 'setslice', 'delslice', 'add',
        'sub',      'mul',      'floordiv', 'mod',      'divmod',   'pow',
        'lshift',   'rshift',   'and',      'xor',      'or',       'div',
        'truediv',  'radd',     'rsub',     'rmul',     'rdiv',     'rtruediv',
        'rfloordiv','rmod',     'rdivmod',  'rpow',     'rlshift',  'rrshift',
        'rand',     'rxor',     'ror',      'iadd',     'isub',     'imul',
        'idiv',     'itruediv', 'ifloordiv','imod',     'ipow',     'ilshift',
        'irshift',  'iand',     'ixor',     'ior',      'neg',      'pos',
        'abs',      'invert',   'complex',  'int',      'long',     'float',
        'oct',      'hex',      'index',    'coerce',   'enter',    'exit',

        'class',    'doc',      'format',   'reduce',   'reduce_ex',
        'sizeof',   'subclasshook',
    )
]

special_methods = r'(?<!\w)__(?:' + r'|'.join(special_method_list) + r')__(?!\w)'

string_prefix = r'(?:\b[BURbur]|\b[BUbu][Rr])?'

sqstring = string_prefix + r"'[^'\\\n]*(?:\\.[^'\\\n]*)*'?"
dqstring = string_prefix + r'"[^"\\\n]*(?:\\.[^"\\\n]*)*"?'
sq3string = string_prefix + r"'''[^'\\]*(?:(?:\\.|'(?!''))[^'\\]*)*(?:''')?"
dq3string = string_prefix + r'"""[^"\\]*(?:(?:\\.|"(?!""))[^"\\]*)*(?:""")?'

escape = [
    r'\\[abtnvfr]',
    r'\\[0-7]{1,3}',
    r'\\[Xx][0-9A-Fa-f]{2}',
]

escape_u = escape + [
    r'\\u[0-9A-Fa-f]{4}',
    r'\\U[0-9A-Fa-f]{8}',
    r'\\N\{[^}]*\}',
]

field_name = r'\w*(?:\.[_A-Za-z]\w*|\[\w+\])*'
conversion = r'[rsa]'

nested = '|{' + field_name + '}'

format_spec = {
    'fill': r'[^}}{{\\]|{esc}'.format(
        esc=escape,
    ) + nested,
    'fill_u': r'[^}}{{\\]{esc}|{{field_name}}'.format(
        esc=escape_u,
    ) + nested,
    'align': r'[<=>^]' + nested,
    'sign': r'[ +-]' + nested,
    'sharp': r'#' + nested,
    'zero': r'0' + nested,
    'width': r'\d+' + nested,
    'comma': r',' + nested,
    'precision': r'\d+' + nested,
    'type_': r'[bcdeEfFgGnosxX%]' + nested,
}

format_brace = (
    r'\{' +
        r'(?:{field_name})?(?:!{conversion})?(?::{format_spec})?'.format(
            field_name=field_name,
            conversion=conversion,
            format_spec=(
                r'(?:(?:{fill})?{align})?(?:{sign})?(?:{sharp})?(?:{zero})?'
                r'(?:{width})?(?:{comma})?(?:\.{precision})?(?:{type_})?'
            ).format(**format_spec),
        ) +
    r'\}'
)

format_brace_u = (
    r'\{' +
        r'(?:{field_name})?(?:!{conversion})?(?::{format_spec})?'.format(
            field_name=field_name,
            conversion=conversion,
            format_spec=(
                r'(?:(?:{fill_u})?{align})?(?:{sign})?(?:{sharp})?(?:{zero})?'
                r'(?:{width})?(?:{comma})?(?:\.{precision})?(?:{type_})?'
            ).format(**format_spec),
        ) +
    r'\}'
)

format_percent = (
    r'%(?:{mapkey})?(?:{flag})?(?:{width})?(?:{precise})?[Lhl]?'
    r'(?:{type_})'.format(
        mapkey=r'\(\w+\)',
        flag=r'[#0 +-]',
        width=r'\d+|\*',
        precise=r'\.\d+|\.\*',
        type_=r'[diouxXeEfFgGcrs%]',
    )
)

regex_ = r'|'.join([
    r'(?P<RE_REPEAT>\{(?:\d+,\d*|,\d+)\}|[+*?])',
    r'(?P<COMMENT>\(\?#(?:[^\\)]|\\(?:.|\n))*\)?)',

    r'(?P<RE_PAR>\)|\()'                # )
    r'(?P<RE_PARENTHESIS>'
        r'(?P<RE_NAME>'
            r'(?:'
                r'\?P<[_A-Za-z]\w*>'    # (?P<NAME>
            r'|'r'\?P=[_A-Za-z]\w*'     # (?=NAME
            r')'
        r'|'
            r'(?:'
                r'\*'
                r'(?:FAIL|F|PRUNE|SKIP)\b'
            r')'
        r')'
    r'|'r'\?(?::|>|[aiLmsux]+)'         # (?: | (?>: | (?aiLmsux
    r'|'r'\?<?[!=]'                     # assertion
    r'|'r'\?\((?:\d+|[_A-Za-z]\w*)\)'   # (?(name/id)
    r'|'                                # (
    r')',

    r'(?P<RE_BRACKET>\[)'
    r'(?P<RE_CARET>\^)?'
    r'(?P<RE_CHARS>'
        r'(?:'
            r'\]'
            r'(?:\\.|[^\]\\])*'
            r'\]?'
        r'|'
            r'(?:\\.|[^\]\\])+'
            r'\]?'
        r'|)'
    r')',
    r'(?P<SPECIAL>\\(?:[AZbBdDsSwW]|\d+|g<(?:\d+|[_A-Za-z]\w*)>))',

    r'(?P<RE_SGL>[.^$|]|&&|~~|--)',
    r'(?P<RE_SPECIAL>\\.)',
])

#
set_of_characters = set_of_characters_u = (
    r'\[\^?'
    r'(?:'
        r'\]'
        r'(?:\\.|[^\]\\])*'
        r'\]?'
    r'|'
        r'(?:\\.|[^\]\\])+'
        r'\]?'
    r'|)'
)
#

invalid = (
    r'\\[0-7abtnvfr\n\\\'"]'
r'|'r'\\[Xx][0-9A-Fa-f]{2}'
r'|' + any(
        'ERROR', [
            r'\\[Xx][0-9A-Fa-f]?(?![0-9A-Fa-f])',
            r'\\[^Xx0-7abtnvfr\n\\\'"]',
        ]
    )
)

invalid_u = (
    r'\\[0-7a-btnvfr\n\\\'"]'
r'|'r'\\[Xx][0-9A-Fa-f]{2}'
r'|'r'\\u[0-9A-Fa-f]{4}'
r'|'r'\\U[0-9A-Fa-f]{8}'
r'|' + any(
        'ERROR', [
            r'\\[Xx][0-9A-Fa-f]?(?![0-9A-Fa-f])',
            r'\\u[0-9A-Fa-f]{,3}(?![0-9A-Fa-f])',
            r'\\U[0-9A-Fa-f]{,7}(?![0-9A-Fa-f])',
            r'\\N(?:(?!\{)|\{[ A-Za-z]*[^ A-Za-z}]+\}?)',
            r'\\[^Xx0-7abtnvfrUuN\n\\\'"]',
        ]
    )
)

invalid_r = (
    r'\\[Xx][0-9A-Fa-f]{2}'
r'|' + any(
        'ERROR', [
            r'\[\^?(?:\](?:\\.|[^\]\\])*|(?:\\.|[^\]\\])+)(?=\'(?:\'\')?$|"(?:"")?$)',
            r'\\[Xx][0-9A-Fa-f]?(?![0-9A-Fa-f])',
        ]
    ) + r'|' + any('RE_SPECIAL', [r'\\.'])
)

invalid_ur = (
    r'\\[Xx][0-9A-Fa-f]{2}'
r'|'r'\\u[0-9A-Fa-f]{4}'
r'|'r'\\U[0-9A-Fa-f]{8}'
r'|' + any(
        'ERROR', [
            r'\[\^?(?:\](?:\\.|[^\]\\])*|(?:\\.|[^\]\\])+)(?=\'(?:\'\')?$|"(?:"")?$)',
            r'\\[Xx][0-9A-Fa-f]?(?![0-9A-Fa-f])',
            r'\\u[0-9A-Fa-f]{,3}(?![0-9A-Fa-f])',
            r'\\U[0-9A-Fa-f]{,7}(?![0-9A-Fa-f])',
            r'\\N(?:(?!\{)|\{[ A-Za-z]*[^ A-Za-z}]+\}?)',
        ]
    ) + r'|' + any('RE_SPECIAL', [r'\\.'])
)

KEYWORD = any('KEYWORD', keyword_list)
BUILTIN = any('BUILTIN', [builtins, numbers]) + r'|' + any('OPERATOR', operator_list)
COMMENT = any('COMMENT', [r'#[^\n]*'])
STRING = any('STRING', [sq3string, dq3string, sqstring, dqstring])

DEFINITION = (
    r'(?P<CLASSDEF>(?<=\bclass[ \t])[ \t]*[_A-Za-z]\w*)'
r'|'r'(?P<FUNCDEF>(?<=\bdef[ \t])[ \t]*[_A-Za-z]\w*)'
)

FORMAT = r'\{\{|\}\}|' + any('FORMAT', [
    format_brace, format_percent
])

FORMAT_U = r'\{\{|\}\}|' + any('FORMAT', [
    format_brace, format_percent
])

KEY_COMMENT = (
    r'(?P<KEYWORD>'
        r'(?i)(?<=#[ \t]*)\b(?:' + r'|'.join(
            ['TODO', 'XXX', 'FIXME', 'TBD']
        ) + r'\b)'
    r'|'r'(?<=\A#!)[^\n]+'
    r'|'r'(?<=^#(?:[ \t]*-\*-)?)[ \t]*coding[:=][ \t]*[-\w.]*[ \t]*'
    r')'
)


REGEX = REGEX_U = regex_

SPECIAL = r'\\[^abtnvfrxX0-7]|' + any('SPECIAL', escape)
SPECIAL_U = r'\\[^abtnvfrxX0-7uUN]|' + any('SPECIAL', escape_u)

SP_VARIABLE = any('SP_VARIABLE', [r'\bself\b', r'\bcls\b'])
SPECIAL_M = any('SPECIAL_M', [special_methods])
CONSTANT = any('CONSTANT', [r'\b[_A-Z][_0-9A-Z]+\b'])

MISC = r'|'.join([SP_VARIABLE, SPECIAL_M, CONSTANT, ur'(?P<ERROR>\u3000)'])

INVALID = invalid
INVALID_R = invalid_r
INVALID_U = invalid_u
INVALID_UR = invalid_ur



font = idleConf.GetOption('main', 'EditorWindow', 'font')

RED = '#ff0b3a'
SKY = '#0086ba'
GREEN = '#38d878'
GREY = '#969896'
BLACK = '#333333'
WHITE = '#ffffff'
INDIGO = '#183691'
ORANGE = '#ed6a43'
PURPLE = '#795da3'


def read_twice(self, head, key, value, chars, m):
    if key == 'STRING':
        top = value[:5]
        prefix = regex.search(r'^[BURbur]*', top).group().lower()
        quot = regex.search(r'^[BURbur]*(\'\'\'|\'|"""|")', top).group(1)

        has_eos = False
        if quot == "'":
            if value.endswith("'"):
                bs = regex.search(r"(\\*)'$", value).group(1)
                if len(bs) % 2:  # escaped '
                    has_eos = False
                else:
                    has_eos = True

        elif quot == '"':
            if value.endswith('"'):
                bs = regex.search(r'(\\*)"$', value).group(1)
                if len(bs) % 2:  # escaped "
                    has_eos = False
                else:
                    has_eos = True

        if quot == "'''":
            if value.endswith("'''"):
                bs = regex.search(r"(\\*)'''$", value).group(1)
                if len(bs) % 2:  # escaped ' + ''
                    has_eos = False
                else:
                    has_eos = True

        elif quot == '"""':
            if value.endswith('"""'):
                bs = regex.search(r'(\\*)"""$', value).group(1)
                if len(bs) % 2:  # escaped " + ""
                    has_eos = False
                else:
                    has_eos = True

        if prefix:
            self.tag_remove('STRING',
                            head + '+{}c'.format(m.start()),
                            head + '+{}c'.format(m.start()+len(prefix)))
            self.tag_add('STRING_PREFIX',
                            head + '+{}c'.format(m.start()),
                            head + '+{}c'.format(m.start()+len(prefix)))


        if 'ur' in prefix:
            reprog = regex.compile(REGEX_U)
        elif 'r' in prefix:
            reprog = regex.compile(REGEX)
        else:
            reprog = None

        if reprog:
            mr = reprog.search(chars, m.start())
            while mr and mr.end() <= m.end():
                for kr, vr in mr.groupdict().items():
                    if vr:
                        ar, br = mr.span(kr)
##                        print kr, vr, ar, br, '<'
                        self.tag_remove('STRING',
                                        head + '+{}c'.format(ar),
                                        head + '+{}c'.format(br))
                        if kr == 'RE_CHARS':  # XXX
                            self.tag_remove('RE_CARET',
                                            head + '+{}c'.format(ar),
                                            head + '+{}c'.format(br))

                        self.tag_add(kr,
                                     head + '+{}c'.format(ar),
                                     head + '+{}c'.format(br))
                mr = reprog.search(chars, mr.end())
            else:
                if mr:
                    for kr, vr in mr.groupdict().items():
                        if vr:
                            ar = mr.start(kr)
                            if has_eos:
                                br = m.end() - len(quot)
                            else:
                                br = m.end()

##                            print kr, vr, ar, br, '^D'
                            self.tag_remove('STRING',
                                            head + '+{}c'.format(ar),
                                            head + '+{}c'.format(br))
                            if kr == 'RE_CHARS':  # XXX
                                self.tag_remove('RE_CARET',
                                                head + '+{}c'.format(ar),
                                                head + '+{}c'.format(br))

                            self.tag_add(kr,
                                         head + '+{}c'.format(ar),
                                         head + '+{}c'.format(br))

        if 'u' in prefix:
            spprog = regex.compile(SPECIAL_U)
            fmtprog = regex.compile(FORMAT_U)
        else:
            spprog = regex.compile(SPECIAL)
            fmtprog = regex.compile(FORMAT)

        mf = fmtprog.search(chars, m.start())
        while mf and mf.end() <= m.end():
            for kf, vf in mf.groupdict().items():
                if vf:
                    af, bf = mf.span('FORMAT')
                    self.tag_remove('STRING',
                                    head + '+{}c'.format(af),
                                    head + '+{}c'.format(bf))
                    self.tag_add('FORMAT',
                                 head + '+{}c'.format(af),
                                 head + '+{}c'.format(bf))
            mf = fmtprog.search(chars, mf.end())

        msp = spprog.search(chars, m.start())
        while msp and msp.end() <= m.end():
            for ksp, vsp in msp.groupdict().items():
                if vsp:
                    asp, bsp = msp.span('SPECIAL')
                    self.tag_remove('STRING',
                                    head + '+{}c'.format(asp),
                                    head + '+{}c'.format(bsp))
                    self.tag_remove('FORMAT',
                                    head + '+{}c'.format(asp),
                                    head + '+{}c'.format(bsp))
                    self.tag_add('SPECIAL' if 'r' not in prefix else 'RE_SPECIAL',
                                 head + '+{}c'.format(asp),
                                 head + '+{}c'.format(bsp))
            msp = spprog.search(chars, msp.end())

        if 'ur' in prefix:
            ivprog = regex.compile(INVALID_UR)
        elif 'u' in prefix:
            ivprog = regex.compile(INVALID_U)
        elif 'r' in prefix:
            ivprog = regex.compile(INVALID_R)
        else:
            ivprog = regex.compile(INVALID)

        mi = ivprog.search(chars, m.start())
##        print `mi`
        while mi and mi.end() <= m.end():
            for ki, vi in mi.groupdict().items():
                if vi:
##                    print ki, vi
                    ai, bi = mi.span(ki)
                    self.tag_remove('STRING',
                                    head + '+{}c'.format(ai),
                                    head + '+{}c'.format(bi))
                    self.tag_remove('RE_CHARS',
                                    head + '+{}c'.format(ai),
                                    head + '+{}c'.format(bi))
                    self.tag_add(ki,
                                 head + '+{}c'.format(ai),
                                 head + '+{}c'.format(bi))
            mi = ivprog.search(chars, mi.end())
        else:
            if mi:
                for ki, vi in mi.groupdict().items():
                    if vi:
                        ai = mi.start(ki)
##                        print ki, vi
                        if has_eos:
                            bi = m.end() - len(quot)
                        else:
                            bi = m.end()

                        self.tag_remove('STRING',
                                        head + '+{}c'.format(ai),
                                        head + '+{}c'.format(bi))
                        self.tag_remove('RE_CHARS',
                                        head + '+{}c'.format(ai),
                                        head + '+{}c'.format(bi))
                        self.tag_add(ki,
                                     head + '+{}c'.format(ai),
                                     head + '+{}c'.format(bi))

    elif key in ('FUNCDEF', 'DEFINITION'):
        sprog = regex.compile(SPECIAL_M)
        ms = sprog.search(chars, m.start())
        if ms and ms.end() <= m.end():
            as_, bs = ms.span('SPECIAL_M')
            self.tag_remove(key,
                            head + '+{}c'.format(as_),
                            head + '+{}c'.format(bs))
            self.tag_add('SPECIAL_M',
                         head + '+{}c'.format(as_),
                         head + '+{}c'.format(bs))

    elif key in ('COMMENT',):
        kprog = regex.compile(KEY_COMMENT)
        mk = kprog.search(chars, m.start())
        while mk and mk.end() <= m.end():
            for kk, vk in mk.groupdict().items():
                ak, bk = mk.span('KEYWORD')
                self.tag_remove(key,
                                head + '+{}c'.format(ak),
                                head + '+{}c'.format(bk))
                self.tag_add('KEYWORD',
                             head + '+{}c'.format(ak),
                             head + '+{}c'.format(bk))
            mk = kprog.search(chars, mk.end())

