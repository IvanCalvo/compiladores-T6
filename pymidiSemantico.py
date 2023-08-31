# Generated from pymidi.g4 by ANTLR 4.12.0
from antlr4 import *
from pymidiVisitor import pymidiVisitor
from Gerador import *
if __name__ is not None and "." in __name__:
    from .pymidiParser import pymidiParser
else:
    from pymidiParser import pymidiParser

# This class defines a complete generic visitor for a parse tree produced by pymidiParser.
class pymidiSemantico(pymidiVisitor):

    # Visit a parse tree produced by pymidiParser#program.
    def visitProgram(self, ctx:pymidiParser.ProgramContext):
        self.visitDeclaracoes(ctx.declaracoes())
        self.visitLoops(ctx.loops())

    # Visit a parse tree produced by pymidiParser#declaracoes.
    def visitDeclaracoes(self, ctx:pymidiParser.DeclaracoesContext):
        if ctx.declaracao_trecho is not None:
            
            for i, c in enumerate(ctx.declaracao_trecho()):
                declaracao = self.visitDeclaracao_trecho(c)
                nome_riff = declaracao.split('=')[0][4:]
                g1.addRiff(nome_riff)
                notas = (declaracao.split('=')[1][1:-1]).split(',')
                for nota in notas:
                    duracao = int(nota[-1])
                    g1.addNota(nome_riff, nota[:-1])
                    g1.addDuracao(nome_riff, duracao)
    
        
    # Visit a parse tree produced by pymidiParser#loops.
    def visitLoops(self, ctx:pymidiParser.LoopsContext):
        if ctx.loop is not None:

            for i, c in enumerate(ctx.loop()):
                riffs = self.visitLoop(c)[6:-1].split(';')
                for riff in riffs:
                    nome_riff = riff.split(',')[0]
                    quantidade = int(riff.split(',')[1])
                    for x in range(quantidade):
                        g1.Tocar(nome_riff)
        
        g1.Gerar()
        
    # Visit a parse tree produced by pymidiParser#declaracao_trecho.
    def visitDeclaracao_trecho(self, ctx:pymidiParser.Declaracao_trechoContext):
        return ctx.getText()


    # Visit a parse tree produced by pymidiParser#valor_trecho.
    def visitValor_trecho(self, ctx:pymidiParser.Valor_trechoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pymidiParser#toque.
    def visitToque(self, ctx:pymidiParser.ToqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pymidiParser#loop.
    def visitLoop(self, ctx:pymidiParser.LoopContext):
        return ctx.getText()