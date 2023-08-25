# Generated from pymidi.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pymidiParser import pymidiParser
else:
    from pymidiParser import pymidiParser

# This class defines a complete listener for a parse tree produced by pymidiParser.
class pymidiListener(ParseTreeListener):

    # Enter a parse tree produced by pymidiParser#program.
    def enterProgram(self, ctx:pymidiParser.ProgramContext):
        pass

    # Exit a parse tree produced by pymidiParser#program.
    def exitProgram(self, ctx:pymidiParser.ProgramContext):
        pass


    # Enter a parse tree produced by pymidiParser#declaracoes.
    def enterDeclaracoes(self, ctx:pymidiParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by pymidiParser#declaracoes.
    def exitDeclaracoes(self, ctx:pymidiParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by pymidiParser#loops.
    def enterLoops(self, ctx:pymidiParser.LoopsContext):
        pass

    # Exit a parse tree produced by pymidiParser#loops.
    def exitLoops(self, ctx:pymidiParser.LoopsContext):
        pass


    # Enter a parse tree produced by pymidiParser#declaracao_trecho.
    def enterDeclaracao_trecho(self, ctx:pymidiParser.Declaracao_trechoContext):
        pass

    # Exit a parse tree produced by pymidiParser#declaracao_trecho.
    def exitDeclaracao_trecho(self, ctx:pymidiParser.Declaracao_trechoContext):
        pass


    # Enter a parse tree produced by pymidiParser#valor_trecho.
    def enterValor_trecho(self, ctx:pymidiParser.Valor_trechoContext):
        pass

    # Exit a parse tree produced by pymidiParser#valor_trecho.
    def exitValor_trecho(self, ctx:pymidiParser.Valor_trechoContext):
        pass


    # Enter a parse tree produced by pymidiParser#loop.
    def enterLoop(self, ctx:pymidiParser.LoopContext):
        pass

    # Exit a parse tree produced by pymidiParser#loop.
    def exitLoop(self, ctx:pymidiParser.LoopContext):
        pass


    # Enter a parse tree produced by pymidiParser#nome.
    def enterNome(self, ctx:pymidiParser.NomeContext):
        pass

    # Exit a parse tree produced by pymidiParser#nome.
    def exitNome(self, ctx:pymidiParser.NomeContext):
        pass



del pymidiParser