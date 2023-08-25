grammar pymidi;

program
    :
    declaracoes loops EOF
    ;

declaracoes
    :
    declaracao_trecho*
    ;

loops
    :
    loop*
    ;

declaracao_trecho
    :
    'riff' nome '=' valor_trecho
    ;

valor_trecho
    :
    '(' (NOTA POSICAO NUM | '-' ) (',' NOTA POSICAO NUM | '-' )* ')'
    ;

loop
    :
    'tocar' '(' nome ',' NUM (';' nome ',' NUM)* ')'
    ;


//lexer
POSICAO
    :
    NUM
    ;

NUM
    :
    ('0'..'9')+('.'('0'..'9')+)?
    ; 

nome
    :
    IDENT ('_' IDENT)*
    ;

//identificadores
IDENT
    :   
    [a-zA-Z][a-zA-Z0-9_]*
    ;

NOTA
    :
    'C' | 'C#' | 'D' | 'D#' | 'E' | 'F' | 'F#' | 'G' |
    'G#' | 'A' | 'A#' | 'B'
    ;

// Ignorando White Space
WS  
    :   
        ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) -> skip
    ;