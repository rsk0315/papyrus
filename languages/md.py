KEYWORD = r'(?P<KEYWORD>(?<=^[ \t]*)[-*]+)'
BUILTIN = (
    r'(?P<BUILTIN>'
        r'(?<!\[)'
        r'(?:'
            r'```[^`\\]*(?:(?:\\.|`(?!``))[^`\\]*)*(?:```)?'
        r'|'r'`[^`\\\n]*(?:\\.[^`\\\n]*)*`?'
        r')'
    r')'
)

STRING = (
    r'(?P<STRING>'
        r'(?<=\[)'
        r'[^\]]+'
    r'|'r'#+'
    r')'
)

COMMENT = VARIANT = DEFINITION = ''

MISC = (
    r'(?P<LINK>'
        r'(?<=\]\()'
        r'[^)]+'
    r')'
)
