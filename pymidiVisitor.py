# Generated from pymidi.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pymidiParser import pymidiParser
else:
    from pymidiParser import pymidiParser

# This class defines a complete generic visitor for a parse tree produced by pymidiParser.

class pymidiVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by pymidiParser#program.
    def visitProgram(self, ctx:pymidiParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pymidiParser#declaracoes.
    def visitDeclaracoes(self, ctx:pymidiParser.DeclaracoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pymidiParser#loops.
    def visitLoops(self, ctx:pymidiParser.LoopsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pymidiParser#declaracao_trecho.
    def visitDeclaracao_trecho(self, ctx:pymidiParser.Declaracao_trechoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pymidiParser#valor_trecho.
    def visitValor_trecho(self, ctx:pymidiParser.Valor_trechoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pymidiParser#toque.
    def visitToque(self, ctx:pymidiParser.ToqueContext):
        print(ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pymidiParser#loop.
    def visitLoop(self, ctx:pymidiParser.LoopContext):
        return self.visitChildren(ctx)



del pymidiParser