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
        4,1,14,80,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,1,1,5,1,20,8,1,10,1,12,1,23,9,1,1,2,5,2,26,8,2,
        10,2,12,2,29,9,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,3,4,41,
        8,4,1,4,1,4,1,4,1,4,1,4,5,4,48,8,4,10,4,12,4,51,9,4,1,4,1,4,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,65,8,5,10,5,12,5,68,9,5,
        1,5,1,5,1,6,1,6,1,6,5,6,75,8,6,10,6,12,6,78,9,6,1,6,0,0,7,0,2,4,
        6,8,10,12,0,0,79,0,14,1,0,0,0,2,21,1,0,0,0,4,27,1,0,0,0,6,30,1,0,
        0,0,8,35,1,0,0,0,10,54,1,0,0,0,12,71,1,0,0,0,14,15,3,2,1,0,15,16,
        3,4,2,0,16,17,5,0,0,1,17,1,1,0,0,0,18,20,3,6,3,0,19,18,1,0,0,0,20,
        23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,3,1,0,0,0,23,21,1,0,0,
        0,24,26,3,10,5,0,25,24,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,
        1,0,0,0,28,5,1,0,0,0,29,27,1,0,0,0,30,31,5,1,0,0,31,32,3,12,6,0,
        32,33,5,2,0,0,33,34,3,8,4,0,34,7,1,0,0,0,35,40,5,3,0,0,36,37,5,13,
        0,0,37,38,5,10,0,0,38,41,5,11,0,0,39,41,5,4,0,0,40,36,1,0,0,0,40,
        39,1,0,0,0,41,49,1,0,0,0,42,43,5,5,0,0,43,44,5,13,0,0,44,45,5,10,
        0,0,45,48,5,11,0,0,46,48,5,4,0,0,47,42,1,0,0,0,47,46,1,0,0,0,48,
        51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,49,1,0,0,
        0,52,53,5,6,0,0,53,9,1,0,0,0,54,55,5,7,0,0,55,56,5,3,0,0,56,57,3,
        12,6,0,57,58,5,5,0,0,58,66,5,11,0,0,59,60,5,8,0,0,60,61,3,12,6,0,
        61,62,5,5,0,0,62,63,5,11,0,0,63,65,1,0,0,0,64,59,1,0,0,0,65,68,1,
        0,0,0,66,64,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,0,68,66,1,0,0,0,69,
        70,5,6,0,0,70,11,1,0,0,0,71,76,5,12,0,0,72,73,5,9,0,0,73,75,5,12,
        0,0,74,72,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,13,
        1,0,0,0,78,76,1,0,0,0,7,21,27,40,47,49,66,76
    ]

class pymidiParser ( Parser ):

    grammarFileName = "pymidi.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'riff'", "'='", "'('", "'-'", "','", 
                     "')'", "'tocar'", "';'", "'_'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "POSICAO", "NUM", "IDENT", 
                      "NOTA", "WS" ]

    RULE_program = 0
    RULE_declaracoes = 1
    RULE_loops = 2
    RULE_declaracao_trecho = 3
    RULE_valor_trecho = 4
    RULE_loop = 5
    RULE_nome = 6

    ruleNames =  [ "program", "declaracoes", "loops", "declaracao_trecho", 
                   "valor_trecho", "loop", "nome" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    POSICAO=10
    NUM=11
    IDENT=12
    NOTA=13
    WS=14

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

        def declaracoes(self):
            return self.getTypedRuleContext(pymidiParser.DeclaracoesContext,0)


        def loops(self):
            return self.getTypedRuleContext(pymidiParser.LoopsContext,0)


        def EOF(self):
            return self.getToken(pymidiParser.EOF, 0)

        def getRuleIndex(self):
            return pymidiParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = pymidiParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.declaracoes()
            self.state = 15
            self.loops()
            self.state = 16
            self.match(pymidiParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracao_trecho(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pymidiParser.Declaracao_trechoContext)
            else:
                return self.getTypedRuleContext(pymidiParser.Declaracao_trechoContext,i)


        def getRuleIndex(self):
            return pymidiParser.RULE_declaracoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracoes" ):
                listener.enterDeclaracoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracoes" ):
                listener.exitDeclaracoes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracoes" ):
                return visitor.visitDeclaracoes(self)
            else:
                return visitor.visitChildren(self)




    def declaracoes(self):

        localctx = pymidiParser.DeclaracoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 18
                self.declaracao_trecho()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pymidiParser.LoopContext)
            else:
                return self.getTypedRuleContext(pymidiParser.LoopContext,i)


        def getRuleIndex(self):
            return pymidiParser.RULE_loops

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoops" ):
                listener.enterLoops(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoops" ):
                listener.exitLoops(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoops" ):
                return visitor.visitLoops(self)
            else:
                return visitor.visitChildren(self)




    def loops(self):

        localctx = pymidiParser.LoopsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 24
                self.loop()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracao_trechoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nome(self):
            return self.getTypedRuleContext(pymidiParser.NomeContext,0)


        def valor_trecho(self):
            return self.getTypedRuleContext(pymidiParser.Valor_trechoContext,0)


        def getRuleIndex(self):
            return pymidiParser.RULE_declaracao_trecho

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_trecho" ):
                listener.enterDeclaracao_trecho(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_trecho" ):
                listener.exitDeclaracao_trecho(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracao_trecho" ):
                return visitor.visitDeclaracao_trecho(self)
            else:
                return visitor.visitChildren(self)




    def declaracao_trecho(self):

        localctx = pymidiParser.Declaracao_trechoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracao_trecho)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(pymidiParser.T__0)
            self.state = 31
            self.nome()
            self.state = 32
            self.match(pymidiParser.T__1)
            self.state = 33
            self.valor_trecho()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Valor_trechoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            return pymidiParser.RULE_valor_trecho

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor_trecho" ):
                listener.enterValor_trecho(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor_trecho" ):
                listener.exitValor_trecho(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValor_trecho" ):
                return visitor.visitValor_trecho(self)
            else:
                return visitor.visitChildren(self)




    def valor_trecho(self):

        localctx = pymidiParser.Valor_trechoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_valor_trecho)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(pymidiParser.T__2)
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 36
                self.match(pymidiParser.NOTA)
                self.state = 37
                self.match(pymidiParser.POSICAO)
                self.state = 38
                self.match(pymidiParser.NUM)
                pass
            elif token in [4]:
                self.state = 39
                self.match(pymidiParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4 or _la==5:
                self.state = 47
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [5]:
                    self.state = 42
                    self.match(pymidiParser.T__4)
                    self.state = 43
                    self.match(pymidiParser.NOTA)
                    self.state = 44
                    self.match(pymidiParser.POSICAO)
                    self.state = 45
                    self.match(pymidiParser.NUM)
                    pass
                elif token in [4]:
                    self.state = 46
                    self.match(pymidiParser.T__3)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
            self.match(pymidiParser.T__5)
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

        def nome(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pymidiParser.NomeContext)
            else:
                return self.getTypedRuleContext(pymidiParser.NomeContext,i)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop" ):
                return visitor.visitLoop(self)
            else:
                return visitor.visitChildren(self)




    def loop(self):

        localctx = pymidiParser.LoopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_loop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(pymidiParser.T__6)
            self.state = 55
            self.match(pymidiParser.T__2)
            self.state = 56
            self.nome()
            self.state = 57
            self.match(pymidiParser.T__4)
            self.state = 58
            self.match(pymidiParser.NUM)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 59
                self.match(pymidiParser.T__7)
                self.state = 60
                self.nome()
                self.state = 61
                self.match(pymidiParser.T__4)
                self.state = 62
                self.match(pymidiParser.NUM)
                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
            self.match(pymidiParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NomeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(pymidiParser.IDENT)
            else:
                return self.getToken(pymidiParser.IDENT, i)

        def getRuleIndex(self):
            return pymidiParser.RULE_nome

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNome" ):
                listener.enterNome(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNome" ):
                listener.exitNome(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNome" ):
                return visitor.visitNome(self)
            else:
                return visitor.visitChildren(self)




    def nome(self):

        localctx = pymidiParser.NomeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_nome)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(pymidiParser.IDENT)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 72
                self.match(pymidiParser.T__8)
                self.state = 73
                self.match(pymidiParser.IDENT)
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





