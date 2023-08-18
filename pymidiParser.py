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
        4,1,9,29,2,0,7,0,2,1,7,1,1,0,4,0,6,8,0,11,0,12,0,7,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,22,8,1,10,1,12,1,25,9,1,1,
        1,1,1,1,1,0,0,2,0,2,0,0,28,0,5,1,0,0,0,2,11,1,0,0,0,4,6,3,2,1,0,
        5,4,1,0,0,0,6,7,1,0,0,0,7,5,1,0,0,0,7,8,1,0,0,0,8,9,1,0,0,0,9,10,
        5,0,0,1,10,1,1,0,0,0,11,12,5,1,0,0,12,13,5,8,0,0,13,14,5,2,0,0,14,
        15,5,5,0,0,15,16,5,6,0,0,16,23,5,7,0,0,17,18,5,3,0,0,18,19,5,5,0,
        0,19,20,5,6,0,0,20,22,5,7,0,0,21,17,1,0,0,0,22,25,1,0,0,0,23,21,
        1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,27,5,4,0,0,
        27,3,1,0,0,0,2,7,23
    ]

class pymidiParser ( Parser ):

    grammarFileName = "pymidi.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'riff'", "'('", "','", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NOTA", "POSICAO", "DURACAO", "IDENT", 
                      "WS" ]

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
    DURACAO=7
    IDENT=8
    WS=9

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

        def DURACAO(self, i:int=None):
            if i is None:
                return self.getTokens(pymidiParser.DURACAO)
            else:
                return self.getToken(pymidiParser.DURACAO, i)

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
            self.match(pymidiParser.IDENT)
            self.state = 13
            self.match(pymidiParser.T__1)
            self.state = 14
            self.match(pymidiParser.NOTA)
            self.state = 15
            self.match(pymidiParser.POSICAO)
            self.state = 16
            self.match(pymidiParser.DURACAO)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 17
                self.match(pymidiParser.T__2)
                self.state = 18
                self.match(pymidiParser.NOTA)
                self.state = 19
                self.match(pymidiParser.POSICAO)
                self.state = 20
                self.match(pymidiParser.DURACAO)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(pymidiParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





