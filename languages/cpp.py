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
                r'\b(?:throw|return|case|static|const|volatile|else|for|while|ifn?def|inline)\b'
            r'|'r'^#define{t}{w}\b'
            r'|'r'\btypedef\b(?:{t}?{w}{t}?(?:<|>?::){t}?)*'
             r')'
            r'{t}?'
        r')'

        r'(?<='
            r'(?:'
                r'(?<=(?:^|[#;{{(]|>?::){s}*)'              # ...;
                r'{w}(?:{t}+{w})*(?:{s}(?#|[*&]))+'         # int foo;
            r'|'r'(?<=\}}{s}*)'                             # struct {...} foo;
            r'|'r'(?<=(?:^|[#;{{])[^;<()=]*<[^();-]*)>'      
                r'(?:::{t}*{w}{s}+)'                        # map<T,T>::iterator foo;
                r'(?:{s}|\*)*'
            r'|'r'(?<=(?:^|[#;{{])[^;<()=]*<[^();-]*)>'     # vector<int> foo;
                r'(?:{t}|\*)*'
            r')'

            r'(?:'
                r'{w}{s}*'
                r'(?:'
                    # int foo[1], bar;
                    r'(?:\[\d*\]{t}*)+'
                    # int foo[1]={1}, bar;
                    r'(?:={t}*\{{[^;]*\}})?'                # array
                    # vector<int> foo(1), bar;
##                r'|'r'\((?:\)(?!{s}*\w)|[^):;])*\)'         # constructor
                r'|'r'(?P<C>\((?:[^();:]+|(?&C))*\))'
                r'|'r'={s}*'
                    r'(?:'
                        # int foo=sqrt(2), bar;
                        r'[^(,:;]+\([^:;()]*\)[^),:;]'      # todo func
                        # char foo='A', bar;
                    r'|'r"'(?:[^\\]|\\[^Xx0-7]|\\.+)'"      # todo char
                        # string foo="FOO", bar;
                    r'|'r'@?"[^"\\]*(?:\\.[^"\\]*)*"'       # string
                        # int foo=1+sqrt(2)+a, bar;
                    r'|'r'[\w()+\-*/%&|^~!?:.,{{}}]+'       # xxx other
                    r')'
                r')?'
                # int foo, bar::baz, qux;
                r'{s}*(?:(?<=\)?),|>?::(?#|<))(?:{t}(?#|\*))*'
            r')*'
        r')'
        r'{w}'
    ).format(
        w=r'(?:\b[_A-Za-z]\w*)',
        s=(
            r'(?:'
                r'(?:[ \t]+)'
##            r'|'r'//[^\r\n]*'
##            r'|'r'/\*[^*]*(?:\*[^/]?|[^*]*)*\*/'
            r')'
        ),
        t=r'(?:[ \t]+)',
        p=r'^#[^\r\n\\]*(?:\\.|[^\r\n\\]*)*',  # todo no need?
    ),

    # int *foo, *bar;
    (
        r'(?<!'
            r'(?:'
                r'\b(?:throw|case|static|const|volatile|else|for|while|ifn?def|inline)\b'
            r'|'r'^#define{t}{w}\b'
            r'|'r'\btypedef\b(?:{t}?{w}{t}?(?:<|>?::){t}?)*'
            r'|'r'\breturn[ \t*]+(?:{w}{t}?\*[ \t*]*)?'
            r')'
            r'{t}?'
        r')'

        r'(?<='
            r'(?:'
                r'(?<=(?:^|[#;{{(]|>?::){s}*)'              # ...;
                r'{w}(?:{t}+{w})*'                          # int *foo;
            r'|'r'(?<=\}})'                                 # struct {...} *foo;
            r'|'r'(?<=(?:^|[#;{{])[^;<()=]*<[^();-]*)>'      
                r'(?:::{t}*{w}{s}+)'                        # map<T,T>::iterator *foo;
            r'|'r'(?<=(?:^|[#;{{])[^;<()=]*<[^();-]*)>'     # vector<int> *foo;
            r')'
            r'{t}?[*&](?:{t}|[*&])*'

            r'(?:'
                r'{w}{s}*'
                r'(?:'
                    # int foo[1], bar;
                    r'(?:\[\d*\]{t}*)+'
                    # int foo[1]={1}, bar;
                    r'(?:={t}*\{{[^;]*\}})?'                # array
                    # vector<int> foo(1), bar;
                r'|'r'={s}*'
                    r'(?:'
                        # string foo="FOO", bar;
                        r'@?"[^"\\]*(?:\\.[^"\\]*)*"'       # string
                        # int foo=1+sqrt(2)+a, bar;
                    r'|'r'[\w()+\-*/%&|^~!?:.,{{}}]+'       # xxx other
                    r')'
                r')?'
                # int foo, bar::baz, qux;
                r'{s}*(?:,|>?::(?#|<))(?:{t}|\*)*'
            r')*'
        r')'
        #r'{w}(?!,(?=[ \t]*[^*_A-Za-z])|[^=\s,;])'
        r'{w}(?=,(?=[ \t]*[*_A-Za-z])|[ \t]*[=,;]|$)'
    ).format(
        w=r'(?:\b[_A-Za-z]\w*)',
        s=(
            r'(?:'
                r'(?:[ \t]+)'
            r')'
        ),
        t=r'(?:[ \t]+)',
        p=r'^#[^\r\n\\]*(?:\\.|[^\r\n\\]*)*',  # todo no need?
    ),

    # <foo>::bar baz
    (
        r'(?<='
            r'(?<=\}})[* \t]*'

            r'(?:'
                r'\b[_A-Za-z]\w*'
##                r'(?:\s*\[\d*\]\s*)*'
                r'\s*(?:,|::)[*\s]*'
            r')*'
        r')'
        r'\b[_A-Za-z]\w*'
    ).format(w=r'(?:\b[A-Za-z]\w*)', t=r'(?:[ \t]*)'),

    # operator overload
    r'(?<=\boperator\b\s*)'
    r'(?:'
        r'\+\+|\&\&|\|\||--'
    r'|'r'->\*?'
    r'|'r'(?:[+\-*/%^&|<>!=]|<<|>>)=?'
    r'|'r'\b(?:new|delete)\b'
    r'|'r'\(\s*\)|\[\s*\]'
    r'|'r'[~,]'
    r')',

    # constructor in struct or class
    r'(?<![,(\-+*/^&|<>=%!.]{s}*){w}(?={s}*\([^{{;]*\){s}*[{{:])'.format(
        w=r'(?:\b[_A-Za-z]\w*)',
        s=(
            r'(?:'
                r'\s+'
##            r'|'r'//[^\r\n]*'
##            r'|'r'/\*[^*]*(?:\*[^/]?|[^*]*)*\*/'
            r')'
        )
    ),

    # todo function which returns pointer
    (
        r'(?<={w}(?:{t}+{w})*{t}?\*+{t}?)'
        r'{w}(?=\()'
    ).format(w=r'(?:[_A-Za-z]\w*)', t=r'(?:[ \t]+)')

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
            r'(?:<[^(;]+>)?'
            r'\('
            r'(?!'
                r'{s}*'
                r'(?:'
                    r'{w}{s}*'
                    r'{w}(?:{s}*={s}*[^,);{{]+)?'
                    r'{s}*'
                r')*'
            r'{s}*'
            r'\){s}*[{{:]'
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

    elif key == 'DEFINITION':
        i = 0
        getch = lambda k: self.get(
            head+'{:+}c'.format(k), head+'{:+}c'.format(k+1))
        char = getch(m.end()-i-1)
        while i <= 160:  # about 2 lines; avoid infinite loop (heuristics)
##            print `char`
            if char in ';)':
                return
            elif char in '(':
                line = self.get(
                        head+'{:+}c'.format(m.end()-i-80),
                        head+'{:+}c'.format(m.end()-i-1))
                if regex.search(r'\b(?:for|while)\s*$', line, flags=regex.M):
                    return

                self.tag_remove('DEFINITION',
                                head + '+{}c'.format(m.start()),
                                head + '+{}c'.format(m.end()))
                return
            i += 1
            char = getch(m.end()-i-1)
