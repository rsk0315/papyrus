import regex

def any(name, alternates):
    return "(?P<{}>{})".format(name, r'|'.join(alternates))


keyword = r'(?<!$|@@?)\b(?:' + r'|'.join(
    [
        'alias',    'and',      r'(?<!^=)begin',        'break',    'case',
        'class',    'def',      r'defined\?',           'do',       'else',
        'elsif',    r'(?<!^=)end',                      'ensure',   'for',
        'if',       'in',       'module',   'next',     'not',      'or',
        'redo',     'rescue',   'retry',    'return',               'super',
        'then',                 'undef',    'unless',   'until',    'when',
        'while',    'yield',

        'nil',      'true',     'false',    'self',
        r'__(?:LINE|FILE|ENCODING)__',
    ]
) + r')\b'

operator = r'(?<!\b(?:def|class)\b)' + r'|'.join(
    [
        r'=>|[,`;]',
        r'(?:\*\*|<<|>>|\&\&|\|\||[+\-*/%&|^])=',
        r'::|<<|>>|\*\*|[<>]=|<=>|=[=~]|===|![=~]|\&\&|\|\||\.\.\.?',
##        r'\[\]',
        r'\b(?:and|or|not)\b',
        r'[+!~\-*%&|^><?:@]',
        r'=(?!\bbegin\b)',

        r'(?<!'
            r'(?:'
                r'\b(?:if|else|elsif|case|for|return|then|unless|until|while)'
            r'|'r'[([{<~+\-*=~!]'
            r')'
            r'\s*'
        r')'
        r'/',
    ]
)

module_func = r'\b(?:' + r'|'.join(
    [
        'Array',    'Complex',  'Float',    'Hash',     'Integer',  'Rational',
        'String',   r'__(?:callee|dir|method)__',       '`',        'abort',
        'at_exit',  r'autoload\??',         'binding',  r'block_given\?',
        r'iterator\?',          'caller',   'caller_locations',     'catch',
        'chomp',    'chop',     'eval',     'exec',     r'exit!?',  'fail',
        'raise',    'fork',     'format',   'sprintf',  'gets',
        'global_variables',     'gsub',     'lambda',   'proc',     'load',
        'local_variables',      'loop',     'open',     'p',        r'printf?',
        r'put[cs]', 'rand',     r'readlines?'           'require',
        'require_relative',     'select',   'set_trace_func',       'sleep',
        'spawn',    'srand',    'sub',      'syscall',  'system',   'test',
        'throw',    'trace_var',            'trap',     'untrace_var',
        'warn',
    ]
) + r')\b'

special_var = r'\$(?:' + r'|'.join(
    [
        'LOADED_FEATURES',      'LOAD_PATH',            'KCODE',    'DEBUG',
        'VERBOSE',  'PROGRAM_NAME',         'FILENAME', 'SAFE',
        r'std(?:in|out|err)',   r'-[0FIKWadilpvw]',     r'1[01]',   r'[\dF]',
    ]
) + r'\b)' + r'''|\$[!"$&'*+,/;:.<=>?@\\_`~]'''

number = r'\b(?:' + r'|'.join(
    [
        r'{z}(?:\.{z})?(?:[Ee][+-]?{z})',
        r'0[Xx][0-9A-Fa-f]+(?:_[0-9A-Fa-f]+)*',
        r'0o[0-7]+(?:_[0-7]+)*',
        r'0[Bb][01]+(?:_[01]+)*',
        r'{z}\.{z}',
        r'{z}',
    ]
).format(
    z=r'(?:[0-9]+(?:_[0-9]+)*)',
    d=r'(?:[1-9]+(?:_[0-9]+)*)',
) + r')'

sqstr = r"'[^\\']*(?:\\.[^\\']*)*'?"
dqstr = r'"{e}*(?:\\.{e}*)*"?'.format(
    e=(
        r'(?:'
            r'[^\\"#]'
        r'|'r'#\{(?:[^#}]*(?:#[^\n]*\n)?)*\}?'
        r'|'r'#(?:\$(?:[_A-Za-z]+|[^-]|-.|1[01]|\d)|[_A-Za-z]\w*)'
        r')'
    ),
)  # todo for expanding
regstr = (
##    r'(?<![])}}>\w]\s*)'
##    (
##        r'(?<=\b(?:' + r'|'.join(
##            [
##                'if', 'else', 'elsif', 'case', 'for', 'return', 'then',
##                'unless', 'until', 'while',
##            ]
##        ) + r'\s*)|^\s*)'
##    ) +
##    r'/{e}*(?:\\.{e}*)*(?:/[ioxmnesu]*)?'
    r'(?<=\b{c}\s*|[~!=]\s*)'
    r'/{e}*(?:\\.{e}*)*(?:/[ioxmnesu]*)?'
).format(
    c=r'|'.join([
        'if', 'else', 'elsif', 'case', 'for', 'return', 'then',
        'unless', 'until', 'while',
    ]),
    e=(
        r'(?:'
            r'[^\\/#]'
        r'|'r'#\{(?:[^#}]*(?:#[^\n]*\n)?)*\}?'
        r'|'r'#(?:\$(?:[_A-Za-z]+|[^-]|-.|1[01]|\d)|[_A-Za-z]\w*)'
#        r'|'r'#(?:\$?-?)[_A-Za-z]\w*'
        r')'
    ),
)  # todo for expanding

comment = [
    r'#[^\n]*',
    r'^=begin\b[^\n]*\n(?:[^\n]*\n)*?(?:^=end\b[^\n]*)',
    r'^=begin\b[^\n]*\n(?:[^\n]*\n)*',
    r'^__END__$.+',
]

definition = (
    r'(?:' + r'|'.join(
        [
            r'[_A-Za-z]\w*',
            r'<=>|===|[!=][=~]|<[=<]|>[=>]|[+-]@|\[\]=?|\*\*',
            r'[|^&><+\-*/%~`!]',
        ]
    ) + r')'
)

funcdef = r'(?<=\bdef\s+)' + definition
classdef = r'(?<=\bclass\s+)' + definition

KEYWORD = any('KEYWORD', [keyword, operator])
BUILTIN = any('BUILTIN', [module_func, special_var, number])
STRING = any('STRING', [sqstr, dqstr, regstr])  # todo need regstr
COMMENT = any('COMMENT', comment)
DEFINITION = any('DEFINITION', [funcdef, classdef])
