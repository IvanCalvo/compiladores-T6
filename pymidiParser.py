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
        4,1,7,24,2,0,7,0,2,1,7,1,1,0,4,0,6,8,0,11,0,12,0,7,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,5,1,17,8,1,10,1,12,1,20,9,1,1,1,1,1,1,1,0,0,2,0,2,
        0,0,23,0,5,1,0,0,0,2,11,1,0,0,0,4,6,3,2,1,0,5,4,1,0,0,0,6,7,1,0,
        0,0,7,5,1,0,0,0,7,8,1,0,0,0,8,9,1,0,0,0,9,10,5,0,0,1,10,1,1,0,0,
        0,11,12,5,1,0,0,12,13,5,2,0,0,13,18,5,5,0,0,14,15,5,3,0,0,15,17,
        5,5,0,0,16,14,1,0,0,0,17,20,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,
        19,21,1,0,0,0,20,18,1,0,0,0,21,22,5,4,0,0,22,3,1,0,0,0,2,7,18
    ]

class pymidiParser ( Parser ):

    grammarFileName = "pymidi.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'riff'", "'('", "','", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NOTA", "POSICAO", "WS" ]

    RULE_program = 0
    RULE_trecho = 1

    ruleNames =  [ "program", "trecho" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    NOTA=5
    POSICAO=6
    WS=7

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

        def trecho(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pymidiParser.TrechoContext)
            else:
                return self.getTypedRuleContext(pymidiParser.TrechoContext,i)


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
            self.state = 5 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                self.trecho()
                self.state = 7 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

            self.state = 9
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

        def NOTA(self, i:int=None):
            if i is None:
                return self.getTokens(pymidiParser.NOTA)
            else:
                return self.getToken(pymidiParser.NOTA, i)

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
            self.state = 11
            self.match(pymidiParser.T__0)
            self.state = 12
            self.match(pymidiParser.T__1)
            self.state = 13
            self.match(pymidiParser.NOTA)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 14
                self.match(pymidiParser.T__2)
                self.state = 15
                self.match(pymidiParser.NOTA)
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 21
            self.match(pymidiParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





