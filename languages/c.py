#!/usr/bin/env python

import regex


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
])
types = r'|'.join([
    'char',     'const',    'double',   'enum',     'float',    'int',
    'long',     'register', 'short',    'signed',   'static',   'struct',
    'typedef',  'union',    'unsigned', 'void',     'volatile',
])
keyword = [
    r'\b(?:{0})(?:\s+(?:{0}))*\b'.format(keywords+r'|'+types),
]

preprocessor = [
    r'(?<=#[ \t]*){0}'.format(i) for i in [
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
        r'(?:0[Xx][\dA-Fa-f]+|0[0-7]+|[1-9]\d*|0)[ULul]*',
    ]
]

operator = [
    r'(?<!\boperator\b)[-!%&+*|<^>?:=~/,]',
    r';',
    r'##',
]


definition = [
    (
        r'(?<!\b(?:typedef|throw|return|case)\b\s*)'
        r'(?<='
            r'(?<!(?:[-=+/*(,|&^~]|\b(?:return|throw)\b)\s*)'

            r'(?:'
                r'{name}(?:[*\s]+{name})*[*\s]+'            # type name
            # r'|'r'(?<=}})[* \t]*'                         # struct
            r')'

            r'(?:'
                r'{name}'                                   # variable
                r'(?:\s*\[\d*\]\s*)*'                       # array
                r'(?:'
                    r'='                                    # initialization
                    r'(?:'
                        r'{{.+}}'                           # array
                    r'|'r"'[^']*'"                          # char
                    r'|'r'"[^"]*(?:\\.[^"]*)*"'             # string
                    r'|'r'[^,]*'                            # constant, etc.
                    r')'
                r')?'
                r'\s*,[*\s]*'
            r')*'
        r')'
        r'{name}'
    ).format(name=r'(?:\b[_A-Za-z]\w*)'),
]

comment = [
    r'//[^\n]*',
    r'/\*[^*]*(?:\*(?:[^/*]|\*(?!/))|[^*])*(?:\*\*?/)?',
]

userdefined = [
    r'\b\w+_t\b',   r'\b[_A-Za-z]\w*(?=\s*\()',
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

CONSTANT = any('CONSTANT', [r'\b[_A-Z][_0-9A-Z]+\b'])


MISC = r'|'.join([CONSTANT, r'(?P<SHARP>#)', r'(?P<PUNC>[(){}[\]])'])


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
        r'(?:[Luhl]+)?'
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
