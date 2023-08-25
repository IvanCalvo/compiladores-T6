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
from pymidiLexer import pymidiLexer
from pymidiParser import pymidiParser
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

#parser.program()

token = lexer.nextToken()

while token.type != Token.EOF:

    # Aplicando a formatacao padrao para as palavras chave
    txt = '\'' + token.text + '\''
    

    # Identificando o tipo do token
    typeStr = pymidiLexer.symbolicNames[token.type]
    
    
    if (typeStr in tipos_definidos):
        output_file.write('<'+ txt + "," + typeStr + '>\n')
    else:
        output_file.write('<' + txt + ',' + txt + '>\n')
    

    token = lexer.nextToken()


output_file.close()