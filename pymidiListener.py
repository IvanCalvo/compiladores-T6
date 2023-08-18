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


    # Enter a parse tree produced by pymidiParser#trecho.
    def enterTrecho(self, ctx:pymidiParser.TrechoContext):
        pass

    # Exit a parse tree produced by pymidiParser#trecho.
    def exitTrecho(self, ctx:pymidiParser.TrechoContext):
        pass


    # Enter a parse tree produced by pymidiParser#loop.
    def enterLoop(self, ctx:pymidiParser.LoopContext):
        pass

    # Exit a parse tree produced by pymidiParser#loop.
    def exitLoop(self, ctx:pymidiParser.LoopContext):
        pass



del pymidiParser