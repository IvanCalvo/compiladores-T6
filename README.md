# Trabalho final da disciplina de Compiladores

# Autores

  Ivan Duarte Calvo - RA: 790739  
  João Ricardo Lopes Lovato - RA: 772138  
  Vinícius Borges de Lima - RA: 795316  

# Descrição

  O propósito da linguagem e compilador criados é de compilar uma linguagem textual contendo notas musicais e *loops*, construir as estruturas necessárias e por fim gerar um arquivo de áudio final.

  Um exemplo da linguagem criada é o seguinte:
      
      riff r1 = (E4-3, A3-3, C4-3, E4-3, B3-3, E3-3, G3-3, B3-3, C4-3, F3-3, A3-3)

      riff r2 = (C4-3, D4-3, G3-3, B3-3, D4-3, E4-3, A3-3, C4-3, E4-3, B3-3, E3-3)

      riff r3 = (C#4-3, B3-3, C4-3, F3-3, A3-3, C4-3, D4-3, G3-3, B3-3, D4-3)

      tocar(r1, 1; r2, 1; r3, 1)
  
  Nesse exemplo pode-se observar a existência dos *riffs*, que são trechos contendo uma ou mais notas, onde cada nota possui também uma duração. Além dos *riffs* também existe a estrutura *tocar* que é um conjunto de *riffs* que podem ser repetidos também uma ou mais vezes cada.

# Instalação e execução do compilador
## Programas necessários

  O código foi escrito na linguagem *Python 3.10*, e também foi utilizado o *ANTLR 4.12.0*. Os arquivos e instruções para *downloads* e instalações podem ser encontrados nos seguintes endereços:  
  https://www.python.org/downloads/  
  https://www.antlr.org/download.html
    

## Biliotecas utilizadas

  Para a execução do código é necessária a instalação da biblioteca *MIDIUtil* que pode ser feita através do seguinte comando
      
      pip install MIDIUtil

## Compilação e execução do programa
  
  O arquivo *Lexer* gerado pelo *ANTLR* pode ser criado através do seguinte comando:
     
     antlr4 -Dlanguage=Python3 gramatica.g4

Após isso, a compilação e execução do código *main.py* é realizada com o comando:

    python3 main.py arquivo_de_entrada arquivo_de_saida

# Sobre a linguagem

## Definição 
A linguagem Pymidi permite ao usuário compor músicas e exportando elas para mid no final de sua execução, a música consiste de `riffs`, que serão então dispostos pelo usuário para então formar a música por completo

## Como usar
Pymidi é uma linguagem simples, e possui apenas 2 comandos principais

### Riff
riff [nome_do_riff] = ((NOTA POSICAO,DURACAO)+)

#### Nota
A nota a ser tocada (as notas podem ir de A a G)

#### Duração 
A duração da nota, começando em 0. A duração da nota é específicada como um múltiplo de 100 milissegundos, por exemplo, uma duração de 5 implica em 500 millisegundos.

#### Exemplo de riff
riff refrao = (E4,3,G2,1,A3,2)

### Tocar
tocar(riffs,quantidade) separado por vírgula

#### Riffs
Os riffs do tocar precisam ter sido declarados anteriormente através do comando `riff`

#### Quantidade
Número de vezes que o riff será repetido
 
#### Exemplo do uso de tocar
tocar(r1,2,r3,1)

### Agradecimentos
Agradecimento especial ao professor da disciplina Daniel Lucrédio e também à Yan Köhler por ajudar com a leitura de partituras.





 
