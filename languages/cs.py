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
##    'wchar_t',  'char16_t', 'char32_t',

    'namespace' #
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
##    'vector', 'string', 'queue', 'list', 'array', 'stack', 'pair', 'deque',
##    'set', 'map', 'tuple', 'iterator', 'complex', 'bitset',
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
##    r'[Rr]"\([^"\\\n]*(?:\\.[^"\\\n]*)*(?:\)")?',
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


definition = [
    (
        r'(?<!'
            r'(?:'
                r'\b(?:throw|return|case|static|const|volatile|else|typename|ifn?def|if|inline|(?:un)?signed)\b'
            r'|'r'^#define{t}{w}\b'
            r'|'r'\btypedef\b(?:{t}?{w}{t}?(?:<|>?::){t}?)*'
             r')'
            r'{t}?'
        r')'

        r'(?<='
            r'(?:'
                r'(?<=(?:^|[#;{{(]|>?::){s}*)'              # ...;
                r'{w}(?:{t}+{w})*(?:{s}|\[\d*\])+'         # int foo;
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
                    r'(?:\[[\d_A-Z]*\]{t}*)+'
                    # int foo[1]={1}, bar;
                    r'(?:={t}*\{{[^;]*\}})?'                # array
                    # vector<int> foo(1), bar;
                r'|'r'\([^:;()]*(?:\(\w*\)[^:;()]*)*\)'
##                r'|'r'\((?:\)(?!{s}*\w)|[^):;])*\)'         # constructor
##                r'|'r'(?P<C>\((?:[^();:]+|(?&C))*\))'     # xxx
                r'|'r'={s}*'
                    r'(?:'
                        # int foo=sqrt(2), bar;
                        r'[^/(,:;]+\([^:;()]*'
                        r'(?:\(\w*\)[^:;()]*)*'
                        r'\)[^),:;]*'     # todo func
                        # int foo=ham[1], bar;
                    r'|'r'[^[,:;]+\[[^:;[\]]*\][^\],:;]*'
                        # char foo='A', bar;
                    r'|'r"'(?:[^\\]|\\[^Xx0-7]|\\.+)'"      # todo char
                        # string foo="FOO", bar;
##                    r'|'r'@?"[^"\\]*(?:\\.[^"\\]*)*"'       # xxx string
                        # int foo=1+sqrt(2)+a, bar;
                    r'|'r'[-\w]+(?:[+\-*/%&|^~!?:.,{{}}<>]+\w*)*'       # xxx other
                    r')'
                r')?'
                # int foo, bar::baz, qux;
                r'{s}*(?:(?<=\)?),|>?::(?#|<))(?:{t}|[&*])*'
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
                r'\b(?:throw|case|static|const|volatile|else|typename|ifn?def|if|inline)\b'
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
##                        r'@?"[^"\\]*(?:\\.[^"\\]*)*"'       # xxx string
                        # int foo=1+sqrt(2)+a, bar;
                    r'|'r'[-\w]+(?:[+\-*/%&|^~!?:.,{{}}]+\w*)*'       # xxx other
                    r')'
                r')?'
                # int foo, bar::baz, qux;
                r'{s}*(?:,|>?::(?#|<))(?:{t}|[&*])*'
            r')*'
        r')'
        #r'{w}(?!,(?=[ \t]*[^*_A-Za-z])|[^=\s,;])'
        r'{w}(?=,(?=[ \t]*[*&_A-Za-z])|[ \t]*[=,;:\[]|$)'
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
    r'|'r'(?:<<|>>|[+\-*/%^&|<>!=])=?'
    r'|'r'\b(?:new|delete)\b'
    r'|'r'\(\s*\)|\[\s*\]'
    r'|'r'[~,]'
    r'|'r'""\s*[_A-Za-z]\w*'
    r')',

    # constructor in struct or class
    r'(?<![,(\-+/^|<>=%!?.:]{s}*){w}'
    #r'(?={s}*\([^{{;]*\){s}*[{{:])'.format(
    r'(?={s}*\((?:\w+[ \t&<>*]+\w+(?:[^;{{])*)*\){s}*[{{:])'.format(
        w=r'(?:\b[_A-Za-z]\w*)',
        s=(
            r'(?:'
                r'\s+'
##            r'|'r'//[^\r\n]*'
##            r'|'r'/\*[^*]*(?:\*[^/]?|[^*]*)*\*/'
            r')'
        )
    ),

##    # todo function which returns pointer
##    (
##        r'(?<={w}(?:{t}+{w})*{t}?\*+{t}?)'
##        r'{w}(?=\()'
##    ).format(w=r'(?:[_A-Za-z]\w*)', t=r'(?:[ \t]+)')

]

comment = [
    r'(?P<COMMENT>//(?P<LINE_COMMENT>[^\n]*))',
    r'(?P<BLOCK_COMMENT>/\*[^*]*(?:\*(?:[^/*]|\*(?!/))|[^*])*(?:\*\*?/)?)',
]

userdefined = [
##    r'\b\w+_t\b',
    r'\b[_A-Za-z]\w*_t(?!\w)',

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
            r'\){s}*[{{]'
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

    r'(?P<KEYWORD>\[:[^:]+:\])',
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

freq_used_val = [
    r'\b(?:' + r'|'.join([
        'true', 'false',
##        'cin', 'cout', 'cerr', 'endl',
    ]) + r')\b'
]

KEYWORD = (
    any('KEYWORD', keyword) + r'|' +
    any('STL_CLASSES', stl_classes)
)
BUILTIN = (
    any('PREPROCESSOR', preprocessor) + r'|' +
    any('BUILTIN', number+userdefined+freq_used_val) + r'|' +
    any('OPERATOR', operator)
)
##COMMENT = any('COMMENT', comment)
COMMENT = r'|'.join(comment)
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

REGEX_PAT = regex.compile(regex_)


def read_twice(self, head, key, value, chars, m):
    if key == 'STRING' and value[0] not in "@Rr":
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

    elif key == 'STRING' and value[0] in "Rr":
        rprog = regex.compile(REGEX_PAT)

        self.tag_remove('STRING',
                        head + '+{}c'.format(m.start()),
                        head + '+{}c'.format(m.start()+1))
        self.tag_add('OPERATOR',
                     head + '+{}c'.format(m.start()),
                     head + '+{}c'.format(m.start()+1))

        if len(regex.search(r'(\\*)"?$', value).group(1)) % 2:
            has_eos = True
        else:
            has_eos = False

        mr = rprog.search(chars, m.start())
        while mr and mr.end() <= m.end():
            for kr, vr in mr.groupdict().items():
                if vr:
                    ar, br = mr.span(kr)
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

            mr = rprog.search(chars, mr.end())
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

##        rprog = regex.compile(r'\\.|(?P<KEYWORD>\[:[^:]+:\])')
##        mr = rprog.search(chars, m.start())
##        while mr and mr.end() <= m.end():
##            for kr, vr in mr.groupdict().items():
##                if vr:
##                    ar, br = mr.span(kr)
##                    self.tag_remove('STRING',
##                                    head + '+{}c'.format(ar),
##                                    head + '+{}c'.format(br))
##                    self.tag_add(kr,
##                                    head + '+{}c'.format(ar),
##                                    head + '+{}c'.format(br))
##
##            mr = rprog.search(chars, mr.end())
##        else:
##            if mr:
##                for kr, vr in mr.groupdict().items():
##                    if vr:
##                        ar = mr.start(kr)
##                        if has_eos:
##                            br = m.end() - 1
##                        else:
##                            br = m.end()
##
##                        self.tag_remove('STRING',
##                                        head + '+{}c'.format(ar),
##                                        head + '+{}c'.format(br))
##                        self.tag_add(kr,
##                                     head + '+{}c'.format(ar),
##                                     head + '+{}c'.format(br))

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

    elif key == 'LINE_COMMENT':
        cprog = regex.compile(ur'(?P<NONASCIIC>[^\0-\x7f]+)')
        mc = cprog.search(chars, m.start())
        while mc and mc.end() <= m.end():
            for kc, vc in mc.groupdict().items():
                if vc:
                    ac, bc = mc.span(kc)
                    self.tag_remove(key,
                                    head + '+{}c'.format(ac),
                                    head + '+{}c'.format(bc))
                    self.tag_remove('COMMENT',
                                    head + '+{}c'.format(ac),
                                    head + '+{}c'.format(bc))
                    self.tag_add(kc,
                                    head + '+{}c'.format(ac),
                                    head + '+{}c'.format(bc))
            mc = cprog.search(chars, mc.end())

    elif key == 'BLOCK_COMMENT':
        cprog = regex.compile(ur'(?P<NONASCIIB>[^\0-\x7f]+)')
        mc = cprog.search(chars, m.start())
        while mc and mc.end() <= m.end():
            for kc, vc in mc.groupdict().items():
                if vc:
                    ac, bc = mc.span(kc)
                    self.tag_remove(key,
                                    head + '+{}c'.format(ac),
                                    head + '+{}c'.format(bc))
                    self.tag_remove('COMMENT',
                                    head + '+{}c'.format(ac),
                                    head + '+{}c'.format(bc))
                    self.tag_add(kc,
                                    head + '+{}c'.format(ac),
                                    head + '+{}c'.format(bc))
            mc = cprog.search(chars, mc.end())
