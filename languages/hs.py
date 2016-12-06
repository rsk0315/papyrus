#!/usr/bin/env python

import regex
#from idlelib.languages.configures import *

def any(name, alternates):
    "Return a named group pattern matching list of alternates."
    return r"(?P<{name}>{pattern})".format(
        name=name,
        pattern=r'|'.join(alternates),
    )

builtin_operators = [
    "!!",   "$!",   "$",    "&&",   "+",    "++",   "-",    ".",    "/",
    "/=",   "<",    "<=",   "=<<",  "==",   ">",    ">=",   ">>",   ">>=",
    "^",    "^^",   "||",
]

operators = [
    r'\.\.', r'::?', r'<-', r'[-=]>', 
    r'[!#$%&*+.,/<=>?@\\^|~]',
    r'--(?! )',
    r'-(?!-)',
    r"`[_a-z][\w']*`",
]

builtin_types = [
    "Bool",     "Bounded",  "Char",     "Double",   "EQ",       "Either",
    "Enum",     "Eq",       "False",    "FilePath", "Float",    "Floating",
    "Fractional",           "Functor",  "GT",       "IO",       "IOError",
    "Int",      "Integer",  "Integral", "Just",     "LT",       "Left",
    "Maybe",    "Monad",    "Nothing",  "Num",      "Ord",      "Ordering",
    "Rational", "Read",     "ReadS",    "Real",     "RealFloat",
    "RealFrac", "Right",    "Show",     "ShowS",    "String",   "True",
]

numbers = [
    r"(?:true|false)",
    r"\d+(?:\.\d+)?(?:[Ee][+-]?\d+)",
    r"\d+\.\d+",
    r"[1-9]\d*",
    r"0[Oo][0-7]+",
    r"0[Xx][0-9A-Fa-f]+",
    r"0",
]

numbers = [
    r'\b(?:' + r'|'.join(numbers) + r')\b'
]

keywords = builtin_types + [
    "case",     "class",    "data",     "default",  "deriving", "do",
    "else",     "if",       "import",   "in",       r"infix[lr]?",
    "instance", "let",      "module",   "newtype",  "of",       "then",
    "type",     "where",    "_",
]

builtin_funcs = [
    "abs",      r"acosh?",  "all",      "and",      "any",
    "appendFile",           "asTypeOf", r"asinh?",  r"atan[2h]?",
    "break",    "ceiling",  "compare",  "concat",
    "concatMap",            "const",    r"cosh?",   "cosh",     "curry",
    "cycle",    "decodeFloat",          r"div(?:Mod)?",   r"drop(?:While)?",
    "either",   "elem",     "encodeFloat",
    r"enumFrom(?:Then)?(?:To)?",
    "error",    "even",     "exp",      "exponent", "fail",     "filter",
    "flip",     "floatDigits",          "floatRadix",           "floatRange",
    "floor",    "fmap",     r"fold[lr]1?",
    "fromEnum", "fromInteger",          "fromIntegral",         "fromRational",
    "fst",      "gcd",      "getChar",  "getContents",          "getLine",
    "head",     "id",       "init",     "interact", "ioError",
    "isDenormalized",       "isIEEE",   "isInfinite",           "isNaN",
    "isNegativeZero",       "iterate",  "last",     "lcm",      "length",
    "lex",      "lines",    r"log(?:Base)?",        "lookup",   "map",
    r"mapM_?",  r"max(?:Bound|imum)?"   "maybe",
    r"min(?:Bound|imum)?",  "mod",      "negate",   r"not(?:Elem)?",
    "null",     "odd",      "or",       "otherwise",
    "pi",       "pred",     "print",    "product",  "properFraction",
    "putChar",  r"putStr(?:Ln)?",       r"quot(?:Rem)?",
    r"read(?:File|IO|List|Ln|Paren|s(?:Prec)?)?",
    "realToFrac",           "recip",
    "rem",      "repeat",   "replicate",            "return",   "reverse",
    "round",    "scaleFloat",           r"scan[lr]1?",
    r"seq(?:uence_?)?",     r"show(?:Char|List|Paren|String|s(?:Prec)?)?",
    "significand",          "signum",
    r"sinh?",   "snd",      "span",     "splitAt",  "sqrt",
    "subtract", "succ",     "sum",      "tail",     r"take(?:While)?",
    r"tanh?",     "toEnum", "toInteger",            "toRational",
    "truncate", "uncurry",  "undefined",            "unlines",  "until",
    "unwords",  r"unzip3?", "userError",            "words",
    "writeFile",            r"zip3?",   r"zipWith3?",
]

identifiers = [
    r"[_a-z][\w']*",
]

strings = [
    r"'(?:[^\\']|\\(?:^.|[A-Z]+|\d+|o[0-7]+|x[0-9A-Fa-f]+))'?",
    r'"[^\\"]*(?:\\.[^\\"]+)*"?',
]

comments = [
    r"-- [^\n]*",
    r"(?P<NCOM>\{-(?:(?:[^{-]|-[^}])+|(?P&NCOM))*-\})",
]


KEYWORD = (
    any("KEYWORD", [r'\b(?:' + r'|'.join(keywords) + r')\b']) + r'|' +
    any("OPERATOR", operators)
)
BUILTIN = any("BUILTIN", builtin_funcs+numbers)
COMMENT = any("COMMENT", comments)
STRING = any("STRING", strings)
DEFINITION = ""

MISC = r'|'.join(
    [
        any("IDENTIFIER", identifiers),
    ]
)


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
            if line[i] in ('"'):  # todo eat ' properly
                quot = line[i]

        i += 1

    return ''.join(line)

def get_lineindex(chars, begin, end):
    linestart = begin
    while linestart > 0:
        if chars[linestart] == '\n':
            if chars[linestart-1] != '\\':
                break

        linestart -= 1

    lineend = end
    while lineend < len(chars):
        if chars[lineend] == '\n':
            break
        elif chars[lineend] == '\\':
            lineend += 1

        lineend += 1

    if lineend > len(chars):
        lineend = len(chars)

    # todo
    while chars[linestart] == '\n':
        linestart += 1

    return (linestart, lineend)

def specify_tag(chars, begin, end):
    chars = eat_quote(chars)
    linestart, lineend = get_lineindex(chars, begin, end)
    line = chars[linestart:lineend]

    if chars[linestart:begin].strip() == "":
        if "=" in chars[end:lineend]:
            return "DEFINITION"

        if "::" in chars[end:lineend]:
            return "DEFINITION"

    m = regex.match(r'\w+', line.lstrip())
    if m is None:
        return

    if m.group() in ("data", "class", "newtype", "let"):
        return "DEFINITION"

def deco_identifier(cdelegator, head, key, lchars, m):
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

more_decorate = {
    "IDENTIFIER": deco_identifier,
}

