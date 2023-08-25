# Generated from pymidi.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("R\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\2\3\3\7\3\26\n\3\f\3\16\3\31\13\3\3")
        buf.write("\4\7\4\34\n\4\f\4\16\4\37\13\4\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\5\6+\n\6\3\6\3\6\3\6\3\6\3\6\7\6\62\n")
        buf.write("\6\f\6\16\6\65\13\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\7\7C\n\7\f\7\16\7F\13\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\7\bM\n\b\f\b\16\bP\13\b\3\b\2\2\t\2\4\6\b\n\f\16")
        buf.write("\2\2\2Q\2\20\3\2\2\2\4\27\3\2\2\2\6\35\3\2\2\2\b \3\2")
        buf.write("\2\2\n%\3\2\2\2\f8\3\2\2\2\16I\3\2\2\2\20\21\5\4\3\2\21")
        buf.write("\22\5\6\4\2\22\23\7\2\2\3\23\3\3\2\2\2\24\26\5\b\5\2\25")
        buf.write("\24\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2")
        buf.write("\30\5\3\2\2\2\31\27\3\2\2\2\32\34\5\f\7\2\33\32\3\2\2")
        buf.write("\2\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\7\3\2")
        buf.write("\2\2\37\35\3\2\2\2 !\7\3\2\2!\"\5\16\b\2\"#\7\4\2\2#$")
        buf.write("\5\n\6\2$\t\3\2\2\2%*\7\5\2\2&\'\7\17\2\2\'(\7\f\2\2(")
        buf.write("+\7\r\2\2)+\7\6\2\2*&\3\2\2\2*)\3\2\2\2+\63\3\2\2\2,-")
        buf.write("\7\7\2\2-.\7\17\2\2./\7\f\2\2/\62\7\r\2\2\60\62\7\6\2")
        buf.write("\2\61,\3\2\2\2\61\60\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2")
        buf.write("\2\63\64\3\2\2\2\64\66\3\2\2\2\65\63\3\2\2\2\66\67\7\b")
        buf.write("\2\2\67\13\3\2\2\289\7\t\2\29:\7\5\2\2:;\5\16\b\2;<\7")
        buf.write("\7\2\2<D\7\r\2\2=>\7\n\2\2>?\5\16\b\2?@\7\7\2\2@A\7\r")
        buf.write("\2\2AC\3\2\2\2B=\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2")
        buf.write("EG\3\2\2\2FD\3\2\2\2GH\7\b\2\2H\r\3\2\2\2IN\7\16\2\2J")
        buf.write("K\7\13\2\2KM\7\16\2\2LJ\3\2\2\2MP\3\2\2\2NL\3\2\2\2NO")
        buf.write("\3\2\2\2O\17\3\2\2\2PN\3\2\2\2\t\27\35*\61\63DN")
        return buf.getvalue()


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
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

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
            while _la==pymidiParser.T__0:
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
            while _la==pymidiParser.T__6:
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
            if token in [pymidiParser.NOTA]:
                self.state = 36
                self.match(pymidiParser.NOTA)
                self.state = 37
                self.match(pymidiParser.POSICAO)
                self.state = 38
                self.match(pymidiParser.NUM)
                pass
            elif token in [pymidiParser.T__3]:
                self.state = 39
                self.match(pymidiParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==pymidiParser.T__3 or _la==pymidiParser.T__4:
                self.state = 47
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [pymidiParser.T__4]:
                    self.state = 42
                    self.match(pymidiParser.T__4)
                    self.state = 43
                    self.match(pymidiParser.NOTA)
                    self.state = 44
                    self.match(pymidiParser.POSICAO)
                    self.state = 45
                    self.match(pymidiParser.NUM)
                    pass
                elif token in [pymidiParser.T__3]:
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
            while _la==pymidiParser.T__7:
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
            while _la==pymidiParser.T__8:
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





