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
    'KEYWORD': {_f: RED, _b: WHITE},
    'BUILTIN': {_f: SKY, _b: WHITE},
    'STRING': {_f: INDIGO, _b: WHITE},
    'DEFINITION': {_f: PURPLE, _b: WHITE},
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
    'PREPROCESSOR': {_f: RED, _b: WHITE},
    'SHARP': {_f:BLACK, _b:WHITE},
    'PUNC': {_f:BLACK, _b:WHITE},
    'LINK': {_f:BLACK, _b:WHITE, 'font':(font, 10, 'underline')},

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
}

##append_tags = dict(
##    (k, dict(d.items()+[('font', font)])) for k, d in _append_tags.items()
##)
