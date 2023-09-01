'''
    Autores:
    Ivan Duarte Calvo RA: 790739
    João Ricardo Lopes Lovato RA: 772138
    Vinícius Borges de Lima RA: 795316

    COMPILAÇÃO:
    o programa pode ser compilado através do seguinte comando:
        python3 main.py arquivo_de_entrada.txt arquivo_de_saida.txt
'''

import sys
from antlr4 import *
from antlr4.error.ErrorListener import *
from antlr4.tree.Trees import Trees
from pymidiLexer import pymidiLexer
from pymidiParser import pymidiParser
from pymidiVisitor import pymidiVisitor
from pymidiListener import pymidiListener
from pymidiSemantico import pymidiSemantico
from pymidiUtils import *
from Gerador import *
from antlr4.error.ErrorListener import ErrorListener

#classe de mensangens customizadas de erros
class pymidiErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        errorText = offendingSymbol.text
        
        if 'mismatched' in msg:
            utils.adicionarErro(f'Linha {offendingSymbol.line}: \'{errorText}\' não reconhecido')
        else:
            utils.adicionarErro(f'Linha {offendingSymbol.line}: erro proximo a {errorText}')

        if errorText == '<EOF>':
            errorText = 'EOF'
        

# Verificando se todos os argumentos necessarios foram passados
if len(sys.argv) < 3:
    print("É necessário fornecer o nome dos arquivos de entrada e saida como argumento.")
    sys.exit(1)

# Os argumentos representam os arquivos de entrada e saida respectivamente 
input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

g1.nome = output_file_name

# Criando um InputStream atraves do arquivo de entrada
input_stream = FileStream(input_file_name, encoding='utf-8')

lexer = pymidiLexer(input_stream)
lexer.removeErrorListeners()
stream = CommonTokenStream(lexer)
parser = pymidiParser(stream)
parser.removeErrorListeners()
parser.addErrorListener(pymidiErrorListener())

# Geração da árvore de análise
tree = parser.program()

printer = pymidiListener()
walker = ParseTreeWalker()
walker.walk(printer, tree)

semantico = pymidiSemantico()

if len(utils.erros) == 0:
    semantico.visitProgram(tree)
    if len(utils.erros) == 0:
        g1.Gerar()
        
if len(utils.erros) > 0:
    #Criando um arquivo de saida
    output_file = open(f"{output_file_name}_out.txt","w")
    for erro in utils.erros:
        output_file.write(erro + '\n')
    output_file.close()
