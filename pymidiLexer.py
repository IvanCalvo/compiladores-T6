# Generated from pymidi.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\13\3\13\3\f\6\f<\n\f\r\f\16\f=\3\f\3\f\6\f")
        buf.write("B\n\f\r\f\16\fC\5\fF\n\f\3\r\3\r\7\rJ\n\r\f\r\16\rM\13")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\5\16_\n\16\3\17\3\17\3\17")
        buf.write("\3\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\3\2\5\4\2C\\c|\6\2\62;C\\")
        buf.write("aac|\5\2\13\f\17\17\"\"\2q\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2")
        buf.write("\5$\3\2\2\2\7&\3\2\2\2\t(\3\2\2\2\13*\3\2\2\2\r,\3\2\2")
        buf.write("\2\17.\3\2\2\2\21\64\3\2\2\2\23\66\3\2\2\2\258\3\2\2\2")
        buf.write("\27;\3\2\2\2\31G\3\2\2\2\33^\3\2\2\2\35`\3\2\2\2\37 \7")
        buf.write("t\2\2 !\7k\2\2!\"\7h\2\2\"#\7h\2\2#\4\3\2\2\2$%\7?\2\2")
        buf.write("%\6\3\2\2\2&\'\7*\2\2\'\b\3\2\2\2()\7/\2\2)\n\3\2\2\2")
        buf.write("*+\7.\2\2+\f\3\2\2\2,-\7+\2\2-\16\3\2\2\2./\7v\2\2/\60")
        buf.write("\7q\2\2\60\61\7e\2\2\61\62\7c\2\2\62\63\7t\2\2\63\20\3")
        buf.write("\2\2\2\64\65\7=\2\2\65\22\3\2\2\2\66\67\7a\2\2\67\24\3")
        buf.write("\2\2\289\5\27\f\29\26\3\2\2\2:<\4\62;\2;:\3\2\2\2<=\3")
        buf.write("\2\2\2=;\3\2\2\2=>\3\2\2\2>E\3\2\2\2?A\7\60\2\2@B\4\62")
        buf.write(";\2A@\3\2\2\2BC\3\2\2\2CA\3\2\2\2CD\3\2\2\2DF\3\2\2\2")
        buf.write("E?\3\2\2\2EF\3\2\2\2F\30\3\2\2\2GK\t\2\2\2HJ\t\3\2\2I")
        buf.write("H\3\2\2\2JM\3\2\2\2KI\3\2\2\2KL\3\2\2\2L\32\3\2\2\2MK")
        buf.write("\3\2\2\2N_\7E\2\2OP\7E\2\2P_\7%\2\2Q_\7F\2\2RS\7F\2\2")
        buf.write("S_\7%\2\2T_\4GH\2UV\7H\2\2V_\7%\2\2W_\7I\2\2XY\7I\2\2")
        buf.write("Y_\7%\2\2Z_\7C\2\2[\\\7C\2\2\\_\7%\2\2]_\7D\2\2^N\3\2")
        buf.write("\2\2^O\3\2\2\2^Q\3\2\2\2^R\3\2\2\2^T\3\2\2\2^U\3\2\2\2")
        buf.write("^W\3\2\2\2^X\3\2\2\2^Z\3\2\2\2^[\3\2\2\2^]\3\2\2\2_\34")
        buf.write("\3\2\2\2`a\t\4\2\2ab\3\2\2\2bc\b\17\2\2c\36\3\2\2\2\b")
        buf.write("\2=CEK^\3\b\2\2")
        return buf.getvalue()


class pymidiLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    POSICAO = 10
    NUM = 11
    IDENT = 12
    NOTA = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'riff'", "'='", "'('", "'-'", "','", "')'", "'tocar'", "';'", 
            "'_'" ]

    symbolicNames = [ "<INVALID>",
            "POSICAO", "NUM", "IDENT", "NOTA", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "POSICAO", "NUM", "IDENT", "NOTA", "WS" ]

    grammarFileName = "pymidi.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


