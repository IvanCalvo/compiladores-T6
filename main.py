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
from antlr4.error.ErrorListener import ErrorListener

#classe de mensangens customizadas de erros léxicos
class pymidiLexerErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        erro = str(e.input)[e.startIndex]

        if erro == '(':
            raise Exception(f'Linha {line}: riff nao fechado')       
        else:
            raise Exception(f'Linha {line}: {erro} - simbolo nao identificado')

#classe de mensangens customizadas de erros léxicos
class pymidiParserErrorListener(ErrorListener):
     def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        errorText = offendingSymbol.text

        if errorText == '<EOF>':
            errorText = 'EOF'
        
        raise Exception(f'Linha {offendingSymbol.line}: erro sintatico proximo a {errorText}')

# Verificando se todos os argumentos necessarios foram passados
if len(sys.argv) < 3:
    print("É necessário fornecer o nome dos arquivos de entrada e saida como argumento.")
    sys.exit(1)

# Os argumentos representam os arquivos de entrada e saida respectivamente 
input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

# Criando um InputStream atraves do arquivo de entrada
input_stream = FileStream(input_file_name, encoding='utf-8')

#Criando um arquivo de saida
output_file = open(output_file_name,"w")

# Utilizando o lexer criado com o ANTLR
lexer = pymidiLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = pymidiParser(stream)

#removendo mensagens de erro padrão do ANTLR
lexer.removeErrorListeners()
parser.removeErrorListeners()

#adicionando mensagens de erro customizadas
lexer.addErrorListener(pymidiLexerErrorListener())
parser.addErrorListener(pymidiParserErrorListener())

#lista vazia com os erros
listaErros = []

#lista de tipos definidos
tipos_definidos = ['NOTA', 'NUM', 'POSICAO', 'IDENT']

#chamada principal do programa
lexer = pymidiLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = pymidiParser(tokens)

# Geração da árvore de análise
tree = parser.program()

# Criação de um visitor e visita da árvore de análise
visitor = pymidiVisitor()
#visitor.visit(tree)

semantico = pymidiSemantico()
semantico.visit(tree)

output_file.close()
