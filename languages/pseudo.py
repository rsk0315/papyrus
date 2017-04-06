keywords = [
    'for', 'if', 'else', 'while', 'function', 'procedure',
    'input', 'output', 'return',
    r'end(?:-\w+)?',
]

KEYWORD = r'^[ \t]*(?P<BOLD>' + r'|'.join(keywords) + r')\b'
BUILTIN = ''
STRING = ''
COMMENT = r'^[ \t]*(?P<COMMENT>[#;][^\n]*)'
DEFINITION = r'(?P<ITALIC>(?<=\b(?:function|procedure)\b[ \t]*)[_A-Za-z]\w*)'

VARIANT = ''
