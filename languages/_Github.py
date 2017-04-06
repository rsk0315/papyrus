#!/usr/bin/env python

from idlelib.configHandler import idleConf


font = idleConf.GetOption('main', 'EditorWindow', 'font')

_f = 'foreground'
_b = 'background'

GREY = '#969696'
RED = '#a71d5d'
SKY = '#0086b3'
INDIGO = '#183691'
PURPLE = '#795da3'
ORANGE = '#ed6a43'
GREEN = '#63a35c'
WHITE = '#ffffff'
BLACK = '#333333'

append_tags = {
    'COMMENT': {_f: GREY, _b: WHITE},
    'KEYWORD': {_f: RED, _b: WHITE, 'font': (font, 10, 'bold')},
    'BUILTIN': {_f: SKY, _b: WHITE},
    'STRING': {_f: INDIGO, _b: WHITE, 'font': (font, 10, 'bold')},
    'DEFINITION': {_f: PURPLE, _b: WHITE, 'font': (font, 10, 'italic')},
    'ERROR': {_f: '#f8f8f8', _b: '#b52a1d'},
    'SELECTED': {_f: BLACK, _b: '#ffffc5'},  # TODO

    'SP_VARIABLE': {_f: ORANGE, _b: WHITE},
    'FORMAT': {_f: SKY, _b: WHITE},
    'SPECIAL': {_f: SKY, _b: WHITE},
    'SPECIAL_M': {_f: SKY, _b: WHITE},
    'CONSTANT': {_f: SKY, _b: WHITE},
    'OPERATOR': {_f: RED, _b: WHITE},
    'CLASSDEF': {_f: PURPLE, _b: WHITE},
    'FUNCDEF': {_f: PURPLE, _b: WHITE},
    'STRING_PREFIX': {_f: RED, _b: WHITE},
    'PREPROCESSOR': {_f: RED, _b: WHITE, 'font': (font, 10, 'italic')},
    'ATTRIBUTES': {_f: RED, _b: WHITE, 'font': (font, 10, 'italic')},
    'SHARP': {_f:BLACK, _b:WHITE},
    'PUNC': {_f:BLACK, _b:WHITE},
    'LINK': {_f:BLACK, _b:WHITE, 'font':(font, 10, 'underline')},
    'STL_CLASSES': {_f:SKY, _b:WHITE},
    'LINE_COMMENT': {_f: GREY, _b: WHITE, 'font':(font, 10, 'italic')},
    'BLOCK_COMMENT': {_f: GREY, _b: WHITE, 'font':(font, 10, 'bold')},
    'RESERVED': {_f: RED, _b: WHITE},
    'KWVAL': {_f: SKY, _b: WHITE, 'font':(font, 10, 'italic')},

    'RE_SGL': {_f: SKY, _b: WHITE},
    'RE_REPEAT': {_f: RED, _b: WHITE},
    'RE_PAR': {_f: INDIGO, _b: WHITE},
    'RE_NAME': {_f: GREEN, _b: WHITE},
    'RE_PAR': {_f: INDIGO, _b: WHITE},
    'RE_PARENTHESIS': {_f: RED, _b: WHITE},
    'RE_BRACKET': {_f: SKY, _b: WHITE},
    'RE_CARET': {_f: RED, _b: WHITE},
    'RE_CHARS': {_f: SKY, _b: WHITE},
    'RE_SPECIAL': {_f: GREEN, _b: WHITE},

    'NONASCII': {'font': ('Meiryo', 7)},
    'NONASCIIC': {_f: GREY, _b: WHITE, 'font': ('Meiryo', 7)},
##    'NONASCIIB': {_f: GREY, _b: WHITE, 'font': ('Meiryo', 7, 'bold')},
    'NONASCIIB': {_f: GREY, _b: WHITE, 'font': ('Consolas', 10, 'bold')},
    'IDENTIFIER': {_f: BLACK, _b: WHITE},
    'WARNING': {_f: RED, _b: WHITE, 'font': ('Consolas', 10, 'underline')},
    'ASSEMBLY': {_f: SKY, _b: WHITE, 'font': ('Consolas', 10, 'italic')},
    'BOLD': {_f: BLACK, _b: WHITE, 'font': ('Consolas', 10, 'bold')},
    'ITALIC': {_f: BLACK, _b: WHITE, 'font': ('Consolas', 10, 'italic')},
}

##append_tags = dict(
##    (k, dict(d.items()+[('font', font)])) for k, d in _append_tags.items()
##)
