# Generated from pymidi.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,48,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,24,8,1,10,1,12,1,
        27,9,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,41,8,
        2,10,2,12,2,44,9,2,1,2,1,2,1,2,0,0,3,0,2,4,0,0,47,0,7,1,0,0,0,2,
        13,1,0,0,0,4,30,1,0,0,0,6,8,3,4,2,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,
        1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,0,11,12,5,0,0,1,12,1,1,0,0,0,13,
        14,5,1,0,0,14,15,5,10,0,0,15,16,5,2,0,0,16,17,5,7,0,0,17,18,5,8,
        0,0,18,25,5,9,0,0,19,20,5,3,0,0,20,21,5,7,0,0,21,22,5,8,0,0,22,24,
        5,9,0,0,23,19,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,
        26,28,1,0,0,0,27,25,1,0,0,0,28,29,5,4,0,0,29,3,1,0,0,0,30,31,5,5,
        0,0,31,32,5,2,0,0,32,33,3,2,1,0,33,34,5,3,0,0,34,42,5,9,0,0,35,36,
        5,6,0,0,36,37,3,2,1,0,37,38,5,3,0,0,38,39,5,9,0,0,39,41,1,0,0,0,
        40,35,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,45,1,
        0,0,0,44,42,1,0,0,0,45,46,5,4,0,0,46,5,1,0,0,0,3,9,25,42
    ]

class pymidiParser ( Parser ):

    grammarFileName = "pymidi.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'riff'", "'('", "','", "')'", "'tocar'", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NOTA", "POSICAO", 
                      "NUM", "IDENT", "WS" ]

    RULE_program = 0
    RULE_trecho = 1
    RULE_loop = 2

    ruleNames =  [ "program", "trecho", "loop" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NOTA=7
    POSICAO=8
    NUM=9
    IDENT=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(pymidiParser.EOF, 0)

        def loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pymidiParser.LoopContext)
            else:
                return self.getTypedRuleContext(pymidiParser.LoopContext,i)


        def getRuleIndex(self):
            return pymidiParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = pymidiParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.loop()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5):
                    break

            self.state = 11
            self.match(pymidiParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TrechoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(pymidiParser.IDENT, 0)

        def NOTA(self, i:int=None):
            if i is None:
                return self.getTokens(pymidiParser.NOTA)
            else:
                return self.getToken(pymidiParser.NOTA, i)

        def POSICAO(self, i:int=None):
            if i is None:
                return self.getTokens(pymidiParser.POSICAO)
            else:
                return self.getToken(pymidiParser.POSICAO, i)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(pymidiParser.NUM)
            else:
                return self.getToken(pymidiParser.NUM, i)

        def getRuleIndex(self):
            return pymidiParser.RULE_trecho

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrecho" ):
                listener.enterTrecho(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrecho" ):
                listener.exitTrecho(self)




    def trecho(self):

        localctx = pymidiParser.TrechoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_trecho)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(pymidiParser.T__0)
            self.state = 14
            self.match(pymidiParser.IDENT)
            self.state = 15
            self.match(pymidiParser.T__1)
            self.state = 16
            self.match(pymidiParser.NOTA)
            self.state = 17
            self.match(pymidiParser.POSICAO)
            self.state = 18
            self.match(pymidiParser.NUM)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 19
                self.match(pymidiParser.T__2)
                self.state = 20
                self.match(pymidiParser.NOTA)
                self.state = 21
                self.match(pymidiParser.POSICAO)
                self.state = 22
                self.match(pymidiParser.NUM)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(pymidiParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def trecho(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pymidiParser.TrechoContext)
            else:
                return self.getTypedRuleContext(pymidiParser.TrechoContext,i)


        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(pymidiParser.NUM)
            else:
                return self.getToken(pymidiParser.NUM, i)

        def getRuleIndex(self):
            return pymidiParser.RULE_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop" ):
                listener.enterLoop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop" ):
                listener.exitLoop(self)




    def loop(self):

        localctx = pymidiParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(pymidiParser.T__4)
            self.state = 31
            self.match(pymidiParser.T__1)
            self.state = 32
            self.trecho()
            self.state = 33
            self.match(pymidiParser.T__2)
            self.state = 34
            self.match(pymidiParser.NUM)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 35
                self.match(pymidiParser.T__5)
                self.state = 36
                self.trecho()
                self.state = 37
                self.match(pymidiParser.T__2)
                self.state = 38
                self.match(pymidiParser.NUM)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(pymidiParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





