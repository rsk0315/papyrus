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
    'default',  'do',       'double',   'else',     'enum',     'extern',
    'float',    'for',      'goto',     'if',       'int',      'long',
    'register', 'return',   'short',    'signed',   'sizeof',   'static',
    'struct',   'switch',   'typedef',  'union',    'unsigned', 'void',
    'volatile', 'while',
    'nullptr',  'class',    'mutable',  'thread_local',         'friend',
    'constexpr',            'explicit', 'inline',   'virtual',  'public',
    'protected',            'private',  'operator', 'template', 'bad_cast',
    'bad_typeid',           'catch',    'const_cast',           #'delete',
    'dynamic_cast',         'except',   'finally',  # 'namespace',
    #'new',
    'reinterpret_cast',     'static_cast',          'throw',
    'type_info',            'typeid',   r'using(?:\s+namespace)?',
    'xalloc',   'asm',      'typename',
    r'(?<!\boperator\b\s*)(?:new|delete)',
])
types = r'|'.join([
    'char',     'const',    'double',   'enum',     'float',    'int',
    'long',     'register', 'short',    'signed',   'static',   'struct',
    'typedef',  'union',    'unsigned', 'void',     'volatile',
    'bool',     # 'true',     'false',
    'wchar_t',  'char16_t', 'char32_t',

    'namespace' #
])
keyword = [
    r'\b(?:{0})(?:\s+(?:{0}))*\b'.format(keywords+r'|'+types),
]

preprocessor = [
    r'(?<=#[ \t]*){0}\b'.format(i) for i in [
        'include',  'define',   r'ifn?def', 'endif',    'if',       'elif',
        'else',     'error',    'warning',  'pragma',   'pragma once',
        'pragma comment',
    ]
]

string = [
    r'\'(?:[^\\\n]|\\[abfnrtv\'"?\\]|\\[0-7]{1,3}|\\[Xx][0-9A-Fa-f]{1,2})\'?',
    r'"[^"\\\n]*(?:(?:\\.)+[^"\\\n]*)*"?',
    r'@"[^"]*(?:(?:"")+[^"]*)*"?',
    r'(?m)(?<=^[ \t]*#[ \t]*include)\s*<[^>\n]*>?'
]

number = [
    r'(?<!\w){0}'.format(i) for i in [
        r'(?:\.\d+|\d+\.\d*)(?:[Ee][+-]?\d+)?',
        r'\d+(?:[Ee][+-]?\d+)',  # todo
        r'(?:0[Qq][0-3]+|0[Bb][01]+)',  # todo
        r'(?:0[Xx][\dA-Fa-f]+|0[0-7]+|[1-9]\d*|0)[ULul]*',
    ]
]

operator = [
    r'(?<!\boperator\b)[-!%&+*|<^>?:=~/,]',
    r';',
    r'##',
    r'(?<!^)#',
]


definition = [
    (
        r'(?<!'
            r'(?:'
                r'\b(?:typedef|throw|return|case|static|const)'
            r'|'r'#define{s}{w}'
            r')'
            r'\b{s}*'
        r')'

        r'(?<='
            r'(?<![<([{{])'

            r'(?:'
                r'(?<=(?:\{{|\A|;|{p}){s}*)'
                r'{w}(?:(?:{s}|\*)+{w})*(?:{s}|\*)+'
            r'|'r'(?<=\}})'
            r'|'r'(?<=(?:\{{|\A|;|{p})[^;<(=]*<[^;]*)>(?:{s}|\*)*'
            r')'

            r'(?:'
                r'{w}'
                r'(?:'
                    r'{s}*\[\d*\]{s}*(?:=\{{.*\}})?'        # array
                r'|'r'{s}*\((?:\)(?!{s}*\w)|[^);])*\)'     # constructor
                r'|'r'{s}*={s}*'
                    r'(?:'
                        r'[^(]*\([^,;]*\)[^,;]*'            # todo func
                    r'|'r"'(?:[^\\]|\\[^Xx0-7]|\\.+)'"      # todo char
                    r'|'r'@?"[^"\\]*(?:\\.[^"\\]*)*"'       # string
                    r'|'r'[^,();]*'
                    r')'
                r')?'
                r'{s}*(?:,|::)(?:{s}|\*)*'
            r')*'
        r')'
        r'{w}'
    ).format(
        w=r'(?:\b[_A-Za-z]\w*)',
        s=(
            r'(?:'
                r'\s+'
            r'|'r'//[^\r\n]*'
            r'|'r'/\*[^*]*(?:\*[^/]?|[^*]*)*\*/'
            r')'
        ),
        p=r'^#[^\r\n\\]*(?:\\.|[^\r\n\\]*)*',  # todo no need?
    ),

    r'(?<='
        r'(?<=\})[* \t]*'

        r'(?:'
            r'\b[_A-Za-z]\w*'
            r'(?:\s*\[\d*\]\s*)*'
            r'\s*(?:,|::)[*\s]*'
        r')*'
    r')'
    r'\b[_A-Za-z]\w*',


    r'(?<=\boperator\b\s*)'
    r'(?:'
        r'\+\+|\&\&|\|\||--'
    r'|'r'->\*?'
    r'|'r'(?:[+\-*/%^&|<>!=]|<<|>>)=?'
    r'|'r'\b(?:new|delete)\b'
    r'|'r'\(\s*\)|\[\s*\]'
    r'|'r'[~,]'
    r')',

    r'{w}(?={s}*\([^);]*\){s}*\{{)'.format(
        w=r'(?:\b[_A-Za-z]\w*)',
        s=(
            r'(?:'
                r'\s+'
            r'|'r'//[^\r\n]*'
            r'|'r'/\*[^*]*(?:\*[^/]?|[^*]*)*\*/'
            r')'
        )
    ),

]

comment = [
    r'//[^\n]*',
    r'/\*[^*]*(?:\*(?:[^/*]|\*(?!/))|[^*])*(?:\*\*?/)?',
]

userdefined = [
    r'\b\w+_t\b',

    (
        r'{w}'
        r'(?='
            r'{s}*\('
            r'(?!'
                r'{s}*'
                r'(?:'
                    r'{w}{s}*'
                    r'{w}(?:{s}*={s}*[^,);{{]+)?'
                    r'{s}*'
                r')*'
            r'{s}*'
            r'\){s}*\{{'
            r')'
        r')'
    ).format(
        w=r'\b[_A-Za-z]\w*',
        s=(
            r'(?:'
                r'\s+'
            r'|'r'//[^\r\n]*'
            r'|'r'/\*[^*]*(?:\*[^/]?|[^*]*)*\*/'
            r')'
        ),
    ),
]

KEYWORD = any('KEYWORD', keyword)
BUILTIN = (
    any('PREPROCESSOR', preprocessor) + r'|' +
    any('BUILTIN', number+userdefined+[r'\b(?:true|false)\b']) + r'|' +
    any('OPERATOR', operator)
)
COMMENT = any('COMMENT', comment)
STRING = any('STRING', string)
DEFINITION = (
    any('DEFINITION', definition)
)
SP_VARIABLE = r'(?P<SP_VARIABLE>\bthis\b)'

CONSTANT = any('CONSTANT', [r'\b[_A-Z][_0-9A-Z]+\b'])


MISC = r'|'.join(
    [
        SP_VARIABLE,
        CONSTANT,
        r'(?P<SHARP>#)',
        r'(?P<PUNC>[(){}[\]])',
        ur'(?P<ERROR>\u3000)',
    ]
)


DEF_POINTER_COMMA = r'(?P<SYMBOL>[*,]+)'
SPECIAL_CHAR = (
    r'(?P<SPECIAL>\\'
        r'(?:'
            r'[abtnvfr]|[Xx][0-9A-Fa-f]{1,2}|[0-7]{1,3}'
        r')'
    r')'
r'|'r'(?P<FORMAT>%'
        r'(?:[-+ 0#])?'
        r'(?:\d+)?'
        r'(?:\.\d+)?'
        r'(?:[Luhl]+|I\d+)?'
        r'(?:[diuoxXcsfeEgGp%])'
    r')'
)

def read_twice(self, head, key, value, chars, m):
    if key == 'STRING' and value[0] not in "'@":
        cprog = regex.compile(SPECIAL_CHAR)
        mc = cprog.search(chars, m.start())
        while mc and mc.end() <= m.end():
            for kc, vc in mc.groupdict().items():
                if vc:
                    ac, bc = mc.span(kc)
                    self.tag_remove('STRING',
                                    head + '+{}c'.format(ac),
                                    head + '+{}c'.format(bc))
                    self.tag_add(kc,
                                    head + '+{}c'.format(ac),
                                    head + '+{}c'.format(bc))
            mc = cprog.search(chars, mc.end())
