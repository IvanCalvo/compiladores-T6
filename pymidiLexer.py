# Generated from pymidi.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,50,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,43,8,4,1,5,
        1,5,1,6,1,6,1,6,1,6,0,0,7,1,1,3,2,5,3,7,4,9,5,11,6,13,7,1,0,1,3,
        0,9,10,13,13,32,32,59,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,
        0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,1,15,1,0,0,0,3,20,1,
        0,0,0,5,22,1,0,0,0,7,24,1,0,0,0,9,42,1,0,0,0,11,44,1,0,0,0,13,46,
        1,0,0,0,15,16,5,114,0,0,16,17,5,105,0,0,17,18,5,102,0,0,18,19,5,
        102,0,0,19,2,1,0,0,0,20,21,5,40,0,0,21,4,1,0,0,0,22,23,5,44,0,0,
        23,6,1,0,0,0,24,25,5,41,0,0,25,8,1,0,0,0,26,43,5,67,0,0,27,28,5,
        67,0,0,28,43,5,35,0,0,29,43,5,68,0,0,30,31,5,68,0,0,31,43,5,35,0,
        0,32,43,2,69,70,0,33,34,5,70,0,0,34,43,5,35,0,0,35,43,5,71,0,0,36,
        37,5,71,0,0,37,43,5,35,0,0,38,43,5,65,0,0,39,40,5,65,0,0,40,43,5,
        35,0,0,41,43,5,66,0,0,42,26,1,0,0,0,42,27,1,0,0,0,42,29,1,0,0,0,
        42,30,1,0,0,0,42,32,1,0,0,0,42,33,1,0,0,0,42,35,1,0,0,0,42,36,1,
        0,0,0,42,38,1,0,0,0,42,39,1,0,0,0,42,41,1,0,0,0,43,10,1,0,0,0,44,
        45,2,49,55,0,45,12,1,0,0,0,46,47,7,0,0,0,47,48,1,0,0,0,48,49,6,6,
        0,0,49,14,1,0,0,0,2,0,42,1,6,0,0
    ]

class pymidiLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    NOTA = 5
    POSICAO = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'riff'", "'('", "','", "')'" ]

    symbolicNames = [ "<INVALID>",
            "NOTA", "POSICAO", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "NOTA", "POSICAO", "WS" ]

    grammarFileName = "pymidi.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


